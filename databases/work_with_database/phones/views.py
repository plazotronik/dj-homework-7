from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'min_price':
        devices = Phone.objects.order_by('price')
    elif sort == 'max_price':
        devices = Phone.objects.order_by('-price')
    else:
        devices = Phone.objects.order_by('name')
    context = {'devices': devices}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    device = Phone.objects.filter(slug=slug).__iter__().__next__()
    context = {
        'device':
            {
                'name': device.name,
                'price': device.price,
                'image': device.image,
                'release_date': device.release_date,
                'lte_exists': device.lte_exists,
            }
    }
    return render(request, template, context)
