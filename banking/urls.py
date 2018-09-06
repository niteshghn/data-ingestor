from django.conf.urls import url

from banking import views

urlpatterns = [
    url('^transaction/$',views.save_transaction, name='transaction')
]