from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views import View
from django.urls import reverse
from . models import Attendance, Class, Student

# Create your views here.
class ClassListView(ListView):
    model = Class
    template_name = 'attendance/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classes'] = Class.objects.all()
        return context

class AttendanceCreationView(View):
    def get(self, request, pk, *args, **kwargs):
        students = Student.objects.filter(class_name=pk)

        context = {
            'students':students,
        }
        return render(request, 'attendance/attendance_creation.html', context)   

    def post(self, request, pk, *args, **kwargs):
        present = request.POST.getlist('presenties')

        class_name = Class.objects.get(id=pk)

        student_list = []
        for x in Student.objects.filter(class_name=pk):
            student_list.append(x.id)
        print(student_list)

        present_list = [int(student) for student in present]

        absent_list = list(set(student_list)-set(present_list))

        create_attendance = Attendance.objects.create(
            class_name=class_name,
        )

        is_present = create_attendance.is_present.set(present)
        is_absent = create_attendance.is_absent.set(absent_list)
        #For many-to-many relationships set() accepts a list of either model instances or field values, normally primary keys, as the objs argument.
        # or can, use : To expand that list into arguments, use * : create_attendance.present_status.add(*present)
        return HttpResponseRedirect(reverse('attendance:attendance_archive'))

        return render(request, 'attendance/attendance_creation.html')

class AttendanceDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        attendance = Attendance.objects.get(id=pk)
        context = {
            'attendance':attendance,
        }
        return render(request, 'attendance/attendance_detail.html', context)      

