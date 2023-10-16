from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Appointment, Identifier


class IdentifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Identifier
        fields = ['system', 'value']

    def validate(self, data):
        system = data.get('system', None)
        value = data.get('value', None)
        if Identifier.objects.filter(system=system).exists():
            data = {
                "success": False,
                "message": "This system already exists in the database "
            }
            raise ValidationError(data)
        elif Identifier.objects.filter(value=value).exists():
            data = {
                "success": False,
                "message": "This value already exists in the database"
            }
            raise ValidationError(data)

        return data


class AppointmentSerializer(serializers.ModelSerializer):
    identifier = IdentifierSerializer()

    class Meta:
        model = Appointment
        fields = ['id', 'identifier', 'patient', 'practitioner', 'organization']

    def create(self, validated_data):
        identifier_data = validated_data.pop('identifier')
        identifier = Identifier.objects.create(**identifier_data)
        appointment = Appointment.objects.create(identifier=identifier, **validated_data)
        return appointment


class ReadAppointmentSerializer(serializers.ModelSerializer):
    identifier = IdentifierSerializer()
    class Meta:
        model = Appointment
        fields = ('id', 'identifier', 'patient', 'practitioner', 'organization')



