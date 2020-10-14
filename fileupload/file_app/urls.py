from django.conf.urls import url
from .views import FileView, FileSave
urlpatterns = [
    url(r'^identify/', FileView.as_view(), name='file-upload'),
    url(r'^train/', FileSave.as_view(), name='file-save'),

]