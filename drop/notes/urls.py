from django.conf.urls import patterns, url

from .views import ImageNoteView

urlpatterns = patterns('',
    url(r'^image$',
        ImageNoteView.as_view(),
        name='notes_image'),
)
