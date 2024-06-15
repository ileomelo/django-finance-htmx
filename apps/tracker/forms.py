from django import forms
from apps.tracker.models import Transaction, Category


class TransactionForm(forms.ModelForm):
  category = forms.ModelChoiceField(
    queryset=Category.objects.all(), widget=forms.RadioSelect()
  )

  class Meta:
    model = Transaction
    fields = ("types", "amount", "date", "category")
    widgets = {"date": forms.DateInput(attrs={"type": "date"})}
