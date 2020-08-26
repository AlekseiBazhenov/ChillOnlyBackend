from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from app.api.serializers import StationSerializer
from app.models import Station


class StationViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Station.objects.all()
    serializer_class = StationSerializer
