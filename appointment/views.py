from .models import Appointment
from .serializers import AppointmentSerializer, ReadAppointmentSerializer, IdentifierSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView


from rest_framework import status, response

class AppointmentView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ReadAppointment(ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = ReadAppointmentSerializer


class DetailAppointmentView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = ReadAppointmentSerializer
    lookup_field = 'id'
