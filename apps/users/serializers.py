from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            "pk",
            "user",
            "name"
        ]
        read_only_fields = ["user"]

    def validate_name(self, value):
        qs = User.objects.filter(name__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The name must be unique")
        return value
