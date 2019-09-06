from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request, 'account/login.html')


def register(request):
    # if request.method == 'POST':

    return render(request, 'account/register.html')
