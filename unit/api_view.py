from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


class UnitAPIList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


class UnitAPIdetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer


@api_view(["GET", "DELETE"])
@permission_classes([IsAuthenticated])
def reservation_detail_api(request, id):
    if request.method == "GET":
        reservation_detail = get_object_or_404(UnitBook, user=request.user, id=id)
        data = BookingSerializer(reservation_detail, context={"request": request}).data
        return Response({"data": data})
    elif request.method == "DELETE":
        reservation = UnitBook.objects.get(user=request.user)
        reservation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
