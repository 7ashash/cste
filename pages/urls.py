from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView  # ✅ تم الاستيراد
from django.urls import reverse_lazy

urlpatterns = [
    path('login', views.index, name='index'),
    path('login/submit', views.login_view, name='login_submit'),
    path('home', views.back_Home, name='home'),
    path('courses', views.back_courses, name='courses'),
    path('courses_2', views.lectures_list, name='courses_2'),
    path('profile', views.back_profile, name='profile'),
    path('lectures', views.lectures_list, name='lectures'),
    path('submit_feedback', views.submit_feedback, name='submit_feedback'),
    
    # ✅ مسار تسجيل الخروج
path('login', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
