from django.shortcuts import render
from first_app.models import Topic, AccesRecord, Webpage


# Create your views here.
def index(request):
    webpages_list = AccesRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
#     my_dict = {'insert_content' : "Hello Iḿ from First_app" }
    return render(request, 'first_app/index.html', context=date_dict)
