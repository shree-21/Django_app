from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.

def photo_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'photo_app/photo_upload.html',
            { 
                'uploaded_file_url': uploaded_file_url
            })
    return render(request, 'photo_app/photo_upload.html')