from django.db import models

class Coordinate(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)  # Optional name for the location
    latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Latitude with precision
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Longitude with precision
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the coordinate is added
    disaster_type = models.CharField(max_length=100)  # Type of disaster (e.g., flood, earthquake, etc.)
    description = models.TextField(blank=True, null=True)  # Detailed description of the disaster
    number_of_volunteers = models.IntegerField(default=0)  # Number of volunteers available or assigned

    def __str__(self):
        return self.name if self.name else f"Lat: {self.latitude}, Lng: {self.longitude}"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)