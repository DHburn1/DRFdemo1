from rest_framework import serializers
from stuapp.models import Actor, Movie


class ActorSerializer(serializers.Serializer):
    """演员序列化器"""
    GENDER_ID = (
        ('0', '男'),
        ('1', '女')
    )
    aid = serializers.IntegerField(label='编号',read_only=True)
    aname = serializers.CharField(label='姓名',max_length=30)
    age = serializers.IntegerField(label='年龄',required=False)
    agender = serializers.ChoiceField(choices=GENDER_ID,label='性别',required=False)
    birth_date = serializers.DateField(label='出生年月',required=False)
    photo = serializers.ImageField(label='头像',required=False)

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.aid = validated_data.get('aid',instance.aid)
        instance.age = validated_data.get('age',instance.age)
        instance.aname = validated_data.get('aname',instance.aname)
        instance.agender = validated_data.get('agender',instance.agender)
        instance.birth_date = validated_data.get('birth_date',instance.birth_date)
        instance.photo = validated_data.get('photo',instance.photo)
        instance.save()

        return instance

class MovieSerializer(serializers.Serializer):
    mid = serializers.IntegerField(label='影片编号',read_only=True)
    mname = serializers.CharField(label='影片名称',max_length=30)
    m_pub_date = serializers.DateField(label='上映日期',required=False)
    mread = serializers.IntegerField(label='阅读量')
    mcomment = serializers.CharField(label='评论',max_length=300,required=False,allow_null=True)
    mimage = serializers.ImageField(label='图片',required=False)
    # actors = serializers.PrimaryKeyRelatedField(label='演员',read_only=True)
    actors_id = serializers.IntegerField()

    def create(self,validated_data):
        print(validated_data)
        instance = Movie.objects.create(**validated_data)
        return instance