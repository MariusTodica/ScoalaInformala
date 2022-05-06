from django.db import models

from first_app.models import Location


class Companies(models.Model):
    company_choices = (('SRL', 'S.R.L.'),
                       ('SA', 'S.A.'))

    name = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    company_type = models.CharField(max_length=5, choices=company_choices)
    active = models.BooleanField(default=1)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company_type} {self.name}"
