from django.db import models

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.employee_id} - {self.name}"

class Item(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('matched', 'Matched'),
        ('closed', 'Closed'),
    ]
    TYPE_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
    ]
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    item_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    location = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_type} - {self.item_name} at {self.location}"
