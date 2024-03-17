from django.http import JsonResponse
from django.views import View
from .models import Ad

class AdListView(View):
    def get(self, request, *args, **kwargs):
        ads = Ad.objects.all()
        data = [
            {
                'id': ad.id,
                'title': ad.title,
                'description': ad.description,
                'price': ad.price,
                'is_active': ad.is_active
            } for ad in ads
        ]
        return JsonResponse(data, safe=False)

class AdDetailView(View):
    def get(self, request, ad_id, *args, **kwargs):
        ad = Ad.objects.get(id=ad_id)
        data = {
            'id': ad.id,
            'title': ad.title,
            'description': ad.description,
            'price': ad.price,
            'is_active': ad.is_active
        }
        return JsonResponse(data)

class AdCreateView(View):
    def post(self, request, *args, **kwargs):
        data = request.json()
        ad = Ad.objects.create(
            title=data['title'],
            description=data['description'],
            price=data['price'],
            is_active=data['is_active']
        )
        data = {
            'id': ad.id,
            'title': ad.title,
            'description': ad.description,
            'price': ad.price,
            'is_active': ad.is_active
        }
        return JsonResponse(data)

class AdUpdateView(View):
    def put(self, request, ad_id, *args, **kwargs):
        ad = Ad.objects.get(id=ad_id)
        data = request.json()
        ad.title = data['title']
        ad.description = data['description']
        ad.price = data['price']
        ad.is_active = data['is_active']
        ad.save()
        data = {
            'id': ad.id,
            'title': ad.title,
            'description': ad.description,
            'price': ad.price,
            'is_active': ad.is_active
        }
        return JsonResponse(data)

class AdDeleteView(View):
    def delete(self, request, ad_id, *args, **kwargs):
        ad = Ad.objects.get(id=ad_id)
        ad.delete()
        return JsonResponse({'message': 'Ad deleted successfully.'})