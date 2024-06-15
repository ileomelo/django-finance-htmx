import pytest
from apps.tracker.models import Transaction


@pytest.mark.django_db
def test_queryset_get_income_method(transactions):
  qs = Transaction.objects.get_income()

  assert qs.count() > 0
  assert all([transactions.types == "income" for transactions in qs])


@pytest.mark.django_db
def test_queryset_get_expenses_method(transactions):
  qs = Transaction.objects.get_expenses()

  assert qs.count() > 0
  assert all([transactions.types == "expense" for transactions in qs])


@pytest.mark.django_db
def test_queryset_get_total_income_method(transactions):
  total_income = Transaction.objects.get_total_income()

  assert total_income == sum(t.amount for t in transactions if t.types == "income")


@pytest.mark.django_db
def test_queryset_get_total_expenses_method(transactions):
  total_expense = Transaction.objects.get_total_expenses()

  assert total_expense == sum(t.amount for t in transactions if t.types == "expense")
