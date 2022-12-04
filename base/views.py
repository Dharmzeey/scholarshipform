from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import ProfileForm

def home(request):
  return render(request, 'base/index.html')

class CreateUser(CreateView):
  template_name = "base/form.html"
  success_url = reverse_lazy("home")
  form_class = ProfileForm
  
  def form_valid(self, form):
    if form.instance.attestation == False:
      form.add_error('attestation', "You have to click the attestation box")
      return self.render_to_response(self.get_context_data(form=form))
    messages.success(self.request, "Application submiteed successfully")
    return super(CreateUser, self).form_valid(form)
create_user = CreateUser.as_view()
