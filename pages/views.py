from django.shortcuts import render, redirect
from .models import Lecture, Student

# صفحة تسجيل الدخول
def index(request):
    return render(request, 'pages/login.html')

# تسجيل الدخول
def login_view(request):
    error_message = None

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(student_id=student_id)
            if student.password == password:
                request.session['student_id'] = student.student_id  # حفظ الـ ID في السيشن
                return redirect('home')
            else:
                error_message = "Invalid ID or Password."
        except Student.DoesNotExist:
            error_message = "Invalid ID or Password."

    return render(request, 'pages/login.html', {'error_message': error_message})

# الصفحة الرئيسية
def back_Home(request):
    return render(request, 'pages/home.html')

# صفحة المحاضرات 1
def back_courses(request):
    return render(request, 'pages/courses.html')

# صفحة المحاضرات 2 + عرض المحاضرات من قاعدة البيانات
def back_courses_2(request):
    lectures = Lecture.objects.all().order_by('-uploaded_at')
    return render(request, 'pages/courses_2.html', {'lectures': lectures})

# صفحة البروفايل - عرض بيانات الطالب الحقيقي
def back_profile(request):
    student_id = request.session.get('student_id')
    if student_id:
        try:
            student = Student.objects.get(student_id=student_id)
            return render(request, 'pages/profile.html', {'student': student})
        except Student.DoesNotExist:
            return redirect('login')  # لو الطالب مش موجود
    else:
        return redirect('login')  # لو مفيش تسجيل دخول

# بديل مباشر لعرض المحاضرات لو محتاج لوحدها
def lectures_list(request):
    lectures = Lecture.objects.all().order_by('-uploaded_at')
    return render(request, 'pages/courses_2.html', {'lectures': lectures})

from .models import Feedback

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        feedback_type = request.POST.get('feedback_type', '')
        message = request.POST.get('message', '')

        Feedback.objects.create(
            name=name,
            email=email,
            feedback_type=feedback_type,
            message=message
        )
        return redirect('home')  # أو رسالة شكر، حسب ما تحب
    else:
        return redirect('home')
from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # حذف السيشن
    request.session.flush()  # تأكيد حذف كل البيانات
    return redirect('index')  # بيرجعك لصفحة login
