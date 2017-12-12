from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^colleges/$', views.CollegeListView.as_view(), name='college'),  
    url(r'^college/(?P<pk>\d+)$', views.CollegeDetailView.as_view(), name='college-detail'),

    #Creating, deleting and updating Colleges
	url(r'^colleges/create/$', views.CollegeCreate.as_view(), name='college_create'),
    url(r'^college/(?P<pk>\d+)/update/$', views.CollegeUpdate.as_view(), name='college_update'),
    url(r'^college/(?P<pk>\d+)/delete/$', views.CollegeDelete.as_view(), name='college_delete'),

    url(r'^school/(?P<pk>\d+)$', views.SchoolDetailView.as_view(), name='school-detail'),
    url(r'^department/(?P<pk>\d+)$', views.DepartmentDetailView.as_view(), name='department-detail'),
    url(r'course/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course-detail'),
    url(r'exam/(?P<pk>\d+)$', views.ExamDetailView.as_view(), name='exam-detail'),

    url(r'college/school/department/course/exam/MCQ/(?P<pk>\d+)$', views.MCQDetailView.as_view(), name='MCQ-detail'),
    url(r'college/school/department/course/exam/MAQ/(?P<pk>\d+)$', views.MAQDetailView.as_view(), name='MAQ-detail'),
    url(r'college/school/department/course/exam/TFQ/(?P<pk>\d+)$', views.TFQDetailView.as_view(), name='TFQ-detail'),
    url(r'college/school/department/course/exam/ESSQ/(?P<pk>\d+)$', views.ESSQDetailView.as_view(), name='ESSQ-detail'),
    url(r'college/school/department/course/exam/ORDQ/(?P<pk>\d+)$', views.ORDQDetailView.as_view(), name='ORDQ-detail'),
    url(r'college/school/department/course/exam/MATQ/(?P<pk>\d+)$', views.MATQDetailView.as_view(), name='MATQ-detail'),
    url(r'college/school/department/course/exam/NUMQ/(?P<pk>\d+)$', views.NUMQDetailView.as_view(), name='NUMQ-detail'),
    url(r'college/school/department/course/exam/SRQ/(?P<pk>\d+)$', views.SRQDetailView.as_view(), name='SRQ-detail'),
    url(r'college/school/department/course/exam/FIBQ/(?P<pk>\d+)$', views.FIBQDetailView.as_view(), name='FIBQ-detail'),
    url(r'college/school/department/course/exam/FIB-PLUS-Q/(?P<pk>\d+)$', views.FIBPLUSQDetailView.as_view(), name='FIB-PLUS-Q-detail'),

    url(r'college/school/department/course/exam/MCQ/$', views.MCQListView.as_view(), name='MCQ-list'),
    url(r'college/school/department/course/exam/MAQ/$', views.MAQListView.as_view(), name='MAQ-list'),
    url(r'college/school/department/course/exam/TFQ/$', views.TFQListlView.as_view(), name='TFQ-list'),
    url(r'college/school/department/course/exam/ESSQ/$', views.ESSQListlView.as_view(), name='ESSQ-list'),
    url(r'college/school/department/course/exam/ORDQ/$', views.ORDQListlView.as_view(), name='ORDQ-list'),
    url(r'college/school/department/course/exam/MATQ/$', views.MATQListView.as_view(), name='MATQ-list'),
    url(r'college/school/department/course/exam/NUMQ/$', views.NUMQListlView.as_view(), name='NUMQ-list'),
    url(r'college/school/department/course/exam/SRQ/$', views.SRQListView.as_view(), name='SRQ-list'),
    url(r'college/school/department/course/exam/FIBQ/$', views.FIBQListView.as_view(), name='FIBQ-list'),
    url(r'college/school/department/course/exam/FIB-PLUS-Q/$', views.FIBPLUSQListView.as_view(), name='FIB-PLUS-Q-list'),

    #Creating, deleting and updating Schools
	url(r'^college/school/create$', views.SchoolCreate.as_view(), name='school_create'),
    url(r'^college/school/(?P<pk>\d+)/update/$', views.SchoolUpdate.as_view(), name='school_update'),
    url(r'^college/school/(?P<pk>\d+)/delete/$', views.SchoolDelete.as_view(), name='school_delete'),

    #Creating, deleting and updating Departments
    url(r'^college/school/department/create$', views.DepartmentCreate.as_view(), name='department_create'),
    url(r'^college/school/department/(?P<pk>\d+)/update/$', views.DepartmentUpdate.as_view(), name='department_update'),
    url(r'^college/school/department/(?P<pk>\d+)/delete/$', views.DepartmentDelete.as_view(), name='department_delete'),

    #Creating, deleting and updating Course
    url(r'^college/school/department/course/create$', views.CourseCreate.as_view(), name='course_create'),
    url(r'^college/school/department/course/(?P<pk>\d+)/update/$', views.CourseUpdate.as_view(), name='course_update'),
    url(r'^college/school/department/course/(?P<pk>\d+)/delete/$', views.CourseDelete.as_view(), name='course_delete'),

    #Creating, deleting and updating Exam
    url(r'^college/school/department/course/exam/create$', views.ExamCreate.as_view(), name='exam_create'),
    url(r'^college/school/department/course/exam/(?P<pk>\d+)/update/$', views.ExamUpdate.as_view(), name='exam_update'),
    url(r'^college/school/department/course/exam/(?P<pk>\d+)/delete/$', views.ExamDelete.as_view(), name='exam_delete'),

    #Creating, deleting and updating MC Questions
    url(r'^college/school/department/course/exam/MCQ/create$', views.MCQCreate.as_view(), name='MC_create'),
    url(r'^college/school/department/course/exam/MCQ/(?P<pk>\d+)/update/$', views.MCQUpdate.as_view(), name='MC_update'),
    url(r'^college/school/department/course/exam/MCQ/(?P<pk>\d+)/delete/$', views.MCQDelete.as_view(), name='MC_delete'),

    #Creating, deleting and updating MA Questions
    url(r'^college/school/department/course/exam/MAQ/create$', views.MAQCreate.as_view(), name='MA_create'),
    url(r'^college/school/department/course/exam/MAQ/(?P<pk>\d+)/update/$', views.MAQUpdate.as_view(), name='MA_update'),
    url(r'^college/school/department/course/exam/MAQ/(?P<pk>\d+)/delete/$', views.MAQDelete.as_view(), name='MA_delete'),

    #Creating, deleting and updating TF Questions
    url(r'^college/school/department/course/exam/TFQ/create$', views.TFQCreate.as_view(), name='TF_create'),
    url(r'^college/school/department/course/exam/TFQ/(?P<pk>\d+)/update/$', views.TFQUpdate.as_view(), name='TF_update'),
    url(r'^college/school/department/course/exam/TFQ/(?P<pk>\d+)/delete/$', views.TFQDelete.as_view(), name='TF_delete'),

    #Creating, deleting and updating ESS Questions
    url(r'^college/school/department/course/exam/ESSQ/create$', views.ESSQCreate.as_view(), name='ESS_create'),
    url(r'^college/school/department/course/exam/ESSQ/(?P<pk>\d+)/update/$', views.ESSQUpdate.as_view(), name='ESS_update'),
    url(r'^college/school/department/course/exam/ESSQ/(?P<pk>\d+)/delete/$', views.ESSQDelete.as_view(), name='ESS_delete'),

    #Creating, deleting and updating ORD Questions
    url(r'^college/school/department/course/exam/ORDQ/create$', views.ORDQCreate.as_view(), name='ORD_create'),
    url(r'^college/school/department/course/exam/ORDQ/(?P<pk>\d+)/update/$', views.ORDQUpdate.as_view(), name='ORD_update'),
    url(r'^college/school/department/course/exam/ORDQ/(?P<pk>\d+)/delete/$', views.ORDQDelete.as_view(), name='ORD_delete'),

    #Creating, deleting and updating MAT Questions
    url(r'^college/school/department/course/exam/MATQ/create$', views.MATQCreate.as_view(), name='MAT_create'),
    url(r'^college/school/department/course/exam/MATQ/(?P<pk>\d+)/update/$', views.MATQUpdate.as_view(), name='MAT_update'),
    url(r'^college/school/department/course/exam/MATQ/(?P<pk>\d+)/delete/$', views.MATQDelete.as_view(), name='MAT_delete'),

    #Creating, deleting and updating NUM Questions
    url(r'^college/school/department/course/exam/NUMQ/create$', views.NUMQCreate.as_view(), name='NUM_create'),
    url(r'^college/school/department/course/exam/NUMQ/(?P<pk>\d+)/update/$', views.NUMQUpdate.as_view(), name='NUM_update'),
    url(r'^college/school/department/course/exam/NUMQ/(?P<pk>\d+)/delete/$', views.NUMQDelete.as_view(), name='NUM_delete'),

    #Creating, deleting and updating SR Questions
    url(r'^college/school/department/course/exam/SRQ/create$', views.SRQCreate.as_view(), name='SR_create'),
    url(r'^college/school/department/course/exam/SRQ/(?P<pk>\d+)/update/$', views.SRQUpdate.as_view(), name='SR_update'),
    url(r'^college/school/department/course/exam/SRQ/(?P<pk>\d+)/delete/$', views.SRQDelete.as_view(), name='SR_delete'),

    #Creating, deleting and updating FIB Questions
    url(r'^college/school/department/course/exam/FIBQ/create$', views.FIBCreate.as_view(), name='FIB_create'),
    url(r'^college/school/department/course/exam/FIBQ/(?P<pk>\d+)/update/$', views.FIBUpdate.as_view(), name='FIB_update'),
    url(r'^college/school/department/course/exam/FIBQ/(?P<pk>\d+)/delete/$', views.FIBDelete.as_view(), name='FIB_delete'),

    #Creating, deleting and updating FIB_PLUS Questions
    url(r'^college/school/department/course/exam/FIB-PLUS-Q/create$', views.FIB_PLUS_Create.as_view(), name='FIB_PLUS_create'),
    url(r'^college/school/department/course/exam/FIB-PLUS-Q/(?P<pk>\d+)/update/$', views.FIB_PLUS_Update.as_view(), name='FIB_PLUS_update'),
    url(r'^college/school/department/course/exam/FIB-PLUS-Q/(?P<pk>\d+)/delete/$', views.FIB_PLUS_Delete.as_view(), name='FIB_PLUS_delete'),
]