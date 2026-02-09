from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    host = models.ForeignKey(User, related_name="listings", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, related_name="bookings", on_delete=models.CASCADE)
    guest = models.ForeignKey(User, related_name="bookings", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.guest.username} - {self.listing.title}"

class Review(models.Model):
    listing = models.ForeignKey(Listing, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}"
