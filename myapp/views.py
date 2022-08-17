from django.shortcuts import render
from myapp.forms import ImageForm
from myapp.models import Image

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
        
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html',{'form':form,'img':img})