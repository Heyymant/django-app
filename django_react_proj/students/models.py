from django.db import models

class Student(models.Model):
    name = models.CharField("Name", max_length=240)
    title = models.CharField(default = '',max_length=20)
    document = models.CharField("Document", max_length=20)
    image = models.CharField(max_length=20)
    registrationDate = models.DateField("Registration Date", auto_now_add=True)

    def __str__(self):
        return self.name