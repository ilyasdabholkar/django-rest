from django.urls import path

from . import views


urlpatterns = [
    path('member/',views.getMembers),
    path('member/<int:id>',views.getMember)
]