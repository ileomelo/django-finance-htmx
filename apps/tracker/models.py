from django.db import models
from django.contrib.auth.models import AbstractUser
from .queryset import TransactionQuerySet


class User(AbstractUser):
  pass


class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)

  class Meta:
    verbose_name_plural = "Categories"

  def __str__(self) -> str:
    return self.name


class Transaction(models.Model):
  TRANSACTION_TYPE = (
    ("income", "Income"),
    ("expense", "Expense"),
  )
  types = models.CharField(max_length=7, choices=TRANSACTION_TYPE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  amount = models.DecimalField(max_digits=10, decimal_places=2)
  date = models.DateField()

  objects = TransactionQuerySet.as_manager()

  def __str__(self) -> str:
    return f"{self.types} of {self.amount} on {self.date} by {self.user}"

  class Meta:
    ordering = ["-date"]
