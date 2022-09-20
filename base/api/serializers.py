from rest_framework.serializers import ModelSerializer
from base.models import Company
from base.models import Team


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'