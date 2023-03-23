from django.shortcuts import render
from django.forms.fields import DateField
from django import http
from django.urls import reverse
from django.forms import inlineformset_factory
from django.http import request
from django.shortcuts import redirect, render
from .forms import *
from .models import *
from django.contrib.auth.models import User, auth
from .decorators import adminonly, staffonly
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q


def home(request):
    return render(request, "index.html")


def check_user_name(username, request):
    if User.objects.filter(username=username).exists():
        print('here')
        messages.error(request, 'Username Already Taken')
        return True
    else:
        return False


# def adminlogin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect("admindash")
#         else:
#             messages.error(request, ("invalid username or password !"))
#
#     return render(request, "adminlogin.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("admindash")
        else:
            messages.error(request, ("invalid username or password !"))
    return render(request, "stafflogin.html")


@login_required(login_url="home")
def admindash(request):
    student_count = Student.objects.filter(status="alive")
    admincount = Profile.objects.filter(admin=True)
    leave = Leave.objects.filter(view="adminnotviewed")
    staff = Staff.objects.filter(status="alive")
    teacher = Teacher.objects.filter(status="alive")
    parent = Parent.objects.filter(status="alive")
    context = {'name': request.user, "student_count": student_count, "admin": admincount, "leave": leave,
               'staff': staff, 'teacher': teacher, 'parent': parent}
    return render(request, 'admin.html', context)


@login_required(login_url="home")
def addstudent(request):
    form = StudentForm()
    if request.method == 'POST':
        print(request)
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['reg_number']
            flag = check_user_name(username, request)
            if flag:
                return http.HttpResponseRedirect(reverse('addstudent'))
            password = 'PS' + str(form.cleaned_data['reg_number'])
            user = User.objects.create_user(username=username, password=password, email=request.POST["email"],
                                            first_name=form.cleaned_data['name'])
            user.save()
            profile = Profile.objects.create(role='Student', user=user, completed=True)
            empl = form.save(commit=False)
            empl.user = user
            empl.save()
            return redirect("admindash")
        else:
            messages.error(request, str(form.errors))
            return http.HttpResponseRedirect(reverse('addstudent'))
    else:
        return render(request, 'addstudent.html', {'form': form})


@login_required(login_url="home")
def viewstudent(request):
    student = Student.objects.filter(status='alive')
    return render(request, 'viewstudent.html', {'student': student})


@login_required(login_url="home")
def addstaff(request):
    form = StaffForm()
    if request.method == 'POST':
        form = StaffForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['staff_code']
            flag = check_user_name(username, request)
            if flag:
                return http.HttpResponseRedirect(reverse('addstaff'))
            password = 'PS' + str(form.cleaned_data['staff_code'])
            user = User.objects.create_user(username=username, password=password, email=request.POST["email"],
                                            first_name=form.cleaned_data['name'])
            user.save()
            profile = Profile.objects.create(role='Staff', user=user, completed=True)
            empl = form.save(commit=False)
            empl.user = user
            empl.save()
            return redirect("admindash")
    else:
        return render(request, 'addstaff.html', {'form': form})


@login_required(login_url="home")
def viewstaff(request):
    staffs = Staff.objects.filter(status='alive')
    return render(request, 'viewstaff.html', {'staffs': staffs})


@login_required(login_url="home")
def addteacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            flag = check_user_name(username, request)
            if flag:
                return http.HttpResponseRedirect(reverse('addteacher'))
            password = 'PS' + str(form.cleaned_data['user_name'])
            user = User.objects.create_user(username=username, password=password, email=request.POST["email"],
                                            first_name=form.cleaned_data['name'])
            user.save()
            profile = Profile.objects.create(role='Teacher', user=user, completed=True)
            empl = form.save(commit=False)
            empl.user = user
            empl.save()
            return redirect("admindash")
    else:
        return render(request, 'addteacher.html', {'form': form})


@login_required(login_url="home")
def viewteacher(request):
    teachers = Teacher.objects.filter(status='alive')
    return render(request, 'viewteacher.html', {'staffs': teachers})


@login_required(login_url="home")
def addparent(request):
    form = ParentForm()
    if request.method == 'POST':
        form = ParentForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['user_name']
            flag = check_user_name(username, request)
            if flag:
                return http.HttpResponseRedirect(reverse('addparent'))
            password = 'PS' + str(form.cleaned_data['user_name'])
            user = User.objects.create_user(username=username, password=password, email=request.POST["email"],
                                            first_name=form.cleaned_data['name'])
            user.save()
            profile = Profile.objects.create(role='Parent', user=user, completed=True)
            empl = form.save(commit=False)
            empl.user = user
            empl.save()
            return redirect("admindash")
    else:
        return render(request, 'addparent.html', {'form': form})


@login_required(login_url="home")
def viewparent(request):
    parent = Parent.objects.filter(status='alive')
    return render(request, 'viewparent.html', {'staffs': parent})


@login_required(login_url="home")
def addannouncement(request):
    form = AnnouncementForm()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.created_by = request.user
            form_data.save()
            return redirect("admindash")
    else:
        return render(request, 'addannouncement.html', {'form': form})


@login_required(login_url="home")
def viewannouncement(request):
    announcements = Announcement.objects.filter(status='alive').order_by('created_at')
    return render(request, 'viewannouncements.html', {'announcements': announcements})


@login_required(login_url="home")
def leave(request):
    notification = False
    leavenot = Leave.objects.filter(send_by=request.user)
    for i in leavenot:
        if i.view == "sendernotviewed":
            notification = True
            break
        else:
            notification = False

    form = leaveform
    if request.method == "POST":
        form = leaveform(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.send_by = request.user
            try:
                student = Parent.objects.get(user=request.user).student
            except Exception as e:
                student = None
                print(e)
            leave.student = student
            leave.view = "adminnotviewed"
            leave.save()
            messages.success(request, ("Leave request has been sent"))
            return redirect(admindash)

    return render(request, 'leave.html', {'notification': notification, 'form': form})


@login_required(login_url="home")
def adminviewleaverequest(request):
    leaves = Leave.objects.all()
    abc = 0
    abc = Leave.objects.filter(status='requested')
    if abc:
        abc = 1
    else:
        abc = 0
    Context = {'leaves': leaves, 'abc': abc}
    if request.method == "POST":
        id = request.POST["id"]
        reason = request.POST["reson"]
        leav = Leave.objects.get(id=id)
        leav.status = "declined"
        leav.adminreson = reason
        leav.view = "sendernotviewed"
        leav.save()
        return redirect('adminviewleaverequest')
    return render(request, 'adminviewleaverequest.html', Context)


@login_required(login_url="home")
def adminviewleavehistory(request):
    parent = Parent.objects.filter(user=request.user)
    if Parent.objects.filter(user=request.user).exists():
        leaves = Leave.objects.filter(send_by=parent.last().user)
    else:
        leaves = Leave.objects.all()
    return render(request, 'leavehistory.html', {'leaves': leaves})


@login_required(login_url="home")
def parentviewleavehistory(request):
    leaves = Leave.objects.filter(send_by=request.user)
    return render(request, 'parentviewleavehistory.html', {'leaves': leaves})


@login_required(login_url="home")
def studentlistattendance(request):
    today = datetime.date.today()
    leaved_students = list(Attendance.objects.filter(date=today, status='Leave').values_list('student_id', flat=True))
    if not Attendance.objects.filter(date=today).exclude(status='Leave').exists():
        students = Student.objects.filter(status='alive').exclude(id__in=leaved_students)
        for student in students:
            Attendance.objects.create(student=student, date=today)
    attendance = Attendance.objects.filter(date=today)
    if Teacher.objects.filter(user=request.user).exists():
        course = Teacher.objects.get(user=request.user).course
        attendance = attendance.filter(student__course=course)
    return render(request, 'studentlistattendance.html', {'attendance': attendance})


@login_required(login_url="home")
def present(request, pk):
    attendance = Attendance.objects.get(id=pk)
    attendance.status = 'Present'
    attendance.updated_by = request.user
    attendance.save()
    return redirect(studentlistattendance)


@login_required(login_url="home")
def absent(request, pk):
    attendance = Attendance.objects.get(id=pk)
    attendance.status = 'Absent'
    attendance.updated_by = request.user
    attendance.save()
    return redirect(studentlistattendance)


@login_required(login_url="home")
def listattendance(request):
    attendance = Attendance.objects.filter().order_by('created_at')
    if Teacher.objects.filter(user=request.user).exists():
        course = Teacher.objects.get(user=request.user).course
        attendance = attendance.filter(student__course=course)
    return render(request, 'listattendance.html', {'attendance': attendance})


def logoutuser(request):
    logout(request)
    return redirect("home")


@login_required(login_url="home")
def adminviewleavedetailed(request, pk):
    details = Leave.objects.get(id=pk)
    context = {'details': details}
    if request.method == "POST":
        leav = Leave.objects.get(id=pk)
        date = leav.date
        days = leav.days
        for i in range(days):
            date = date + timedelta(days=1)
            Attendance.objects.create(student=student, date=date, status='Leave')
        leav.status = "accepted"
        leav.view = "sendernotviewed"
        leav.save()
        return redirect('adminviewleaverequest')
    return render(request, 'adminviewleavedetailed.html', context)


@login_required(login_url="home")
def adminviewattendancedetail(request, e):
    atn = Attendance.objects.filter(student=e).order_by('date')
    leavec = Attendance.objects.filter(student=e, status="Leave")
    context = {'atn': atn, 'leavec': leavec}
    if request.method == "POST":
        date = request.POST["value"]
        val = Attendance.objects.filter(student=e, date__startswith=date)
        leavec = Attendance.objects.filter(student=e, date__startswith=date, status="Leave")
        context = {'atn': val, 'leavec': leavec}
        return render(request, "adminviewatndetailed.html", context)
    return render(request, "adminviewatndetailed.html", context)


@login_required(login_url="home")
def addmarksheet(request):
    form = MarkForm()
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.updated_by = request.user
            form_data.save()
            return redirect("admindash")
    else:
        return render(request, 'addannouncement.html', {'form': form})


@login_required(login_url="home")
def viewmarksheet(request, pk):
    marks = Mark.objects.filter(student=pk).order_by('semester')
    context = {'marks': marks}
    return render(request, 'viewmarksheet.html', context)


@login_required(login_url="home")
def viewallmarksheet(request):
    marks = Mark.objects.filter().order_by('created_at')
    context = {'marks': marks}
    if request.method == "POST":
        filter_arguments = []
        course = request.POST["course"]
        semester = request.POST["semester"]
        if course not in [None, '']:
            print('fdfdfdfdf')
            filter_arguments.append(['course__name', course])
        if semester not in [None, '']:
            print('fdfdfdfdf')
            filter_arguments.append(['semester__name', semester])
        filter_arguments = dict(filter_arguments)
        marks = Mark.objects.filter(**filter_arguments).order_by('created_at')
        context = {'marks': marks}
        return render(request, "viewcompleteresult.html", context)
    return render(request, "viewcompleteresult.html", context)


@login_required(login_url="home")
def viewstudentmarksheet(request, pk):
    print(pk)
    student = Student.objects.filter(user_id=pk)
    if student.exists():
        student = student.last()
    else:
        student = Parent.objects.get(user=pk).student
    marks = Mark.objects.filter(student=student).order_by('semester')
    context = {'marks': marks}
    return render(request, 'viewmarksheet.html', context)


@login_required(login_url="home")
def addreference(request):
    form = ReferenceForm()
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.updated_by = request.user
            form_data.save()
            return redirect("admindash")
    else:
        return render(request, 'addannouncement.html', {'form': form})


@login_required(login_url="home")
def viewreferences(request):
    refer = Reference.objects.filter().order_by('course')
    student = Student.objects.filter(user=request.user)
    if student.exists():
        refer = Reference.objects.filter(course=student.last().course).order_by('semester')
    return render(request, 'viewreference.html', {'refer': refer})


@login_required(login_url="home")
def viewattendance(request):
    notification = False
    student = Student.objects.filter(user=request.user)
    if student.exists():
        student = student.last()
    else:
        student = Parent.objects.get(user=request.user).student
    atn = Attendance.objects.filter(student=student).order_by('date')
    leavec = Attendance.objects.filter(student=student, status="Leave")
    context = {'notification': notification, 'atn': atn, 'leavec': leavec}
    if request.method == "POST":
        value = request.POST["value"]
        val = Attendance.objects.filter(student__user=student, date__startswith=value)
        leavec = Attendance.objects.filter(student__user=student, date__startswith=value, status="Leave")
        context = {'notification': notification, 'atn': val, 'leavec': leavec}
        return render(request, "viewatn.html", context)
    return render(request, 'viewatn.html', context)


def studentedit(request, pk):
    instance = Student.objects.get(id=pk)
    form = StudentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('viewstudent')
    return render(request, 'studentedit.html', {'form': form})


def staffedit(request, pk):
    instance = Staff.objects.get(id=pk)
    form = StaffForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('viewstudent')
    return render(request, 'studentedit.html', {'form': form})


def teacheredit(request, pk):
    instance = Teacher.objects.get(id=pk)
    form = TeacherForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('viewteacher')
    return render(request, 'teacheredit.html', {'form': form})


def parentedit(request, pk):
    instance = Parent.objects.get(id=pk)
    form = ParentForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('viewparent')
    return render(request, 'parentedit.html', {'form': form})


def studentdelete(request, pk):
    Student.objects.filter(id=pk).update(status='deleted')
    return redirect('viewstudent')


def staffdelete(request, pk):
    Staff.objects.filter(id=pk).update(status='deleted')
    return redirect('viewstaff')


def parentdelete(request, pk):
    Parent.objects.filter(id=pk).update(status='deleted')
    return redirect('viewparent')

def teacherdelete(request, pk):
    Teacher.objects.filter(id=pk).update(status='deleted')
    return redirect('viewteacher')

# ================================================================================#
