from rest_framework import serializers

from first_app.models import Location


class LocationSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = ['city', 'country']