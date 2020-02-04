from django.db import models

STATE_CHOICES = (
    ('andhrapradesh', 'Andhrapradesh'),
    ('karnataka', 'Karnataka'),
    ('tamilnadu', 'Tamilnadu'),
    ('kerala', 'Kerala'),
)


class State(models.Model):
    state_name = models.CharField(max_length=120, choices=STATE_CHOICES)

    def __str__(self):
        return self.state_name
