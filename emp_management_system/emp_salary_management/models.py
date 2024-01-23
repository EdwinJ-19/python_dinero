from django.db import models
from emp_management.models import emp

class emp_sal(models.Model):
    employee = models.ForeignKey(emp, on_delete=models.CASCADE)
    salary_amount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.salary_amount}"

    class Meta:
        db_table = 'emp_sal'