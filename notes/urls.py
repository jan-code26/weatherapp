from django.urls import path

from . import views

urlpatterns = [
    path('', views.listViews.as_view(),name="notes.list"),
    path('notes/<int:pk>',views.notedetail.as_view(),name="notes.details"),
    path('notes/<int:pk>/edit',views.updatenote.as_view(),name="notes.update"),
    path('notes/<int:pk>/delete',views.deletenote.as_view(),name="notes.delete"),
    path('notes/new', views.createnote.as_view(),name="notes.new"),
]