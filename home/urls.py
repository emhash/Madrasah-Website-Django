from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='homes'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.the_login, name='login'),
    path('faculty/', views.faculty, name='faculty'),
    path('employee/', views.third_grade_employee, name='employee'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('routine/', views.routine, name='routine'),
    path('results/', views.results, name='results'),
    path('all_class/', views.all_class, name='all_class'),
    path('student_info/', views.student_info, name='student_info'),
    path('notice/', views.notice, name='notice'),
    path('downloadfile/<int:pk>/', views.downloadfile, name='downloadfile'),

    path('admins/<int:pk>', views.admins, name='admins'),



    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if not settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

