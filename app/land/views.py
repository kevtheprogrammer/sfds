from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
import json
from django.views.generic import ListView , DetailView ,View,TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import *
from account.models import Controller

class SoilDetailView(TemplateView):
    model = SoilNutrient
    template_name = 'admin/farmers/soil.html'
   
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # soilData = self.get_object()
        context["controllers"] = Controller.objects.filter(client=self.request.user)
        return context 



class SoilListView(CreateView):
    model = SoilNutrient

    # def get(self, request, *args, **kwargs) :
    #     return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs) :
        # get soil nutirent details form arduino
        # save details to database
        return super().get(request, *args, **kwargs)

