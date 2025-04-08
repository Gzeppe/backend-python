from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from files.forms import UploadForm
from django import forms
from .models import File


def index(request):
    return render(request, 'files/index.html')

def files(request):
    data = File.objects.all()
    return render(request, 'files/files.html', {'files': data, 'form': UploadForm})

def file(request, file_id):
    # Safely fetch the file using get_object_or_404
    f = get_object_or_404(File, pk=file_id)
    return render(request, 'files/file.html', {'file': f})

def edit(request, file_id):
    f = get_object_or_404(File, pk=file_id)  # Safely fetch the file
    if request.method == "POST":
        name = request.POST.get('name')
        file_type = request.POST.get('type')
        
        # Only update fields if they are provided in the form
        if name:
            f.name = name
        if file_type:
            f.file_type = file_type
        
        f.save()  # Save the updated file
        return redirect('files')  # Redirect to the files list
    else:
        return render(request, 'files/edit.html', {'file': f})  # Render the edit form with the file details

def delete(request, file_id):
    f = get_object_or_404(File, pk=file_id)  # Safely fetch the file
    f.delete()  # Delete the file
    return redirect('files')  # Redirect to the files list

def upload(request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the uploaded file
        return redirect(files)  # Redirect to the files list

class UploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file_type', 'file']  # Make sure 'file' is included as a field

