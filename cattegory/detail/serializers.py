from rest_framework import serializers

from detail.models import Cattegory


class CattegorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cattegory
        fields = ('species', 'price', 'food', 'buy_place')

    # species = serializers.CharField(read_only=True)
    # species = serializers.CharField(required=False)
    # price = serializers.IntegerField(required=False)
    # food = serializers.CharField(required=False)
    # buy_place = serializers.CharField(required=False)
