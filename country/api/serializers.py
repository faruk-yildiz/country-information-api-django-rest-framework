from rest_framework import serializers

from country.models import Country


class CountrySerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    isoCode=serializers.CharField()
    callingCode=serializers.CharField()
    flag=serializers.CharField()
    capital=serializers.CharField()
    population=serializers.IntegerField()


    def create(self, validated_data):
        return Country.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.isoCode=validated_data.get('isoCode',instance.isoCode)
        instance.callingCode=validated_data.get('callingCode',instance.callingCode)
        instance.flag=validated_data.get('flag',instance.flag)
        instance.capital=validated_data.get('capital',instance.capital)
        instance.population=validated_data.get('population',instance.population)
        instance.save()
        return instance