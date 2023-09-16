from django.shortcuts import render,redirect
from .models import *
from django.core.paginator import Paginator

def home_common_data(request):
    data = BasicInfo.objects.first()
    link1 = ImportantLink1.objects.all()
    link2 = ImportantLink2.objects.all()
    context = {
        'madrasa' : data,
        'link1' : link1,
        'link2' : link2,
    }
    return context 



def home(request):
    noti = Notice.objects.all()
    paginator = Paginator(noti, 10)
    page_number = request.GET.get('notices')
    notices = paginator.get_page(page_number)

    marque = Notice.objects.all().order_by('-uploaded_at')[:5]
    
    professor1 = Lagacy.objects.first()
    professor2 = Lagacy.objects.all()[1]


    sliders = Slider.objects.all()
    # for i in sliders:
    #     print(i.photo_title)

    g = Gallary.objects.all()

    context = {
        'notices' : notices,
        'marque' : marque,
        'admins' : professor2,
        'headmaster' : professor1,
        'sliders' : sliders,
        'pic' : g,

    }

    return render(request, 'main/index.html', context )


def contact(request):

    return render(request, 'main/contact.html')

def about(request):

    return render(request, 'main/about.html')

def the_login(request):

    return render(request, 'main/login.html')

def third_grade_employee(request):
    data = Employee.objects.all()
    context = {
        'employees':data,
    }
    return render(request, 'main/employee.html', context)

def syllabus(request):
    sy = Syllabus.objects.all()

    return render(request, 'main/syllabus.html', {'sy':sy})

def routine(request):

    return render(request, 'main/temp.html')

def results(request):

    return render(request, 'main/temp.html')

def faculty(request):
    stuff = Teacher.objects.all()
    data = {
        'teachers' : stuff,
    }

    return render(request, 'main/faculty.html', data)

def all_class(request):
    professor1 = Lagacy.objects.first()
    professor2 = Lagacy.objects.all()[1]

    return render(request, 'main/temp.html', {'admins' : professor2,'headmaster' : professor1,})

def student_info(request):

    return render(request, 'main/temp.html')

def notice(request):
    notices = Notice.objects.all()
    context = {
        'notices' : notices,
    }
    return render(request, 'main/notice.html', context)



def admins(request, pk):
    profiles = Lagacy.objects.get(id=pk)
    # print(profiles)
    return render(request, 'main/admin.html' , {'admins' : profiles,})

# --------------------------------------------------------------------

# ============ This is for click and download file(IE - PDF) ==========

import os
from django.http import StreamingHttpResponse 
from wsgiref.util import FileWrapper
import mimetypes

def downloadfile(request, pk):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    files = Syllabus.objects.get(id=pk)
    loc = str(files.add_file.url)
    filepath = base_dir + loc

    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(
        FileWrapper(open(thefile, 'rb'), chunk_size),
        content_type=mimetypes.guess_type(thefile)[0],
    )
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response




# =-------------------------------------------------------------------------------=