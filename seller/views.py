from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')


def login(request):
    return render(request, 'login.html')



def test(request):
    return render(request, 'test.html')