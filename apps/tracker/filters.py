from django import forms
import django_filters

from apps.tracker.models import Category, Transaction


class TransactionFilter(django_filters.FilterSet):
  transaction_type = django_filters.ChoiceFilter(
    choices=Transaction.TRANSACTION_TYPE,
    field_name="types",
    lookup_expr="iexact",
    empty_label="All",
  )

  start_date = django_filters.DateFilter(
    field_name="date",
    lookup_expr="gte",
    label="Date From",
    widget=forms.DateInput(attrs={"type": "date"}),
  )

  end_date = django_filters.DateFilter(
    field_name="date",
    lookup_expr="lte",
    label="Date To",
    widget=forms.DateInput(attrs={"type": "date"}),
  )

  category = django_filters.ModelMultipleChoiceFilter(
    queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple()
  )

  class Meta:
    model = Transaction
    fields = ("transaction_type", "start_date", "end_date", "category")
