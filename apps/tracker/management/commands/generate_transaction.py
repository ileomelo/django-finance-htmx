import random
from unittest.mock import Base
from faker import Faker
from django.core.management.base import BaseCommand

from apps.tracker.models import Category, Transaction, User



class Command(BaseCommand):
  help = "Generates transactions for testing"

  def handle(self, *args, **options):
    fake = Faker()

    # creating a category
    categories = [
      "Bills",
      "Clothes",
      "Medical",
      "Food",
      "Housing",
      "Salary",
      "Social",
      "Transport",
      "Vacation",
    ]

    # Create a category in database for categories
    for category in categories:
      Category.objects.get_or_create(name=category)

    # get User
    user = User.objects.filter(username="admin").first()
    if not user:
      user = User.objects.create_superuser(username="admin", password="test")

    # creating a 20 transactions per type [income, expense]
    categories = Category.objects.all()
    types = [x[0] for x in Transaction.TRANSACTION_TYPE]
    for i in range(20):
      Transaction.objects.create(
        category=random.choice(categories),
        user=user,
        amount=random.uniform(1, 2500),
        date=fake.date_between(start_date="-1y", end_date="today"),
        types=random.choice(types),
      )
