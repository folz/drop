from django.shortcuts import render
from django.views.generic import CreateView

from .forms import ImageNoteForm
from .models import ImageNote

class ImageNoteView(CreateView):
    model = ImageNote
    fields = ['image', 'point']
