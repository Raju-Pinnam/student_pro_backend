from django.db import models

STATE_CHOICES = (
    ('andhrapradesh', 'Andhrapradesh'),
    ('karnataka', 'Karnataka'),
    ('tamilnadu', 'Tamilnadu'),
    ('kerala', 'Kerala'),
)


class Student(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=20)
    address_line1 = models.CharField(max_length=255)
    state = models.CharField(max_length=120, choices=STATE_CHOICES)
    city =  models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        return self.name
