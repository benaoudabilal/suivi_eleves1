# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from eleve.models import Eleve,Module,Note,Instructeur,Motif,Absence,Classe,Specialities 
class EleveAdmin (admin.ModelAdmin):
    list_display= ('matricule','nom', 'prenom', 'grade')
class AbsenceAdmin (admin.ModelAdmin):
    list_display= ('eleve','motif',)

admin.site.register(Note)
admin.site.register(Eleve,EleveAdmin)
admin.site.register(Module)
admin.site.register(Instructeur)
admin.site.register(Absence,AbsenceAdmin)
admin.site.register(Motif)
admin.site.register(Classe)
admin.site.register(Specialities)