import csv
from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):
    help = "Import products from CSV file"

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="Path to CSV file"
        )

    def handle(self, *args, **kwargs):

        csv_file = kwargs["csv_file"]

        count = 0

        with open(csv_file, mode="r", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            for row in reader:

                Product.objects.create(
                    id=int(row["id"]),
                    product_name=row["product_name"],
                    product_description=row["product_description"],
                    category=row["category"],
                    tags=row["tags"].split(",")
            )

                count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully imported {count} products."
            )
        )