from django.urls import path
from . import views

# NameSpacing URL names
#------------------Problem------------------------
# The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?

#-----------------Solution------------------------
# For Each and every app add app_names for creating difference between ULR's

app_names = 'polls'
urlpatterns = [
    # /polls/
    path('',views.index,name='index'),
    # /polls/5/
    path('<int:question_id>/',views.detail,name='detail'),
    # /polls/5/results
    path('<int:question_id>/results/',views.results,name='results'),
    # /polls/5/vote
    path('<int:question_id>/vote/',views.vote,name='vote'),
]
