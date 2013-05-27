from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")


#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
#from django.views import generic

#from home.models import  home

#class IndexView(generic.ListView):
    #template_name = 'home/index.html'
    #context_object_name = 'latest_home_list'

    #def get_queryset(self):
       # """Return the last five published polls."""
       # return home.objects.order_by('message')[:5]


#class DetailView(generic.DetailView):
   # model = home
   # template_name = 'home/detail.html'


#class ResultsView(generic.DetailView):
   # model = home
   # template_name = 'home/results.html'

#def message(request, home_id):

    # p = get_object_or_404(home, pk=home_id)
    
    # return HttpResponseRedirect(reverse('home:results', args=(p.id,)))
                    
