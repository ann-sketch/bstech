from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'product_key')
