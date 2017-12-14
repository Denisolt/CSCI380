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
    name = models.CharField(max_length=200, help_text="Enter the Department's name (e.g. Computer Science)")
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
    name = models.CharField(max_length=600, help_text="Enter the CourseID (e.g. Artificial Intelligence)")
    DepartmentName = models.ForeignKey(Department)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('course-detail', args=[str(self.id)])

class Exam(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the Exam name (e.g. Midterm exam 1)")
    ExamDate = models.DateField(null=True, blank=True)
    InstrucorName = models.CharField(max_length=600, help_text="Enter Instructors name (e.g. Sertac Artan)")
    InstructorsEmail = models.EmailField(max_length=600, help_text="Enter Instructors email (e.g. dshakhbu@nyit.edu)")

    SemesterOptions = (
        ('fall', 'Fall'),
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('winter', 'Winter'),
    )

    semester= models.CharField(max_length=6, choices=SemesterOptions, blank=True, default='fall', help_text='Semester')
    Year = models.CharField(max_length=600, help_text="Enter the Year (e.g. 2017)")
    Course = models.ForeignKey(Course, help_text="Select a Course for this Exam")
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('exam-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class MC_Question(models.Model):
    exam = models.ForeignKey(Exam, help_text="Select exam for this question")
    question = models.TextField()
    TF_Question_Option = (
         ('correct', 'correct'),
         ('incorrect', 'incorrect'),
         ('null', 'null')
    )
    title = 'MC'

    A = models.CharField(max_length=600, default='null')
    correctness1 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    B = models.CharField(max_length=600, default='null')
    correctness2 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    C = models.CharField(max_length=600, default='null')
    correctness3 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    D = models.CharField(max_length=600, default='null')
    correctness4 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    E = models.CharField(max_length=600, default='null')
    correctness5 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    F = models.CharField(max_length=600, default='null')
    correctness6 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    G = models.CharField(max_length=600, default='null')
    correctness7 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    H = models.CharField(max_length=600, default='null')
    correctness8 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    I = models.CharField(max_length=600, default='null')
    correctness9 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    J = models.CharField(max_length=600, default='null')
    correctness10 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    K = models.CharField(max_length=600, default='null')
    correctness11 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    M = models.CharField(max_length=600, default='null')
    correctness12 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    L = models.CharField(max_length=600, default='null')
    correctness13 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    N = models.CharField(max_length=600, default='null')
    correctness14 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    O = models.CharField(max_length=600, default='null')
    correctness15 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    P = models.CharField(max_length=600, default='null')
    correctness16 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    Q = models.CharField(max_length=600, default='null')
    correctness17 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    R = models.CharField(max_length=600, default='null')
    correctness18 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    S = models.CharField(max_length=600, default='null')
    correctness19 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    T = models.CharField(max_length=600, default='null')
    correctness20 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('MCQ-detail', args=[str(self.id)])


class MA_Question(models.Model):
    exam = models.ForeignKey(Exam)
    question = models.TextField()
    title = 'MA'

    TF_Question_Option = (
         ('correct', 'correct'),
         ('incorrect', 'incorrect'),
         ('null', 'null')
    )
    title = 'MC'

    A = models.CharField(max_length=600, default='null')
    correctness1 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    B = models.CharField(max_length=600, default='null')
    correctness2 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    C = models.CharField(max_length=600, default='null')
    correctness3 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    D = models.CharField(max_length=600, default='null')
    correctness4 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    E = models.CharField(max_length=600, default='null')
    correctness5 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    F = models.CharField(max_length=600, default='null')
    correctness6 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    G = models.CharField(max_length=600, default='null')
    correctness7 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    H = models.CharField(max_length=600, default='null')
    correctness8 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    I = models.CharField(max_length=600, default='null')
    correctness9 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    J = models.CharField(max_length=600, default='null')
    correctness10 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    K = models.CharField(max_length=600, default='null')
    correctness11 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    M = models.CharField(max_length=600, default='null')
    correctness12 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    L = models.CharField(max_length=600, default='null')
    correctness13 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    N = models.CharField(max_length=600, default='null')
    correctness14 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    O = models.CharField(max_length=600, default='null')
    correctness15 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    P = models.CharField(max_length=600, default='null')
    correctness16 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    Q = models.CharField(max_length=600, default='null')
    correctness17 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    R = models.CharField(max_length=600, default='null')
    correctness18 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    S = models.CharField(max_length=600, default='null')
    correctness19 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    T = models.CharField(max_length=600, default='null')
    correctness20 = models.CharField(max_length=9, choices=TF_Question_Option, blank=True, default='null', help_text='Correct or not corerect')

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('MAQ-detail', args=[str(self.id)])

class TF_Question(models.Model):
    exam = models.ForeignKey(Exam)
    question = models.TextField()
    title = 'TF'
    TF_Question_Option = (
         ('True', 'True'),
         ('False', 'False'),
    )

    answers= models.CharField(max_length=5, choices=TF_Question_Option, blank=True, default='null')

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('TFQ-detail', args=[str(self.id)])

class ESS_Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = 'ESS'
    question = models.CharField(max_length=600)
    answer = models.TextField(default='null')

    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('ESSQ-detail', args=[str(self.id)])

class ORD_Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = 'ORD'
    question = models.CharField(max_length=600)
    correct = models.CharField(max_length=600, help_text='enter the correct order')
    answer1 = models.CharField(max_length=600, default='null')
    answer2 = models.CharField(max_length=600, default='null')
    answer3 = models.CharField(max_length=600, default='null')
    answer4 = models.CharField(max_length=600, default='null')
    answer5 = models.CharField(max_length=600, default='null')
    answer6 = models.CharField(max_length=600, default='null')
    answer7 = models.CharField(max_length=600, default='null')
    answer8 = models.CharField(max_length=600, default='null')
    answer9 = models.CharField(max_length=600, default='null')
    answer10 = models.CharField(max_length=600, default='null')
    answer11 = models.CharField(max_length=600, default='null')
    answer12 = models.CharField(max_length=600, default='null')
    answer13 = models.CharField(max_length=600, default='null')
    answer14 = models.CharField(max_length=600, default='null')
    answer15 = models.CharField(max_length=600, default='null')
    answer16 = models.CharField(max_length=600, default='null')
    answer17 = models.CharField(max_length=600, default='null')
    answer18 = models.CharField(max_length=600, default='null')
    answer19 = models.CharField(max_length=600, default='null')
    answer20 = models.CharField(max_length=600, default='null')

    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('ORDQ-detail', args=[str(self.id)])

class MAT_Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = 'MAT'
    question = models.CharField(max_length=600)
    correct = models.CharField(max_length=600, help_text='enter the correct match, in format number-letter, etc')
    A = models.CharField(max_length=600, default='null')
    B = models.CharField(max_length=600, default='null')
    C = models.CharField(max_length=600, default='null')
    D = models.CharField(max_length=600, default='null')
    E = models.CharField(max_length=600, default='null')
    F = models.CharField(max_length=600, default='null')
    G = models.CharField(max_length=600, default='null')
    H = models.CharField(max_length=600, default='null')
    I = models.CharField(max_length=600, default='null')
    J = models.CharField(max_length=600, default='null')
    K = models.CharField(max_length=600, default='null')
    M = models.CharField(max_length=600, default='null')
    L = models.CharField(max_length=600, default='null')
    N = models.CharField(max_length=600, default='null')
    O = models.CharField(max_length=600, default='null')
    P = models.CharField(max_length=600, default='null')
    Q = models.CharField(max_length=600, default='null')
    R = models.CharField(max_length=600, default='null')
    S = models.CharField(max_length=600, default='null')
    T = models.CharField(max_length=600, default='null')

    answer1 = models.CharField(max_length=600, default='null')
    answer2 = models.CharField(max_length=600, default='null')
    answer3 = models.CharField(max_length=600, default='null')
    answer4 = models.CharField(max_length=600, default='null')
    answer5 = models.CharField(max_length=600, default='null')
    answer6 = models.CharField(max_length=600, default='null')
    answer7 = models.CharField(max_length=600, default='null')
    answer8 = models.CharField(max_length=600, default='null')
    answer9 = models.CharField(max_length=600, default='null')
    answer10 = models.CharField(max_length=600, default='null')
    answer11 = models.CharField(max_length=600, default='null')
    answer12 = models.CharField(max_length=600, default='null')
    answer13 = models.CharField(max_length=600, default='null')
    answer14 = models.CharField(max_length=600, default='null')
    answer15 = models.CharField(max_length=600, default='null')
    answer16 = models.CharField(max_length=600, default='null')
    answer17 = models.CharField(max_length=600, default='null')
    answer18 = models.CharField(max_length=600, default='null')
    answer19 = models.CharField(max_length=600, default='null')
    answer20 = models.CharField(max_length=600, default='null')


    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('MATQ-detail', args=[str(self.id)])

class NUM_Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = 'NUM'
    question = models.CharField(max_length=600)
    answer = models.IntegerField(default=0)
    def __str__(self):
        return self.question
    def get_absolute_url(self):
        return reverse('NUMQ-detail', args=[str(self.id)])

class SR_Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = 'SR'
    question = models.CharField(max_length=600)
    answer = models.TextField(default='null')

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('SRQ-detail', args=[str(self.id)])

class FIB_PLUS_Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = 'FIB_PLUS'
    question = models.CharField(max_length=600)
    x = models.CharField(max_length=600, default='null')
    y = models.CharField(max_length=600, default='null')
    z = models.CharField(max_length=600, default='null')
    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('FIB-PLUS-Q-detail', args=[str(self.id)])

class FIB_SINGLE_Question(models.Model):
    exam = models.ForeignKey(Exam)
    title = 'FIB_SINGLE'
    question = models.CharField(max_length=600)
    x = models.CharField(max_length=600, default='null')
    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('FIBQ-detail', args=[str(self.id)])