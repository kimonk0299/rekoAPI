from django.conf.urls import url
from .views import FileView, FileSave
urlpatterns = [
    url(r'^upload/', FileView.as_view(), name='file-upload'),
    url(r'^check/', FileSave.as_view(), name='file-save'),

]