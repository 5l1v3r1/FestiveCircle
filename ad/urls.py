from django.urls import path
from .views import *

urlpatterns = [
    path('',main,name='main'),
    path('ad/post-an-ad/',post, name='postanadd'),
    path('search/q=ca_<category>&ct_<city>&min-pr_<min_price>&max-pr_<max_price>', search, name='search'),
    path('venue/<id>/',display,name='display'),
    path('edit/<id>/',edit,name='edit'),
    path('delete/<id>/',delete,name='delete'),
    path('user/my-ads/',ads,name='ads'),
    path('deactivate/<id>/',deactivate,name='deactivate'),
    path('activate/<id>/', activate , name='activate'),
    path('advanced-search/',adv_search,name='advanced_search'),
]