from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	#-likes is descending order
	context_dict = {'categories' : category_list}
	# Return a rendered response to send to the client.
	# We make use of the shortcut function to make our lives easier.
	# Note that the first parameter is the template we wish to use.
	return render(request, 'rango/index.html', context_dict)

def about(request):
	return render(request, 'rango/about.html')