from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.template import context
from .forms import notesforms

from .models import notes
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class deletenote(DeleteView):
    model=notes
    success_url='/notes'
    template_name='notes/notes_delete.html'

class updatenote(UpdateView):
    model=notes
    success_url='/notes'
    form_class=notesforms

class createnote(CreateView):
    model=notes
    success_url='/notes'
    form_class=notesforms

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
class listViews(LoginRequiredMixin,ListView):
    model=notes
    context_object_name='notes'
    template_name='notes/notes_list.html'
    login_url='/admin'

    def get_queryset(self):
        return self.request.user.notes.all()
class notedetail(DetailView):
    model=notes
    context_object_name='note'

