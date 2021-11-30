from django.urls import path
from django.views.generic.dates import ArchiveIndexView
from .views import ClassListView, AttendanceCreationView, AttendanceDetailView
from .models import Attendance

app_name = 'attendance'
urlpatterns = [
    path('', ClassListView.as_view(), name='classes'),
    path('<str:pk>/attendance/', AttendanceCreationView.as_view(), name='attendance_creation'),
    path('archive/', ArchiveIndexView.as_view(model=Attendance, date_field="date"), name="attendance_archive"),
    path('archive/<str:pk>/', AttendanceDetailView.as_view(), name='attendance_detail')
]
