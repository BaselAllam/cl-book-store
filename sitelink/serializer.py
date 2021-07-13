from rest_framework import serializers
from sitelink.models import Link


class LinkSerializer(serializers.ModelSerializer):
    facebookLink = serializers.CharField(read_only = True)
    siteLink = serializers.CharField(read_only = True)




    class Meta:
        model = Link
        fields = '__all__'