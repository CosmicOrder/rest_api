from django.core.exceptions import ValidationError
from django.http import HttpResponseNotFound, HttpResponseBadRequest, HttpResponseServerError
from rest_framework import generics

from .models import SomeObject
from .serializers import SomeObjectListSerializer, SomeObjectRetrieveSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST


class SomeObjectListAPIView(generics.ListAPIView):
    queryset = SomeObject.objects.all()
    serializer_class = SomeObjectListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if name := self.request.query_params.get('name'):
            print(name)
            return queryset.filter(name__icontains=name)
        return queryset


class SomeObjectRetrieveAPIView(generics.RetrieveAPIView):
    queryset = SomeObject.objects.all()
    serializer_class = SomeObjectRetrieveSerializer

    def get(self, request, *args, **kwargs):
        try:
            if self.kwargs['pk'] == '0':
                queryset = super(SomeObjectRetrieveAPIView, self).get_queryset()
                serializer = self.serializer_class(queryset, many=True)
                return Response(serializer.data)
            elif not self.kwargs['pk'].isdigit():
                if self.kwargs['pk'] in '(%^:*':
                    raise Exception
                return BadRequest(request, ValueError)
            elif self.get_queryset().filter(id=int(self.kwargs['pk'])).count() == 0:
                return pageNotFound(request, ValueError)

            return super().get(request, *args, **kwargs)
        except Exception as e:
            return InternalServerError(request, e)


def BadRequest(request, exception):
    return HttpResponseBadRequest('<h1>id задан как не цифра</h1>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Объект не существует</h1>')


def InternalServerError(request, exception):
    return HttpResponseServerError('<h1>Возникла иная ошибка</h1>')
