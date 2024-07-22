from django.shortcuts import render

# Create your views here.

#just renders index.html which is the home page

def render_index(request):
    return render(request,'index.html')

