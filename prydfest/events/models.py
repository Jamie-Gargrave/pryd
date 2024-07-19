from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)
    event_date = models.DateTimeField()
    venue_name = models.CharField(max_length=200)
    venue_address = models.CharField(max_length=300)
    entry_fee = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.name
