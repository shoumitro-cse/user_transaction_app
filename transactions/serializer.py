from transactions.models import Transactions
from rest_framework import serializers


class TransactionsSerializer(serializers.ModelSerializer):
    scheduled_date_time = serializers.DateTimeField(required=False)

    class Meta:
        model = Transactions
        exclude = ('sender_user', 'created_at', 'created_by', 'updated_at', 'updated_by', )

    def create(self, validated_data):
        del validated_data["scheduled_date_time"]
        return super().create(validated_data)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({"status": str(instance.get_status_display()).capitalize()})
        return data
