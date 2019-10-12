# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from eleve.froms import ConnexionForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

def connexion(request):
   if request.method =="POST":
        form=ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"] # Nous

            password = form.cleaned_data["password"] # ... et le mot

            user = authenticate(username=username,password=password) #Nous vérifions si les données sont correctes
        if user: 
            login(request, user) 

        else: 
             error = True
   else:
        form=ConnexionForm()
   return render(request,'eleve/user.html',locals())