from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def test(request):
    return render_to_response('content.html', locals(),
        context_instance = RequestContext(request))

def gallery_test(request):
    return render_to_response('gallery.html', locals(),
        context_instance = RequestContext(request))
