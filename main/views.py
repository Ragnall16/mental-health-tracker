from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306210550',
        'name': 'Ragnall Muhammad Al Fath',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)