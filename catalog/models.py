from django.db import models


from django.urls import reverse #Used to generate urls by reversing the URL patterns


class College(models.Model):
    """
    Model representing a College (e.g. NYIT, PACE).
    """
    name = models.CharField(max_length=200, help_text="Enter the College (e.g. NYIT, PACE, etc)")
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('college-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=200, help_text="Enter School's name (e.g. School of Engineering)")
    college = models.ForeignKey('College', on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('school-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the Department's name (e.g. Computer Science")
    SchoolName = models.ForeignKey(School, help_text="Select a School for this Department")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('department-detail', args=[str(self.id)])

class Course(models.Model):
    CourseID = models.CharField(max_length=200, help_text="Enter the CourseID (e.g. CSCI 360)")
    name = models.CharField(max_length=200, help_text="Enter the CourseID (e.g. Artificial Intelligence)")
    DepartmentName = models.ForeignKey(Department)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('course-detail', args=[str(self.id)])

class MC_Question(models.Model):
    question = models.TextField()
    title = 'MC'

    def __str__(self):
        return self.title

# class MC_Answers(Models.Model):
#     answer = models.CharField(max_length=200)
#     question = models.ManyToManyField(MC_Question)

#     def __str__(self):
#         return self.answer

class MA_Question(models.Model):
    question = models.TextField()
    title = 'MA'
    def __str__(self):
        return self.title

# class MA_Answers(Models.Model):
#     answer = models.CharField(max_length=200)
#     MA_Question_Option = (
#         ('c', 'correct'),
#         ('i', 'inccorect'),
#     )
#     CorrectOrNot= models.CharField(max_length=1, choices=MA_Question_Option, blank=True, default='f', help_text='Semester')

#     question = models.ManyToManyField(MA_Question)

#     def __str__(self):
#         return self.answer

class TF_Question(models.Model):
    question = models.TextField()
    title = 'TF'
    TF_Question_Option = (
         ('t', 'True'),
         ('f', 'False'),
    )

    answers= models.CharField(max_length=1, choices=TF_Question_Option, blank=True, default='f', help_text='Semester')

    def __str__(self):
        return self.title

class ESS_Question(models.Model):
    title = 'ESS'
    question = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title

class ORD_Question(models.Model):
    title = 'ORD'
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class MAT_Question(models.Model):
    title = 'MAT'
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class NUM_Question(models.Model):
    title = 'NUM'
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class SR_Question(models.Model):
    title = 'SR'
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class FIB_PLUS_Question(models.Model):
    title = 'FIB_PLUS'
    question = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class QuestionTypes(models.Model):
    #exam = models.ForeignKey(Exam, help_text='Exam')

    Multuple_Choice_Question = models.ManyToManyField(MC_Question, help_text='Multuple Choice Questions')
    Multuple_Answer_Question = models.ManyToManyField(MA_Question, help_text='Multuple Answer Questions')
    True_or_False_Question = models.ManyToManyField(TF_Question, help_text='True or False Questions')
    Essay_Question = models.ManyToManyField(ESS_Question, help_text='Essay Questions')
    Order_Question = models.ManyToManyField(ORD_Question, help_text='Ordering Questions')
    Match_Question = models.ManyToManyField(MAT_Question, help_text='Matching Questions')
    Numeric_Reponse_Question = models.ManyToManyField(NUM_Question, help_text='Number Response  Questions')
    Short_Reponse_Question = models.ManyToManyField(SR_Question, help_text='Multuple Choice Questions')
    Fill_in_blank_Question = models.ManyToManyField(FIB_PLUS_Question, help_text='Fill in the Blank Questions')

    def __str__(self):
        return self.Multuple_Choice_Question

class Exam(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the Exam name (e.g. Midterm exam 1)")
    ExamDate = models.DateField(null=True, blank=True)
    InstrucorName = models.CharField(max_length=200, help_text="Enter Instructors name (e.g. Sertac Artan)")
    InstructorsEmail = models.EmailField(max_length=200, help_text="Enter Instructors email (e.g. dshakhbu@nyit.edu")

    SemesterOptions = (
        ('f', 'Fall'),
        ('s', 'Spring'),
        ('l', 'Summer'),
        ('w', 'Winter'),
    )

    semester= models.CharField(max_length=1, choices=SemesterOptions, blank=True, default='f', help_text='Semester')
    Year = models.CharField(max_length=200, help_text="Enter the Year (e.g. 2017)")
    Course = models.ForeignKey(Course, help_text="Select a Course for this Exam")


    Multuple_Choice_Question = models.ManyToManyField(MC_Question, help_text='Multuple Choice Questions')
    Multuple_Answer_Question = models.ManyToManyField(MA_Question, help_text='Multuple Answer Questions')
    True_or_False_Question = models.ManyToManyField(TF_Question, help_text='True or False Questions')
    Essay_Question = models.ManyToManyField(ESS_Question, help_text='Essay Questions')
    Order_Question = models.ManyToManyField(ORD_Question, help_text='Ordering Questions')
    Match_Question = models.ManyToManyField(MAT_Question, help_text='Matching Questions')
    Numeric_Reponse_Question = models.ManyToManyField(NUM_Question, help_text='Number Response  Questions')
    Short_Reponse_Question = models.ManyToManyField(SR_Question, help_text='Multuple Choice Questions')
    Fill_in_blank_Question = models.ManyToManyField(FIB_PLUS_Question, help_text='Fill in the Blank Questions')

    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('exam-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
        