from django.db import models

class Person(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_firstname = models.CharField(max_length=50,null=True)
    p_lastname = models.CharField(max_length=50,null=True)
    p_idLine = models.CharField(max_length=50,null=True)  # Placeholder for Line ID
    p_startOfWork = models.DateField(null=True, blank=True)  # Placeholder for start date of work
    p_status = models.CharField(max_length=50,null=True)  # Placeholder for status
    p_endOfWork = models.DateField(null=True, blank=True)  # Placeholder for end date of work
    p_picture = models.ImageField(upload_to='profile_pictures/')
    p_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True)  # Placeholder for salary
    p_position = models.CharField(max_length=50,null=True)
    def __str__(self):
        return f'{self.p_firstname} {self.p_lastname}'
