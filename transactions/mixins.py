from rest_framework.permissions import IsAuthenticated
from transactions.models import Transactions
from transactions.serializer import TransactionsSerializer


class BaseTransactionsViewMixin:
    serializer_class = TransactionsSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Transactions.objects.all()
    
