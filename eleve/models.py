# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models 

class Profil(models.Model):
    user = models.OneToOneField(User) 


class Specialities (models.Model):
    nom = models.CharField(max_length=100)
    def __str__ (self):
        return self.nom


class Classe (models.Model):
    annee = models.IntegerField()
    specialities=models.ForeignKey(Specialities)
    
    def __unicode__(self):
         return "{0} {1}".format(self.annee , self.specialities )





class Eleve (models.Model):
    classe = models.ForeignKey(Classe,default=0)
    matricule=models.CharField(max_length=50)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    grade=models.CharField(max_length=20)
    
    
    def __str__ (self):
        return self.nom

class Module (models.Model):
    nom=models.CharField(max_length=50)
    def __str__ (self):
        return self.nom

class Note (models.Model):
    eleve=models.ForeignKey(Eleve)
    module=models.ForeignKey(Module)
    test1=models.IntegerField(default=0)
    test2=models.IntegerField(default=0)
    examen=models.IntegerField(default=0)
    moyenne=models.IntegerField(default=0)
    mention=models.CharField(max_length=20,default=0)

    def __unicode__(self):
         return "{0} {1} {2}".format(self.eleve , self.moyenne,self.mention )


class Instructeur (models.Model):
    mat=models.CharField(max_length=20,default=0)
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    grade=models.CharField(max_length=20)
    module=models.ManyToManyField(Module)
    
    def __str__ (self):
        return self.nom



class Motif(models.Model):
     motif_abs=models.CharField(max_length=50)
     def __str__ (self):
        return self.motif_abs 



class Absence (models.Model):
     eleve=models.ForeignKey(Eleve,default='0')
     motif=models.ForeignKey(Motif)
     date_sortie = models.DateField(default='0')
     date_entree  =models.DateField(default='0')
     def __str__ (self):
         return "{0}  {1} ".format(self.eleve,self.motif )


