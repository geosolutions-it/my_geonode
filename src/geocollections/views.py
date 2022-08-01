import json
import logging
import traceback

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import PermissionRequiredMixin

from dynamic_rest.viewsets import DynamicModelViewSet
from dynamic_rest.filters import DynamicFilterBackend, DynamicSortingFilter

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from geonode.base.api.pagination import GeoNodeApiPagination

from .models import Geocollection
from .serializers import GeocollectionSerializer
from .permissions import GeocollectionPermissionsFilter


logger = logging.getLogger(__name__)


class GeocollectionDetail(PermissionRequiredMixin, DetailView):
    model = Geocollection

    def has_permission(self):
        return self.request.user.has_perm('access_geocollection', self.get_object())


class GeocollectionViewSet(DynamicModelViewSet):
    """
    API endpoint that allows geocollections to be viewed or edited.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    filter_backends = [
        DynamicFilterBackend, DynamicSortingFilter,
        GeocollectionPermissionsFilter
    ]
    queryset = Geocollection.objects.all()
    serializer_class = GeocollectionSerializer
    pagination_class = GeoNodeApiPagination

