from django.urls import path
from .views import AppointmentView, ReadAppointment, DetailAppointmentView

urlpatterns = [
    path('api/', AppointmentView.as_view(), name="appointment"),
    path('list/', ReadAppointment.as_view(), name='list'),
    path('api/<int:id>/', DetailAppointmentView.as_view(), name='detail')

]
