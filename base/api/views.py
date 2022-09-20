from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Company
from base.models import Team
from .serializers import CompanySerializer
from .serializers import TeamSerializer
from base.api import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import user_passes_test

@api_view(['GET', 'POST', 'HEAD', 'OPTIONS'])
def getRoutes(request):
    permission_classes = (IsAuthenticated,)
    routes = [
        'GET /api',
        'GET /api/company',
        'GET /api/company/:id',
        'GET /api/company/:id/team'
    ]
    return Response(routes)

@api_view(['GET', 'POST', 'HEAD', 'OPTIONS'])
@user_passes_test(lambda u: u.is_superuser)
def getCompany(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'HEAD', 'OPTIONS'])
def getCompanyDetails(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'HEAD', 'OPTIONS'])
def getTeamDetails(request, pk):
    team = Team.objects.get(company=pk)
    serializer = TeamSerializer(team, many=False)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'HEAD', 'OPTIONS'])
def postCompany(self, request):
    company_data = request.data
    new_company = Company.objects.create(name=company_data["name"], ceo=company_data["ceo"], address=company_data["address"], date=company_data["date"])
    new_company.save()
    serializer = CompanySerializer(new_company)
    return Response(serializer.data)

@api_view(['GET', 'POST', 'HEAD', 'OPTIONS'])
def postTeam(self, request, pk):
    team_data = request.data
    new_team = Team.objects.create(company=pk, lead=team_data["lead"])
    new_team.save()
    serializer = TeamSerializer(new_team)
    return Response(serializer.data)