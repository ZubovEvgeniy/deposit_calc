from rest_framework import serializers


class DepositSerializer(serializers.Serializer):

    date = serializers.DateField(format="%d.%m.%Y", input_formats=["%d.%m.%Y"])
    periods = serializers.IntegerField(min_value=1, max_value=60)
    amount = serializers.IntegerField(min_value=10_000, max_value=3_000_000)
    rate = serializers.FloatField(min_value=1, max_value=8)
