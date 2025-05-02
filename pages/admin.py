from django.contrib import admin
from .models import Lecture, Student, Feedback

@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'email', 'major', 'gpa')
    search_fields = ('student_id', 'name', 'email')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('feedback_type', 'name', 'email', 'submitted_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('feedback_type', 'submitted_at')
