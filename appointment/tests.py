from rest_framework.test import APITestCase

from rest_framework.reverse import reverse
from .models import Appointment, Identifier
from rest_framework import status
from rest_framework import serializers
from rest_framework.test import APITestCase
from .serializers import AppointmentSerializer
from rest_framework.exceptions import ValidationError


class CreateTestCase(APITestCase):

    def setUp(self):
        self.url = reverse('appointment')

    def test_create_app(self):
        data = {
            'id': 11,
            'identifier': {
                'system': "https://shifonur.uz/",
                'value': 1234},
            'patient': 1234567890,
            'practitioner': 1234567890,
            'organization': 1234567890
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        appoint_count = Appointment.objects.count()
        self.assertEqual(appoint_count, 1)
        appoint = Appointment.objects.get(id=11)
        self.assertEquals(appoint.patient, '1234567890')
        self.assertEquals(appoint.practitioner, '1234567890')
        self.assertEquals(appoint.organization, '1234567890')



class RegexAPITestCase(APITestCase):

    def test_valid(self):
        data = {
            'id': 11,
            'identifier': {
                          'system': "https://shifonur.uz/",
                          'value': 1234},
            'patient': 1234567890,
            'practitioner': 1234567890,
            'organization': 1234567890
        }

        response = self.client.post(reverse('appointment'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        appoint = Appointment.objects.get(id=11)

        self.assertRegex(appoint.patient, r'^[1-9][0-9]{9}$')
        self.assertRegex(appoint.practitioner, r'^[1-9][0-9]{9}$')
        self.assertRegex(appoint.organization, r'^[1-9][0-9]{9}$')



    def test_invalid(self):
        data = {
            'id': 11,
            'identifier': {
                'system': "https://shifonur.uz/",
                'value': 1234},
            'patient': 123456,
            'practitioner': 1234567,
            'organization': 1234567890
        }

        response = self.client.post(reverse('appointment'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class RequiredAPITestCase(APITestCase):
    def test_invalid_appointment(self):
        data = {
            'id': 11,
            'identifier': {
                'system': "https://shifonur.uz/",
                'value': 1234},
        }

        response = self.client.post(reverse('appointment'), data=data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_400_BAD_REQUEST)

        # Check if the 'patient' field is required
        errors = response.data
        self.assertIn('patient', errors)
        self.assertIn('practitioner', errors)
        self.assertIn('organization', errors)

class InvalidMessageAPITestCase(APITestCase):
    def test_duplicate_identifier_system(self):
        existing_identifier = Identifier.objects.create(system="https://shifonur.uz/", value="12345")
        existing_appointment = Appointment.objects.create(
            id=1,
            identifier=existing_identifier,
            patient="1234567890",
            practitioner="1234567890",
            organization="1234567890"
        )

        serializer_data = {
            'id': 11,
            'identifier': {
                          'system': "https://shifonur.uz/",
                          'value': 1234},
            'patient': 1234567890,
            'practitioner': 1234567890,
            'organization': 1234567890
        }

        serializer = AppointmentSerializer(data=serializer_data)

        with self.assertRaisesMessage(ValidationError, "This system already exists in the database"):
            serializer.is_valid(raise_exception=True)


    def test_duplicate_identifier_value(self):
        existing_identifier = Identifier.objects.create(system="https://shifonur.uz/", value="12345")
        existing_appointment = Appointment.objects.create(
            id=1,
            identifier=existing_identifier,
            patient="1234567890",
            practitioner="1234567890",
            organization="1234567890"
        )

        serializer_data = {
            'id': 11,
            'identifier': {
                'system': "https://shifonurr.uz/",
                'value': 12345},
            'patient': 1234567890,
            'practitioner': 1234567890,
            'organization': 1234567890
        }

        serializer = AppointmentSerializer(data=serializer_data)

        with self.assertRaisesMessage(ValidationError, "This value already exists in the database"):
            serializer.is_valid(raise_exception=True)