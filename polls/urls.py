from django.urls import include, path

from rest_framework import routers

from . import views
from . import viewsets

router = routers.DefaultRouter()
router.register(r"questions", viewsets.QuestionViewSet)
router.register(r"choices", viewsets.ChoiceViewSet)

#app_name = "polls"
urlpatterns = [
    #path("", views.IndexView.as_view(), name="index"),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
    path("", include(router.urls)),
]