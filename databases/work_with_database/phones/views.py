from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    objects = Phone.objects.all()
    devices = []
    for object in objects:
        devices.append({
            'name': object.name,
            'price': object.price,
            'slug': object.slug,
            'image': object.image,
        })
    sort = request.GET.get('sort')
    if sort == 'min_price':
        new_devices = sorted(devices, key=lambda x: x['price'])
    elif sort == 'max_price':
        new_devices = sorted(devices, key=lambda x: x['price'], reverse=True)
    else:
        new_devices = sorted(devices, key=lambda x: x['name'])
    context = {'devices': new_devices}
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
