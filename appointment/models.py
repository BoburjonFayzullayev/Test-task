from django.core.validators import RegexValidator
from django.db import models


class Identifier(models.Model):
    system = models.URLField(max_length=100)
    value = models.CharField(max_length=20,
                             validators=[RegexValidator(r'^[1-9][0-9]*$')])

    def __str__(self):
        return self.system





class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    identifier = models.ForeignKey(Identifier, on_delete=models.CASCADE)
    patient = models.CharField(max_length=10, validators=[RegexValidator(r'^[1-9][0-9]{9}$')])
    practitioner = models.CharField(max_length=10, validators=[RegexValidator(r'^[1-9][0-9]{9}$')])
    organization = models.CharField(max_length=10, validators=[RegexValidator(r'^[1-9][0-9]{9}$')])

    def __str__(self):
        return str(self.id)
