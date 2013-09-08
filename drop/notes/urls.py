from django.conf.urls import patterns, url

from .views import ImageNoteView, NearbyNoteView

urlpatterns = patterns('',
    url(r'^image$',
        ImageNoteView.as_view(),
        name='notes_image'),
    url(r'^nearby$',
        NearbyNoteView.as_view(),
        name='notes_nearby'),
)
