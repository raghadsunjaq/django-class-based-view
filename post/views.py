from django.shortcuts import render
from  .models import poost
from django.views.generic import ListView, DetailView, CreateView,DeleteView,UpdateView


class PoostList(ListView):
    model=poost
    context_object_name = 'all_post'
    ordering=['-created_at']
class PoostCreate():
    pass
class PoostDetail(DetailView):
    model=poost
class PoostUpdate():
    pass
class PoostDelete():
    pass