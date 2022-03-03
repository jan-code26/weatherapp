from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.listViews.as_view(),name="notes.list"),
    path('<int:pk>',views.notedetail.as_view(),name="notes.details"),
    path('<int:pk>/edit',views.updatenote.as_view(),name="notes.update"),
    path('<int:pk>/delete',views.deletenote.as_view(),name="notes.delete"),
    path('new', views.createnote.as_view(),name="notes.new"),
]