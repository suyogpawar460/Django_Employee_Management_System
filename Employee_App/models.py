from django.db import models


class Employee(models.Model):
    ename = models.CharField(max_length=30)
    salary = models.FloatField()  # 10000.00
    city = models.CharField(max_length=30)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.ename
