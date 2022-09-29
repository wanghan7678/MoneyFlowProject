from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import WikiTopic, WikiSection, WikiContent
from .serializers import WikiTopicSerializer, WikiTopicWithSectionSerializer, WikiSectionSerializer, \
    WikiContentDomSerializer


@api_view(['GET'])
def get_all_topics(request):
    wiki_topics = WikiTopic.objects.all()
    serializer = WikiTopicSerializer(wiki_topics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_topic_detail(request, topic_id):
    wiki_topic = WikiTopic.objects.get(id=topic_id)
    serializer = WikiTopicWithSectionSerializer(wiki_topic, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_topic(request):
    data = request.data
    flag = WikiTopic.objects.create(**data)
    if flag:
        return Response({
            "status": 200,
            "msg": "Topic Add Success",
            "data": []
        })
    else:
        Response({
            "status": 201,
            "msg": "Topic Add Fail",
            "data": []
        })


@api_view(['PUT'])
def edit_topic(request):
    topic_id = request.data.pop('id')
    flag = WikiTopic.objects.filter(id=topic_id).update(**request.data)
    if not flag:
        return Response({
            "status": 201,
            "msg": "Topic Edit Fail",
            "data": []
        })
    return Response({
        "status": 200,
        "msg": "Topic Edit Success",
        "data": []
    })


@api_view(['DELETE'])
def delete_topic(request):
    topic_id = request.data.get('id')
    flag = WikiContent.objects.filter(id=topic_id).delete()
    if not flag[0]:
        return Response({
            "status": 201,
            "msg": "Topic Delete Fail",
            "data": []
        })
    return Response({
        "status": 200,
        "msg": "Topic Delete Success",
        "data": []
    })


@api_view(['GET'])
def get_section(request, section_id):
    wiki_section = WikiSection.objects.get(id=section_id)
    serializer = WikiSectionSerializer(wiki_section)
    return Response(serializer.data)


@api_view(['POST'])
def add_section(request):
    data = request.data
    flag = WikiSection.objects.create(**data)
    if flag:
        return Response({
            "status": 200,
            "msg": "Section Add Success",
            "data": []
        })
    else:
        Response({
            "status": 201,
            "msg": "Section Add Fail",
            "data": []
        })


@api_view(['PUT'])
def edit_section(request):
    section_id = request.data.pop('id')
    flag = WikiSection.objects.filter(id=section_id).update(**request.data)
    if not flag:
        return Response({
            "status": 201,
            "msg": "Section Edit Fail",
            "data": []
        })
    return Response({
        "status": 200,
        "msg": "Section Edit Success",
        "data": []
    })


@api_view(['DELETE'])
def delete_section(request):
    section_id = request.data.get('id')
    flag = WikiContent.objects.filter(id=section_id).delete()
    if not flag[0]:
        return Response({
            "status": 201,
            "msg": "Section Delete Fail",
            "data": []
        })
    return Response({
        "status": 200,
        "msg": "Section Delete Success",
        "data": []
    })


@api_view(['GET'])
def get_page(request, page_id):
    wiki_content = WikiContent.objects.get(id=page_id)
    serializer = WikiContentDomSerializer(wiki_content)
    return Response(serializer.data)


@api_view(['POST'])
def add_page(request):
    data = request.data
    flag = WikiContent.objects.create(**data)
    if flag:
        return Response({
            "status": 200,
            "msg": "Page add success",
            "data": []
        })
    else:
        return Response({
            "status": 201,
            "msg": "Page add fail",
            "data": []
        })


@api_view(['PUT'])
def edit_page(request):
    page_id = request.data.pop('id')
    flag = WikiContent.objects.filter(id=page_id).update(**request.data)
    if not flag:
        return Response({
            "status": 201,
            "msg": "Page Edit Fail",
            "data": []
        })
    return Response({
        "status": 200,
        "msg": "Page Edit Success",
        "data": []
    })


@api_view(["DELETE"])
def delete_page(request):
    page_id = request.data.get('id')
    flag = WikiContent.objects.filter(id=page_id).delete()
    if not flag[0]:
        return Response({
            "status": 201,
            "msg": "Page Delete Fail",
            "data": []
        })
    return Response({
        "status": 200,
        "msg": "Page Delete Success",
        "data": []
    })
