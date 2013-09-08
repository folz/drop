from base64 import b64decode
import binascii
import datetime
import json
import os

from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, View

from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D

from .forms import ImageNoteForm
from .models import ImageNote

class ImageNoteView(CreateView):
    model = ImageNote
    fields = ['user_id', 'image', 'point']

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ImageNoteView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        image_data = b64decode(form.cleaned_data['image'])
        self.object = form.save(commit=False)
        self.object.actual_image = ContentFile(image_data, "" + binascii.hexlify(os.urandom(16)) + str(datetime.datetime.now()) + ".jpg")
        self.object.save()
        return super(ImageNoteView, self).form_valid(form)

class NearbyNoteView(View):
    def get(self, request):
        #import rpdb2; rpdb2.start_embedded_debugger("password")
        lat = request.GET.get('lat')
        long = request.GET.get('long')
        
        pt = fromstr('POINT({} {})'.format(lat, long))
        qs = ImageNote.objects.filter(point__distance_lte=(pt, D(ft=150)))[:5]

        response_data = {}
        for note in qs:
            response_data[note.pk] = {
                'user_id': note.user_id,
                'point': {
                    'x': pt.x,
                    'y': pt.y
                },
                'image': note.actual_image.url
            }

        return HttpResponse(json.dumps([response_data]), content_type="application/json")
