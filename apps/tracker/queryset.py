from django.db import models


class TransactionQuerySet(models.QuerySet):
  def get_expenses(self):
    return self.filter(types="expense")

  def get_income(self):
    return self.filter(types="income")

  def get_total_expenses(self):
    return self.get_expenses().aggregate(total=models.Sum("amount"))["total"] or 0

  def get_total_income(self):
    return self.get_income().aggregate(total=models.Sum("amount"))["total"] or 0

  def get_net_value(self):
    income = self.get_total_income()
    expenses = self.get_total_expenses()
    return income - expenses
