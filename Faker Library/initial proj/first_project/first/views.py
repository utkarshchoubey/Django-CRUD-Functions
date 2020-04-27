from django.shortcuts import render
from django.http import HttpResponse
from first.models import Topic,AccessRecord,Webpage
from . import forms
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    #my_dic = {'insert_me' : "Hey I'm coming from first/index.html" }
    return render(request,'first/index.html',context=date_dict)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if(form.is_valid()):
            print("validation Success!")
            print("name -> " + form.cleaned_data['name'])
            print("email -> " + form.cleaned_data['email'])
            print("text ->  " + form.cleaned_data['text'])

    return render(request,'first/form_page.html' , {'form' : form})
