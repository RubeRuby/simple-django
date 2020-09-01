from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from hashids import Hashids

from sdh.shortener.models import Redirect

# Update before ID's reach 6 digits (likely never)
hashids = Hashids(min_length=5)

def generate_slug(id):
    return hashids.encode(id)


class ShortenView(View):
    def get(self, request):
        return render(request, 'shortener/shorten.html')

    def post(self, request):
        context = {}
        og_url = request.POST['url']
        if og_url:
            instance = Redirect(original_url=og_url)
            instance.save()

            # Generate shortened 'slug'
            hashid = generate_slug(instance.id)
            if (len(hashid) != 5):
                context['error'] = 'Max entries reached, please contact the admin' 
                return render(request, 'shortener/shorten.html', context=context, status=500)
            instance.slug = hashid
            instance.save()
            context['instance'] = instance

            return render(request, 'shortener/shortened.html', context=context, status=201)
        else: 
            context['error'] = 'URL cannot be empty' 
            return render(request, 'shortener/shorten.html', context=context, status=400)


def redirect_shortened(request, slug):
    instance = get_object_or_404(Redirect, slug=slug)
    return redirect(instance.original_url)


def list(request):
    context = {}
    context['list'] = Redirect.objects.all()
    return render(request, 'shortener/list.html', context=context, status=200)


def root(request):
    return render(request, 'shortener/root.html', status=200)