from rest_framework import serializers

from stuapp.models import Actor


class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('aid','aname','age','agender')
        read_only_fields = ('aid','aname')
        extra_kwargs = {
            'age':{'min_value':0,'required':False}
        }