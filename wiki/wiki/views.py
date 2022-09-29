from django.shortcuts import render
from base.models import WikiTopic, WikiSection, WikiContent


def home(request):
    wiki_topics = WikiTopic.objects.all()
    context = {"topics": wiki_topics}
    return render(request, 'index.html', context)


def topic(request, topic_id):
    wiki_topic = WikiTopic.objects.get(id=topic_id)
    wiki_sections = WikiSection.objects.filter(topic_id=topic_id)
    context = {'topic': wiki_topic, 'sections': wiki_sections}
    return render(request, 'topic.html', context)
