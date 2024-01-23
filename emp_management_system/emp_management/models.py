from django.db import models

class emp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.TextField(max_length=100)
    des_CHOICES = (
        ('ASSOCIATE', 'Associate'),
        ('TEAM LEADER', 'TL'),
        ('MANAGER', 'Manager'),
    )
    designation = models.CharField(max_length=50,choices=des_CHOICES,default='ASSOCIATE')
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL,null=True,blank=True)
    department = models.ForeignKey('dept_management.dept',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'emp'