from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Employee, Item
from django.db.models import Q, Count
from datetime import datetime

def home(request):
    return render(request, 'tracker/home.html')

def report_item(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        try:
            employee = Employee.objects.get(employee_id=employee_id)
        except Employee.DoesNotExist:
            messages.error(request, 'Invalid Employee ID')
            return redirect('report_item')
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        item_type = request.POST.get('item_type')
        location = request.POST.get('location')
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        item = Item.objects.create(
            item_name=item_name,
            description=description,
            item_type=item_type,
            location=location,
            date=date,
            employee=employee
        )
        # Smart match
        match_score = 0
        matched_item = None
        opposite_type = 'found' if item_type == 'lost' else 'lost'
        candidates = Item.objects.filter(item_type=opposite_type, status='open')
        for cand in candidates:
            score = 0
            if item.item_name.lower() == cand.item_name.lower():
                score += 50
            if item.location.lower() == cand.location.lower():
                score += 30
            if abs((item.date - cand.date).days) <= 7:
                score += 20
            if score > match_score:
                match_score = score
                matched_item = cand
        if match_score >= 60:
            item.status = 'matched'
            item.save()
            matched_item.status = 'matched'
            matched_item.save()
            messages.success(request, f'Item reported. Possible match found with {match_score}% confidence.')
        else:
            messages.success(request, 'Item reported successfully.')
        return redirect('listings')
    return render(request, 'tracker/report.html')

def listings(request):
    item_type = request.GET.get('type')
    location = request.GET.get('location')
    q = request.GET.get('q')
    items = Item.objects.all()
    if q:
        items = items.filter(Q(item_name__icontains=q) | Q(description__icontains=q))
    if item_type:
        items = items.filter(item_type=item_type)
    if location:
        items = items.filter(location__icontains=location)
    lost_items = items.filter(item_type='lost')
    found_items = items.filter(item_type='found')
    return render(request, 'tracker/listings.html', {
        'lost_items': lost_items,
        'found_items': found_items,
        'item_type': item_type,
        'location': location,
        'q': q,
    })

def close_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.status = 'closed'
    item.save()
    messages.success(request, 'Item marked as returned.')
    return redirect('listings')

def insights(request):
    # Most commonly lost item
    lost_counts = Item.objects.filter(item_type='lost').values('item_name').annotate(count=Count('item_name')).order_by('-count')
    most_lost = lost_counts.first() if lost_counts else None
    # Most frequent location
    location_counts = Item.objects.values('location').annotate(count=Count('location')).order_by('-count')
    most_location = location_counts.first() if location_counts else None
    # Total items recovered
    recovered = Item.objects.filter(status='closed').count()
    return render(request, 'tracker/insights.html', {
        'most_lost': most_lost,
        'most_location': most_location,
        'recovered': recovered,
    })

def employees(request):
    employees = Employee.objects.all()
    return render(request, 'tracker/employees.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')
        department = request.POST.get('department')
        if not Employee.objects.filter(employee_id=employee_id).exists():
            Employee.objects.create(employee_id=employee_id, name=name, department=department)
            messages.success(request, 'Employee added successfully.')
        else:
            messages.error(request, 'Employee ID already exists.')
        return redirect('employees')
    return render(request, 'tracker/add_employee.html')

def delete_employee(request, employee_id):
    try:
        employee = Employee.objects.get(employee_id=employee_id)
        employee.delete()
        messages.success(request, 'Employee removed successfully.')
    except Employee.DoesNotExist:
        messages.error(request, 'Employee not found.')
    return redirect('employees')
