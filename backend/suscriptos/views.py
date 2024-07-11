from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Suscripto
from .serializers import SuscriptoSerializer

class SuscriptoViewSet(viewsets.ModelViewSet):
    queryset = Suscripto.objects.all()
    serializer_class = SuscriptoSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=400)
        if Suscripto.objects.filter(email=email).exists():
            return Response({'error': 'Email already subscribed'}, status=400)
        suscripto = Suscripto.objects.create(email=email)
        return Response({'mensasage': 'Subscription successful', 'email': suscripto.email, 'date_subscribed': suscripto.date_subscribed})

    @action(detail=False, methods=['post'])
    def subscribe(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=400)
        if Suscripto.objects.filter(email=email).exists():
            return Response({'error': 'Email already subscribed'}, status=400)
        suscripto = Suscripto.objects.create(email=email)
        return Response({'message': 'Subscription successful', 'email': suscripto.email, 'date_subscribed': suscripto.date_subscribed})

    @action(detail=False, methods=['get'], url_path='search')
    def search_by_email(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email query parameter is required'}, status=400)
        try:
            suscripto = Suscripto.objects.get(email=email)
            serializer = self.get_serializer(suscripto)
            return Response(serializer.data)
        except Suscripto.DoesNotExist:
            return Response({'email': None}, status = 200)