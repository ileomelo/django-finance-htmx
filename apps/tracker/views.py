from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from apps.tracker.forms import TransactionForm
from apps.tracker.models import Transaction
from apps.tracker.filters import TransactionFilter


# Create your views here.
def index(request):
  return render(request, "tracker/index.html")


@login_required
def transactions_list(request):
  transactions_filter = TransactionFilter(
    request.GET,
    queryset=Transaction.objects.filter(user=request.user).select_related("category"),
  )
  total_expenses = transactions_filter.qs.get_total_expenses()
  total_income = transactions_filter.qs.get_total_income()
  net_total = transactions_filter.qs.get_net_value()

  context = {
    "filter": transactions_filter,
    "total_expenses": total_expenses,
    "total_income": total_income,
    "net_income": net_total,
  }

  if request.htmx:
    return render(request, "tracker/partials/transactions-container.html", context)

  return render(request, "tracker/transactions-list.html", context)


@login_required
def create_transaction(request):
  if request.method == "POST":
    form = TransactionForm(request.POST)
    if form.is_valid():
      transaction = form.save(commit=False)
      transaction.user = request.user
      transaction.save()
      return redirect(reverse('transaction-list'))
  context = {'form': TransactionForm()}
  return render(request, "tracker/partials/create-transaction.html", context)
