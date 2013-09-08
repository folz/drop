import floppyforms as forms


class ImageNoteForm(forms.Form):
    image = forms.ImageField()
    point = forms.gis.PointField()
