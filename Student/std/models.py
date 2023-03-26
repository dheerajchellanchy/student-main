from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django.db.models import Q


class Profile(models.Model):
    role = (
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('Parent', 'Parent'),
        ('Admin', 'Admin'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True, choices=role)
    admin = models.BooleanField(null=True, blank=True, default=False)
    status = models.CharField(max_length=50, default="alive")
    datejoined = models.DateField(auto_now_add=True, null=True)
    profile_picture = models.ImageField(default="dora.jpg")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    parent_name = models.CharField(max_length=200, null=True, blank=True)
    parent_contact = models.CharField(max_length=200, null=True, blank=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, null=True)
    reg_number = models.CharField(max_length=20, null=True, blank=True)
    mob = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(auto_now=False, null=True)
    joining_date = models.DateField(auto_now=False, null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default="alive") #deleted
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    profile_picture = models.ImageField(default="dora.jpg")
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    staff_code = models.CharField(max_length=200, null=True, blank=True)
    designation = models.ForeignKey('Designation', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    mob = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(auto_now=False, null=True)
    joining_date = models.DateField(auto_now=False, null=True)
    status = models.CharField(max_length=50, default="alive")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    profile_picture = models.ImageField(default="dora.jpg")

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=200, null=True, blank=True)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    mob = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(auto_now=False, null=True)
    joining_date = models.DateField(auto_now=False, null=True)
    status = models.CharField(max_length=50, default="alive")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    profile_picture = models.ImageField(default="dora.jpg")

    def __str__(self):
        return self.name


class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    user_name = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    mob = models.CharField(max_length=20, null=True, blank=True)
    dob = models.DateField(auto_now=False, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=50, default="alive")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    profile_picture = models.ImageField(default="dora.jpg")

    def __str__(self):
        return self.name


class Announcement(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=50, default="alive")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='attendance_approved_user')
    status = models.CharField(max_length=50, default="Absent")  # Present
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.id)


class Leave(models.Model):
    send_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='approved_by')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='student_leave')
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    days = models.IntegerField(null=True)
    reson = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(default="requested", max_length=50)
    adminreson = models.CharField(max_length=500, null=True, blank=True)
    view = models.CharField(max_length=20, default="adminnotviewed", null=True)

    def __str__(self):
        return str(self.view)


class Course(models.Model):
    status = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    name = models.CharField(max_length=500, null=True, blank=True)
    code = models.CharField(max_length=20, default="0")
    status = models.CharField(max_length=50, null=True, blank=True, choices=status, default="Active")

    def __str__(self):
        return str(self.name)


class Semester(models.Model):
    status = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    name = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=status, default="Active")

    def __str__(self):
        return str(self.name)


class Designation(models.Model):
    status = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    name = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=status, default="Active")

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    status = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    name = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True, choices=status, default="Active")

    def __str__(self):
        return str(self.name)


class Mark(models.Model):
    mark = models.IntegerField(null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    date_of_exam = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.mark


class Reference(models.Model):
    book_name = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=500, null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True)
    attachment = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.mark
