#from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, CharFilter
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioFilter(FilterSet):
    dni = CharFilter(field_name='dni', lookup_expr='icontains')

    class Meta:
        model = Usuario
        fields = ['dni', 'nombre']

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = UsuarioFilter
    #filterset_field = ['dni']
    search_fields = ['nombre']

