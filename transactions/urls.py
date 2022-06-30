from django.urls import path
from transactions.views import ( 
    TransactionsListCreateView,
    TransactionsUpdateDeleteDestroyView
)

urlpatterns = [
    #  This URL is used for transactions create or to see transactions lists
    path('transaction/', TransactionsListCreateView.as_view(), name='transaction_create_list'),
    # This URL is used for transactions retrieve, partially or fully update and delete
    path('transaction/<int:pk>/', TransactionsUpdateDeleteDestroyView.as_view(),
         name='transaction_retrieve_update_delete'),
]