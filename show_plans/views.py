from django.shortcuts import render
import requests


def simple_view(request):
    response = requests.get("http://localhost:8000/plans/api/").json()
    context = {'response': response}
    return render(request, 'show_plans/home.html', context)


    # data = response.json()
    # context = {'plans': response}
    # return render(request, 'show_plans/home.html', context)


# def simple_view(request):
#     response=requests.get('https://api.covid19api.com/countries')
#     render(request,'show_plans/home.html',{'response':response})
