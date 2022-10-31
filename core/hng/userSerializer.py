from rest_framework.serializers import ModelSerializer



from .models import HngUserModel


class HngUserSerializer(ModelSerializer):

    class Meta:
        model = HngUserModel
        fields = [
            "first_name",
            "last_name",
            "email",
            "stack",
            "date_joined",
        ]


