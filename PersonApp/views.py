from django.shortcuts import render
from rest_framework import viewsets
from PersonApp.models import Person
from PersonApp.serializers import PersonSerializer
# Create your views here.
class PersonViewSets(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


