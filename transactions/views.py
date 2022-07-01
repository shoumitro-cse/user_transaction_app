from decimal import Decimal

from django.db.models import Q
from rest_framework.response import Response
from transactions import mixins
from rest_framework import generics, status
from transactions.models import Transactions
from django.conf import settings


class TransactionsListCreateView(mixins.BaseTransactionsViewMixin,
                                 generics.ListCreateAPIView):
    """
    <div style='text-align: justify;'>
    This api is to be used to create transactions or to see all transactions.
    Only Authenticated user will be able to see it. when a user try to send this request:
    <ul>
        <li> It performs create operation after sending a post request </li>
        <li> It gives a list of transactions after sending a get request.</li>
    </ul>
    Here, the status argument value will be 1 or 2.
    <pre>
        OUTGOING = 1
        INCOMING = 2
    </pre>
    </div>
    """

    def create(self, request, *args, **kwargs):
        if self.request.user.id == request.data.get("receiver_user"):
            message = "The sender and the recipient can't be the same."
            return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST,)
        elif self.request.user.get_balance_amount < Decimal(request.data.get("amount")):
            message = "This transfer amount is too much more than the sender's balance amount."
            return Response({"error": message}, status=status.HTTP_400_BAD_REQUEST,)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(sender_user=self.request.user)

    def get_queryset(self):
        return Transactions.objects.filter(Q(sender_user=self.request.user) |
                                           Q(receiver_user=self.request.user))


class TransactionsUpdateDeleteDestroyView(mixins.BaseTransactionsViewMixin,
                                          generics.RetrieveUpdateDestroyAPIView):
    """
    <div style='text-align: justify;'>
    This API is used to get four HTTP methods functionality
    like get, put, patch, and delete for transactions crud operation.
    it is only for Authenticated users. <br/>Non-Authenticated
    users can't access it. when a user try to send this request:
    <ul>
        <li> It performs an update operation after sending a put request.</li>
        <li> It performs a partial update operation after sending a patch request.</li>
        <li> It performs a delete operation after sending a delete request.</li>
        <li> It gives the transactions details after sending a get request.</li>
    </ul>
    </div>
    """

    pass
