from django.shortcuts import render
from .forms import ImageForm
from .models import Image

def home(request):
    # for show the data in site
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    # to public image on site
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img':img, 'form':form})
