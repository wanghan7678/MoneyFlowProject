import api.views as vs
from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('topic/', vs.get_all_topics),
    path('topic/<int:topic_id>', vs.get_topic_detail),
    re_path(r'topic/add$', vs.add_topic),
    re_path(r'topic/update$', vs.edit_topic),
    re_path(r'topic/delete$', vs.delete_topic),
    path('section/<int:section_id>', vs.get_section),
    re_path('section/add$', vs.add_section),
    re_path(r'section/update$', vs.edit_section),
    re_path(r'section/delete$', vs.delete_section),
    path('page/<int:page_id>', vs.get_page),
    re_path(r'page/add$', vs.add_page),
    re_path(r'page/update$', vs.edit_page),
    re_path(r'page/delete$', vs.delete_page)
    ]