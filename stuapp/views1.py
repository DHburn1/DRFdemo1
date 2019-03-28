import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from stuapp.models import Actor


class ActorListView(View):
    def get(self,request):

        actors = Actor.objects.all()

        actorList = []

    # aid = models.AutoField(primary_key=True)
    # aname = models.CharField(max_length=30)
    # age = models.PositiveIntegerField()
    # agender = models.CharField(max_length=1,choices=GENDER_ID)
    # birth_date = models.DateField()
    # photo = models.ImageField(default='',upload_to='actors/')

        for actor in actors:
            actorList.append({
                'aid':actor.aid,
                'aname':actor.aname,
                'age':actor.age,
                'agender':actor.agender,
                'birth_date':actor.birth_date,
                'photo':actor.photo if actor.photo else ''
            })

        return JsonResponse(actorList,safe = False)

    def post(self,request):
        json_bytes = request.body

        json_str = json_bytes.decode()

        actor_dict = json.loads(json_str)
        print(actor_dict)

        actor = Actor.objects.create(aname = actor_dict.get('aname'),
            age = actor_dict.get('age'),
            agender = actor_dict.get('agender'),
            birth_date = actor_dict.get('birth_date'))

        return JsonResponse({
            'aid':actor.aid,
            'aname':actor.aname,
            'age':actor.age,
            'agender':actor.agender,
            'birth_date':actor.birth_date,
            'photo':actor.photo.url if actor.photo else ''

        },status=201)


class ActorDetailListView(View):
    def get(self,request,pk):
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'aid':actor.aid,
            'aname':actor.aname,
            'age':actor.age,
            'agender':actor.agender,
            'birth_date':actor.birth_date,
            'photo':actor.photo.url if actor.photo else ''

        })

    def put(self,request,pk):
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        actor_dict = json.loads(json_str)

        actor.aname = actor_dict.get('aname')
        actor.age = actor_dict.get('age')
        actor.agender = actor_dict.get('agender')
        actor.save()

        return JsonResponse({
            'aid':actor.aid,
            'aname':actor.aname,
            'age':actor.age,
            'agender':actor.agender,
            'birth_date':actor.birth_date,
            'photo':actor.photo.url if actor.photo else ''
        })

    def delete(self,request,pk):
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        actor.delete()

        return HttpResponse({'message':'ok'},status=204)

