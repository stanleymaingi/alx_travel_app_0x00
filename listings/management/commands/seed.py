from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings, bookings, and reviews"

    def handle(self, *args, **kwargs):
        # Create a host user if none exists
        if not User.objects.filter(username="host1").exists():
            host = User.objects.create_user(username="host1", password="password123")
        else:
            host = User.objects.get(username="host1")

        # Create some guest users
        guests = []
        for i in range(1, 6):
            username = f"guest{i}"
            if not User.objects.filter(username=username).exists():
                guest = User.objects.create_user(username=username, password="password123")
            else:
                guest = User.objects.get(username=username)
            guests.append(guest)

        # Seed 10 Listings
        listings = []
        for i in range(1, 11):
            listing = Listing.objects.create(
                title=f"Sample Listing {i}",
                description="This is a sample listing.",
                price=random.randint(50, 500),
                location=f"City {i}",
                host=host
            )
            listings.append(listing)

        # Seed Bookings
        for listing in listings:
            for guest in random.sample(guests, k=2):  # each listing has 2 bookings
                start = date.today() + timedelta(days=random.randint(1, 30))
                end = start + timedelta(days=random.randint(1, 7))
                Booking.objects.create(
                    listing=listing,
                    guest=guest,
                    start_date=start,
                    end_date=end,
                    total_price=listing.price * (end - start).days
                )

        # Seed Reviews
        for listing in listings:
            for guest in random.sample(guests, k=2):  # 2 reviews per listing
                Review.objects.create(
                    listing=listing,
                    user=guest,
                    rating=random.randint(1, 5),
                    comment="This is a sample review."
                )

        self.stdout.write(self.style.SUCCESS("Successfully seeded listings, bookings, and reviews"))
