from django.shortcuts import render

# Create your views here.

from .models import College, School, Department, Course, Exam, MC_Question, MA_Question, TF_Question, ORD_Question, ESS_Question, MAT_Question, NUM_Question, SR_Question, FIB_PLUS_Question
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin


def index(request):
    colleges = College.objects.filter()
    return render(request,'index.html')

def school(request):
    schools = School.objects.filter()
    return render(request,'index.html',{'schools': schools})

class CollegeListView(generic.ListView):
    """
    Generic class-based list view for a list of authors.
    """
    model = College
    paginate_by = 10 

class SchoolListView(generic.ListView):
    model = School
    paginate_by = 10

class SchoolDetailView(generic.DetailView):
    model = School

class CollegeDetailView(generic.DetailView):
	model = College

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class CollegeCreate(PermissionRequiredMixin, CreateView):
    model = College
    fields = '__all__'
    initial={'name':'College',}
    permission_required = 'catalog.can_mark_returned'

class CollegeUpdate(PermissionRequiredMixin, UpdateView):
    model = College
    fields = ['name']
    permission_required = 'catalog.can_mark_returned'

class CollegeDelete(PermissionRequiredMixin, DeleteView):
    model = College
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class SchoolCreate(PermissionRequiredMixin, CreateView):
    model = School
    fields = '__all__'
    initial={'name':'School',}
    permission_required = 'catalog.can_mark_returned'

class SchoolUpdate(PermissionRequiredMixin, UpdateView):
    model = School
    fields = ['name']
    permission_required = 'catalog.can_mark_returned'

class SchoolDelete(PermissionRequiredMixin, DeleteView):
    model = School
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class DepartmentCreate(PermissionRequiredMixin, CreateView):
    model = Department
    fields = '__all__'
    initial={'name':'Department',}
    permission_required = 'catalog.can_mark_returned'

class DepartmentUpdate(PermissionRequiredMixin, UpdateView):
    model = Department
    fields = ['name']
    permission_required = 'catalog.can_mark_returned'

class DepartmentDelete(PermissionRequiredMixin, DeleteView):
    model = Department
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class DepartmentDetailView(generic.DetailView):
    model = Department

class CourseCreate(PermissionRequiredMixin, CreateView):
    model = Course
    fields = '__all__'
    initial={'name':'Course', 'courseID':'CSCI-360'}
    permission_required = 'catalog.can_mark_returned'

class CourseUpdate(PermissionRequiredMixin, UpdateView):
    model = Course
    fields = ['name', 'CourseID']
    permission_required = 'catalog.can_mark_returned'

class CourseDelete(PermissionRequiredMixin, DeleteView):
    model = Course
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class CourseDetailView(generic.DetailView):
    model = Course

class ExamCreate(PermissionRequiredMixin, CreateView):
    model = Exam
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ExamUpdate(PermissionRequiredMixin, UpdateView):
    model = Exam
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class ExamDelete(PermissionRequiredMixin, DeleteView):
    model = Exam
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'

class ExamDetailView(generic.DetailView):
    model = Exam

#--------------------------------------------------------#

class MCQDetailView(generic.DetailView):
    model = MC_Question

class MAQDetailView(generic.DetailView):
    model = MA_Question

class TFQDetailView(generic.DetailView):
    model = TF_Question

class ESSQDetailView(generic.DetailView):
    model = ESS_Question

class ORDQDetailView(generic.DetailView):
    model = ORD_Question

class MATQDetailView(generic.DetailView):
    model = MAT_Question

class NUMQDetailView(generic.DetailView):
    model = NUM_Question

class SRQDetailView(generic.DetailView):
    model = SR_Question

class FIBQDetailView(generic.DetailView):
    model = FIB_PLUS_Question

#--------------------------------------------------------#

class MCQListView(generic.ListView):
    model = MC_Question

class MAQListView(generic.ListView):
    model = MA_Question

class TFQDListlView(generic.ListView):
    model = TF_Question

class ESSQListlView(generic.ListView):
    model = ESS_Question

class ORDQListlView(generic.ListView):
    model = ORD_Question

class MATQListView(generic.ListView):
    model = MAT_Question

class NUMQListlView(generic.ListView):
    model = NUM_Question

class SRQListView(generic.ListView):
    model = SR_Question

class FIBQListView(generic.ListView):
    model = FIB_PLUS_Question

#--------------------------------------------------------#

class MCQCreate(PermissionRequiredMixin, CreateView):
    model = MC_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class MCQUpdate(PermissionRequiredMixin, UpdateView):
    model = MC_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class MCQDelete(PermissionRequiredMixin, DeleteView):
    model = MC_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
#--------------------------------------------------------#

class MAQCreate(PermissionRequiredMixin, CreateView):
    model = MA_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class MAQUpdate(PermissionRequiredMixin, UpdateView):
    model = MA_Question
    fields = ['name', 'ExamDate', 'InstrucorName', 'InstructorsEmail', 'semester', 'Year']
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class MAQDelete(PermissionRequiredMixin, DeleteView):
    model = MA_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

#--------------------------------------------------------#

class TFQCreate(PermissionRequiredMixin, CreateView):
    model = TF_Question
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class TFQUpdate(PermissionRequiredMixin, UpdateView):
    model = TF_Question
    fields = ['name', 'ExamDate', 'InstrucorName', 'InstructorsEmail', 'semester', 'Year']
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class TFQDelete(PermissionRequiredMixin, DeleteView):
    model = TF_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

#--------------------------------------------------------#

class ESSQCreate(PermissionRequiredMixin, CreateView):
    model = ESS_Question
    fields = '__all__'
    initial={'name': 'Midterm'}
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class ESSQUpdate(PermissionRequiredMixin, UpdateView):
    model = ESS_Question
    fields = ['name', 'ExamDate', 'InstrucorName', 'InstructorsEmail', 'semester', 'Year']
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class ESSQDelete(PermissionRequiredMixin, DeleteView):
    model = ESS_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

#--------------------------------------------------------#

class ORDQCreate(PermissionRequiredMixin, CreateView):
    model = ORD_Question
    fields = '__all__'
    initial={'name': 'Midterm'}
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class ORDQUpdate(PermissionRequiredMixin, UpdateView):
    model = ORD_Question
    fields = ['name', 'ExamDate', 'InstrucorName', 'InstructorsEmail', 'semester', 'Year']
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class ORDQDelete(PermissionRequiredMixin, DeleteView):
    model = ORD_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

#--------------------------------------------------------#

class MATQCreate(PermissionRequiredMixin, CreateView):
    model = MAT_Question
    fields = '__all__'
    initial={'name': 'Midterm'}
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class MATQUpdate(PermissionRequiredMixin, UpdateView):
    model = MAT_Question
    fields = ['name', 'ExamDate', 'InstrucorName', 'InstructorsEmail', 'semester', 'Year']
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class MATQDelete(PermissionRequiredMixin, DeleteView):
    model = MAT_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

#--------------------------------------------------------#

class NUMQCreate(PermissionRequiredMixin, CreateView):
    model = NUM_Question
    fields = '__all__'
    initial={'name': 'Midterm'}
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class NUMQUpdate(PermissionRequiredMixin, UpdateView):
    model = NUM_Question
    fields = ['name', 'ExamDate', 'InstrucorName', 'InstructorsEmail', 'semester', 'Year']
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class NUMQDelete(PermissionRequiredMixin, DeleteView):
    model = NUM_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

#--------------------------------------------------------#

class SRQCreate(PermissionRequiredMixin, CreateView):
    model = SR_Question
    fields = '__all__'
    initial={'name': 'Midterm'}
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class SRQUpdate(PermissionRequiredMixin, UpdateView):
    model = SR_Question
    fields = ['name', 'ExamDate', 'InstrucorName', 'InstructorsEmail', 'semester', 'Year']
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class SRQDelete(PermissionRequiredMixin, DeleteView):
    model = SR_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

#--------------------------------------------------------#

class FIBCreate(PermissionRequiredMixin, CreateView):
    model = FIB_PLUS_Question
    fields = '__all__'
    initial={'name': 'Midterm'}
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class FIBUpdate(PermissionRequiredMixin, UpdateView):
    model = FIB_PLUS_Question
    fields = ['name', 'ExamDate', 'InstrucorName', 'InstructorsEmail', 'semester', 'Year']
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

class FIBDelete(PermissionRequiredMixin, DeleteView):
    model = FIB_PLUS_Question
    success_url = reverse_lazy('college')
    permission_required = 'catalog.can_mark_returned'
    success_url = reverse_lazy('college')

#--------------------------------------------------------#