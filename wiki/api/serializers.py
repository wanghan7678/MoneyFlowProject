from rest_framework import serializers
from base.models import WikiTopic, WikiSection, WikiContent
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff')


class WikiTopicSerializer(serializers.ModelSerializer):
    users = UserSerializer(source='creator')

    class Meta:
        model = WikiTopic
        fields = ('id', 'name', 'description', 'created', 'updated', 'users')


class WikiContentSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='author')

    class Meta:
        model = WikiContent
        fields = ('id', 'updated', 'created', 'user', 'section_id')


class WikiContentDomSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='author')

    class Meta:
        model = WikiContent
        fields = ('id', 'dom', 'updated', 'created', 'user', 'section_id')


class WikiSectionSerializer(serializers.ModelSerializer):
    users = UserSerializer(source='author')
    pages = WikiContentSerializer(many=True)

    class Meta:
        model = WikiSection
        fields = ('id', 'title', 'views', 'created', 'updated', 'topic_id', 'users', 'pages')


class WikiTopicWithSectionSerializer(serializers.ModelSerializer):
    sections = WikiSectionSerializer(many=True)
    users = UserSerializer(source='creator')

    class Meta:
        model = WikiTopic
        fields = ('id', 'name', 'description', 'created', 'updated', 'sections', 'users')
