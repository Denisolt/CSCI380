from django.contrib import admin

# Register your models here.

from .models import School, College, Department, Course, Exam, MC_Question, MA_Question, TF_Question, ESS_Question, MAT_Question, NUM_Question, SR_Question, FIB_PLUS_Question

"""
# Minimal registration of Models.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
"""
admin.site.register(College)
admin.site.register(School)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Exam)

admin.site.register(MC_Question)
admin.site.register(MA_Question)
admin.site.register(TF_Question)
admin.site.register(ESS_Question)
admin.site.register(MAT_Question)
admin.site.register(NUM_Question)
admin.site.register(SR_Question)
admin.site.register(FIB_PLUS_Question)