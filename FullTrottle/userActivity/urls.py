from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_all_users$', views.UserView.as_view({'get':'getAllUsers'})),
    url(r'^get_user$', views.UserView.as_view({'get':'getUserDetail'})),
    url(r'^create_user$', views.UserView.as_view({'post': 'createUser'})),
    url(r'^get_user_activity$', views.UserActivityView.as_view({'get': 'getUserAcivity'})),
    url(r'^create_user_activity$', views.UserActivityView.as_view({'post': 'createUserActivity'})),
    url(r'^get_user_detail_activity$', views.UserAndActivityView.as_view({'get': 'getUserAndActivity'})),
    url(r'^delete_user$', views.UserAndActivityView.as_view({'delete': 'deleteUserAndActivity'})),
]