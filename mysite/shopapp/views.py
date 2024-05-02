from django.http import HttpResponse
from django.shortcuts import render

def shop_index(reqest):
    return HttpResponse('Hello World!!!')
