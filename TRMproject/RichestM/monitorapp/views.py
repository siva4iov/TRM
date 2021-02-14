import os

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import *
import datetime
from random import sample


def round(num):
    num = str(num)[:-1]
    num += '0'
    return int(num)


def index(request, country=''):
    if Person.objects.filter(citizenship__slug=country):
        persons = Person.objects.filter(citizenship__slug=country)[:10]
    else:
        if not country:
            persons = Person.objects.all()[:10]
        else:
            return HttpResponseNotFound()
    people = []
    max_whealth = 200000000000
    today = datetime.date.today()
    prices = []
    num = 0
    for person in persons:
        born = person.dob
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        num += 1
        people.append({
            'id': person.id, 'name': person.name, 'fortune': person.fortune, 'desc': person.short_description,
            'img': person.miniature, 'age': age, 'wealth': int((person.fortune/max_whealth)*100),
            'num': num, 'slug': person.slug
        })
        seq = {
            'air': person.air, 'cocain': person.cocain, 'doshirak': person.doshirak, 'falcon': person.falcon,
            'iphone': person.iphone, 'janitor': person.janitor, 'krepost': person.krepost,
            'palace': person.palace, 'lenin': person.lenin, 'tesla': person.tesla, 'weed': person.weed
        }
        keys = sample(list(seq), 3)
        di = {}
        for k in keys:
            di[k] = round(seq[k])
        prices.append(di)
        di = {}
        people[-1]['prices'] = prices[-1]
    return render(request, 'index.html', {'people': people})


def personpage(request, name):
    person = Person.objects.get(slug=name)
    today = datetime.date.today()
    born = person.dob
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    industries = person.industry.all()
    photos = person.photos_set.all()
    context = {
        'person': person, 'age': age, 'fortune': person.fortune//1000000000,
        'industries': industries, 'photos': photos,
    }
    if request.method == 'POST':
        zp = int(request.POST.get('zp'))
        if zp >= 500000:
            context['zp'] = 9
        else:
            months = person.rub//zp
            zp = round(months//12)
            context['zp'] = zp

    return render(request, 'person.html', context)


def teampage(request):
    return render(request, 'team.html', )
