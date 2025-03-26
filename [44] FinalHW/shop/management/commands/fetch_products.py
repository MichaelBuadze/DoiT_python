from django.core.management.base import BaseCommand
from shop.models import Product
from shop.utils import fetch_products

class Command(BaseCommand):
    help = "Fetch products from API and save to database"

    def handle(self, *args, **kwargs):
        products = fetch_products()
        for item in products:
            Product.objects.update_or_create(
                name=item["name"],
                defaults={
                    "image_url": item["image"],
                    "price": item["price"],
                    "brand": item["brand"],
                    "category": item["category"],
                    "stock": item["stock"],
                    "release_date": item["release_date"],
                    "rating": item["rating"],
                },
            )
        self.stdout.write(self.style.SUCCESS("Products successfully updated!"))
