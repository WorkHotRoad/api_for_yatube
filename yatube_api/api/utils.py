from rest_framework import mixins, viewsets


class UpdateDeleteViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    pass
