from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('company/', views.getCompany),
    path('company/<str:pk>/', views.getCompanyDetails),
    path('company/<str:pk>/team', views.getTeamDetails),
    path('company/create', views.postCompany),
    path('company/<str:pk>/team/create', views.postTeam),
]