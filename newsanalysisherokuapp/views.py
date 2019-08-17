# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'base.html', {'data': {}} )

def report(request):
    return render(request, 'report.html', {'data': {}})

def results(request):
    return render(request, 'report.html', {'data': {}})
