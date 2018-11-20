from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Ride
from .serializers import RideSerializer


class RideView(APIView):
    def get(self, request):
        rides = Ride.objects.all()
        serializer = RideSerializer(rides, many=True)
        return Response({"rides": serializer.data})

    # def post(self, request):
    #     serializer = RideSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         ride_saved = serializer.save()
    #     return Response({"message": f"ride from {ride_saved.origin} to {ride_saved.destination} successfully created"})
    def post(self, request):
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_BADREQUEST)

    def put(self, request, pk):
        saved_ride = get_object_or_404(Ride.objects.all(), pk=pk)
        data = request.data
        serializer = RideSerializer(instance=saved_ride, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            ride_saved = serializer.save()
            # return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': f'ride from {ride_saved.origin} updated'})
        # return Response(serializer.errors, status=status.HTTP_400_BAD_BADREQUEST)

    def delete(self, request, pk):
        ride_to_delete = get_object_or_404(Ride.objects.all(), pk=pk)
        ride_to_delete.delete()
        return Response({'message': f'Ride with id {pk} deleted'})


