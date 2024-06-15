from django.urls import path

from apps.tracker import views

urlpatterns = [
  path("", views.index, name="index"),
  path("transactions/", views.transactions_list, name="transaction-list"),
  path("transaction/create/", views.create_transaction, name="create-transaction"),
]
