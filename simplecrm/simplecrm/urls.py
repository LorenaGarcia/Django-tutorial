from django.contrib import admin
from django.urls import path
from crmapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'accounts', views.AccountAPIView.as_view(), name='account-list'),
    path(r'contacts', views.ContactAPIView.as_view(), name='contact-list'),
    path(r'activities', views.ActivityAPIView.as_view(), name='activity-list'),
    path(r'activitystatuses', views.ActivityStatusAPIView.as_view(), name='activity-status-list'),
    path(r'contactsources', views.ContactSourceAPIView.as_view(), name='contact-source-list'),
    path(r'contactstatuses', views.ContactStatusAPIView.as_view(), name='contact-status-list')
]
