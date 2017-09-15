from django.shortcuts import render, render_to_response
import datetime as dt
from .models import Work, Quotes, Cities

class Person():
    def __init__(self):
        self.fullName = 'Остап-Сулейман-Берта-Мария-Бендер-бей'
        self.name = 'Остап Бендер'
        self.birthday = dt.date(1900, 1, 1)
        self.hobby = 'Афёры и авантюры'
        self.study = 'Учился я в частной гимназии Илиади'

def home(request):
    person = Person()
    return render_to_response('home.html', {'person': person, 'current_page': 'home'})

def study(request):
    person = Person()
    return render_to_response('study.html',  {'person': person, 'current_page': 'study'})

def work(request):
    person = Person()
    works = Work.objects.all()
    worksList = []
    for work in works:
        arr = []
        myDict = {}
        for per in work.personages.all():
            arr.append(per.firstName + ' ' + per.secondName)
        myDict['single_work'] = work
        myDict['personages'] = arr
        worksList.append(myDict)
    return render_to_response('work.html',  {'person': person, 'current_page': 'work', 'works': worksList})

def quotes(request):
    person = Person()
    quotes = Quotes.objects.all()
    return render_to_response('quotes.html',  {'person': person, 'current_page': 'quotes', 'quotes': quotes})

def cities(request, cityID = 1):
    city = Cities.objects.get(id=cityID)
    return render_to_response('city.html',  {'city': city, 'current_page': 'city'})
