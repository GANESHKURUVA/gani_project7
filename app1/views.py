from django.shortcuts import render

# Create your views here.
def csk(request):
    d={
        'name':'MS DHONI',
        'age':38,
        'team':csk,
    }
    return render(request,'csk.html',context=d)