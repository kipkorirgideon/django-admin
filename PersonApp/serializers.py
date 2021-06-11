from rest_framework import serializers
from PersonApp.models import Person
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'age', "course"]
