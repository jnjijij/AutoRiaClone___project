from django.http import JsonResponse
from django.views import View

from backend.listings.models import Ad


class AdPriceView(View):
    def get(self, request, *args, **kwargs):
        ads = Ad.objects.all()
        data = [
            {
                'id': ad.id,
                'price': ad.price,
            } for ad in ads
        ]
        return JsonResponse(data, safe=False)


class PriceConsumer:
    @classmethod
    def as_asgi(cls):
        pass