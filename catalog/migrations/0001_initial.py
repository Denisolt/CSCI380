# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-12-09 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the College (e.g. NYIT, PACE, etc)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseID', models.CharField(help_text='Enter the CourseID (e.g. CSCI 360)', max_length=200)),
                ('name', models.CharField(help_text='Enter the CourseID (e.g. Artificial Intelligence)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DeniIsHere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the Department's name (e.g. Computer Science", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ESS_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the Exam name (e.g. Midterm exam 1)', max_length=200)),
                ('ExamDate', models.DateField(blank=True, null=True)),
                ('InstrucorName', models.CharField(help_text='Enter Instructors name (e.g. Sertac Artan)', max_length=200)),
                ('InstructorsEmail', models.EmailField(help_text='Enter Instructors email (e.g. dshakhbu@nyit.edu', max_length=200)),
                ('semester', models.CharField(blank=True, choices=[('fall', 'Fall'), ('spring', 'Spring'), ('summer', 'Summer'), ('winter', 'Winter')], default='fall', help_text='Semester', max_length=6)),
                ('Year', models.CharField(help_text='Enter the Year (e.g. 2017)', max_length=200)),
                ('Course', models.ForeignKey(help_text='Select a Course for this Exam', on_delete=django.db.models.deletion.CASCADE, to='catalog.Course')),
            ],
        ),
        migrations.CreateModel(
            name='FIB_PLUS_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='MA_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer1', models.CharField(default='null', max_length=200)),
                ('correctness1', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer2', models.CharField(default='null', max_length=200)),
                ('correctness2', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer3', models.CharField(default='null', max_length=200)),
                ('correctness3', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer4', models.CharField(default='null', max_length=200)),
                ('correctness4', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer5', models.CharField(default='null', max_length=200)),
                ('correctness5', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer6', models.CharField(default='null', max_length=200)),
                ('correctness6', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer7', models.CharField(default='null', max_length=200)),
                ('correctness7', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer8', models.CharField(default='null', max_length=200)),
                ('correctness8', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer9', models.CharField(default='null', max_length=200)),
                ('correctness9', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer10', models.CharField(default='null', max_length=200)),
                ('correctness10', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer11', models.CharField(default='null', max_length=200)),
                ('correctness11', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer12', models.CharField(default='null', max_length=200)),
                ('correctness12', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer13', models.CharField(default='null', max_length=200)),
                ('correctness13', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer14', models.CharField(default='null', max_length=200)),
                ('correctness14', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer15', models.CharField(default='null', max_length=200)),
                ('correctness15', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer16', models.CharField(default='null', max_length=200)),
                ('correctness16', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer17', models.CharField(default='null', max_length=200)),
                ('correctness17', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer18', models.CharField(default='null', max_length=200)),
                ('correctness18', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer19', models.CharField(default='null', max_length=200)),
                ('correctness19', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer20', models.CharField(default='null', max_length=200)),
                ('correctness20', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='MAT_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='MC_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer1', models.CharField(default='null', max_length=200)),
                ('correctness1', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer2', models.CharField(default='null', max_length=200)),
                ('correctness2', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer3', models.CharField(default='null', max_length=200)),
                ('correctness3', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer4', models.CharField(default='null', max_length=200)),
                ('correctness4', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer5', models.CharField(default='null', max_length=200)),
                ('correctness5', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer6', models.CharField(default='null', max_length=200)),
                ('correctness6', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer7', models.CharField(default='null', max_length=200)),
                ('correctness7', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer8', models.CharField(default='null', max_length=200)),
                ('correctness8', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer9', models.CharField(default='null', max_length=200)),
                ('correctness9', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer10', models.CharField(default='null', max_length=200)),
                ('correctness10', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer11', models.CharField(default='null', max_length=200)),
                ('correctness11', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer12', models.CharField(default='null', max_length=200)),
                ('correctness12', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer13', models.CharField(default='null', max_length=200)),
                ('correctness13', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer14', models.CharField(default='null', max_length=200)),
                ('correctness14', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer15', models.CharField(default='null', max_length=200)),
                ('correctness15', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer16', models.CharField(default='null', max_length=200)),
                ('correctness16', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer17', models.CharField(default='null', max_length=200)),
                ('correctness17', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer18', models.CharField(default='null', max_length=200)),
                ('correctness18', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer19', models.CharField(default='null', max_length=200)),
                ('correctness19', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('answer20', models.CharField(default='null', max_length=200)),
                ('correctness20', models.CharField(blank=True, choices=[('correct', 'correct'), ('incorrect', 'incorrect'), ('null', 'null')], default='null', help_text='Correct or not corerect', max_length=9)),
                ('exam', models.ForeignKey(help_text='Select exam for this question', on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='NUM_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='ORD_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter School's name (e.g. School of Engineering)", max_length=200)),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.College')),
            ],
        ),
        migrations.CreateModel(
            name='SR_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='TF_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answers', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], default='null', help_text='Semester', max_length=5)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam')),
            ],
        ),
        migrations.AddField(
            model_name='ess_question',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam'),
        ),
        migrations.AddField(
            model_name='department',
            name='SchoolName',
            field=models.ForeignKey(help_text='Select a School for this Department', on_delete=django.db.models.deletion.CASCADE, to='catalog.School'),
        ),
        migrations.AddField(
            model_name='deniishere',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Exam'),
        ),
        migrations.AddField(
            model_name='course',
            name='DepartmentName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Department'),
        ),
    ]