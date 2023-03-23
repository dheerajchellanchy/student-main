from tkinter import Label
from django import forms
from django.forms import widgets
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        labels = {
            'dob': ('Date of Birth'),
        }

        fields = (
            'name', 'mob', 'reg_number', 'course', 'parent_name', 'parent_contact', 'semester', 'dob', 'joining_date',
            'profile_picture')

        widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mob': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control', }),
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_number': forms.TextInput(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-control', }),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),

        }


class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        labels = {
            'dob': ('Date of Birth'),
        }

        fields = ('name', 'staff_code', 'designation', 'mob', 'dob', 'joining_date', 'profile_picture')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'staff_code': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-control', }),
            'mob': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        labels = {
            'dob': ('Date of Birth'),
        }
        fields = ('name', 'user_name', 'course', 'subject', 'mob', 'dob', 'joining_date', 'profile_picture')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control', }),
            'subject': forms.Select(attrs={'class': 'form-control', }),
            'mob': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        labels = {
            'dob': ('Date of Birth'),
        }
        fields = ('name', 'user_name', 'student', 'mob', 'dob', 'profile_picture')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control', }),
            'mob': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
        }


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('heading', 'description')

        widgets = {
            'heading': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class leaveform(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ('date', 'days', 'reson')
        widgets = {

            'date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control'}),
            'days': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'No Of Days You Needed Leave'}),
            'reson': forms.Textarea(attrs={'class': 'form-control ', 'placeholder': "Specify The Reson"}),
        }
        labels = {
            'reson': "",
            'date': "",
            'days': "",

        }


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('student', 'course', 'semester', 'subject', 'mark', 'date_of_exam')

        widgets = {
            'mark': forms.NumberInput(attrs={'class': 'form-control'}),
            'student': forms.Select(attrs={'class': 'form-control', }),
            'course': forms.Select(attrs={'class': 'form-control', }),
            'semester': forms.Select(attrs={'class': 'form-control', }),
            'subject': forms.Select(attrs={'class': 'form-control', }),
            'date_of_exam': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', }),
        }


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ('book_name', 'author', 'course', 'semester', 'subject')

        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control', }),
            'semester': forms.Select(attrs={'class': 'form-control', }),
            'subject': forms.Select(attrs={'class': 'form-control', }),
        }
