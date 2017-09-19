from django.shortcuts import render, redirect
from rutinas.models import Instructor, Rutina, Sexo, Tipo
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.template import loader
from django.http import HttpResponse, request


# Create your views here.


class InstructorListView(ListView):
    model = Instructor


class RutinaListView(ListView):
    model = Rutina

    # filter for instructor and sex

    def get_queryset(self):
        inst = Rutina.objects.filter(sexo=self.kwargs['pk1'], instructor=self.kwargs['pk'])
        return inst


class SexoListView(ListView):
    model = Sexo

    # Filter for sex and gets pk
    def get_context_data(self, **kwargs):
        data = Sexo.objects.filter(rutina=self.kwargs['pk'])
        context = {
            'datas': data,
            'pk': self.kwargs['pk']
        }

        return context



class TipoListView(ListView):
    model = Tipo

    # Filter for tipo and gets pk
    def get_context_data(self, **kwargs):
        data = Tipo.objects.filter(rutina=self.kwargs['pk'])
        context = {
            'datas': data,
            'pk': self.kwargs['pk'],
            'pk1': self.kwargs['pk1']
        }

        return context