from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'calculate/home.html')
def calculate(request):
    print(request.GET.get('a'))
    if (request.GET.get('a') or request.GET.get('b')) == '':
        return render(request,'calculate/error.html')
    num1=int(request.GET.get('a'))
    num2=int(request.GET.get('b'))
    print(num1)
    print(num2)
    ans=0
    if request.GET.get('add'):
        ans=num1+num2
    elif request.GET.get('sub'):
        ans=num1-num2
    elif request.GET.get('mul'):
        ans=num1*num2
    elif request.GET.get('div'):
        ans=num1//num2
    return render(request,'calculate/calc.html',{"answer":ans})
