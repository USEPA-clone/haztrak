from django.shortcuts import render


# Create your views here.
def emanifest(request):
    return render(request, 'base.html')
