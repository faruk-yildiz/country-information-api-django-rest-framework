from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from country.models import Country
from country.api.serializers import CountrySerializer

@api_view(['GET','POST'])
def country_list_create_api_view(request):
    if request.method=="GET":
        countries=Country.objects.all()
        serializer=CountrySerializer(countries,many=True)

        return Response(serializer.data)
    elif request.method=="POST":
        serializer=CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def country_detail_api_view(request,iso):
    try:
        country_instance=Country.objects.get(isoCode=iso)
    except Country.DoesNotExist:
        return Response({
            'error':404,
            'message':'Böyle bir ülke bulunamadı'

        },
        status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method=="GET":
        serializer=CountrySerializer(country_instance)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer=CountrySerializer(country_instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method=="DELETE":
        country_instance.delete()
        return Response(status.HTTP_204_NO_CONTENT)