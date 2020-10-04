from rest_framework.views import APIView
from rest_framework.authentication import (
    TokenAuthentication, SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Sum
from swap_analysis.apps.swap.serializers import SwapSerializer, StatSerializer
from swap_analysis.apps.swap.models import Swap


class CreateSwap(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Swap.objects.all()
    serializer_class = SwapSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TotalEnergy(generics.GenericAPIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = StatSerializer

    def get(self, request):
        serialized = self.get_serializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        date = serialized.data['date']
        total = Swap.objects.filter(created_at=date).aggregate(
            energy_sum=Sum('used_energy'))

        day_total = total['energy_sum'] or 0

        return Response({'date': date, 'used_energy': day_total})


class TotalDistance(generics.GenericAPIView):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, )
    serializer_class = StatSerializer

    def get(self, request):
        serialized = self.get_serializer(data=request.data)
        serialized.is_valid(raise_exception=True)

        date = serialized.data['date']
        total = Swap.objects.filter(created_at=date).aggregate(
            distance_sum=Sum('driven_distance'))

        day_total = total['distance_sum'] or 0

        return Response({'date': date, 'driven_distance': day_total})
