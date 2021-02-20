from django.urls import path
from pages.views import AboutView, IndexView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    #path(route, view, opt(kısayol ismi))

]