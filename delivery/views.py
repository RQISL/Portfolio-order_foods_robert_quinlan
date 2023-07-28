import json
from django.shortcuts import render, redirect
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'aboutus.html')


class Order_Foods(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'order_foods.html')
