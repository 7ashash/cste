from django.db import models

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='lectures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)  # مبدئيًا نخليها نص عادي، نقدر نغيرها لاحقًا لتشفير
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    address = models.TextField()
    rank = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    expected_graduation = models.DateField()

    def __str__(self):
        return f"{self.student_id} - {self.name}"

class Feedback(models.Model):
    FEEDBACK_CHOICES = [
        ('Complaint', 'Complaint'),
        ('Suggestion', 'Suggestion'),
    ]

    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.feedback_type} from {self.name or 'Anonymous'}"
