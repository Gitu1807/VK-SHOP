from django.urls import path 
from shopapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home',views.home),
    path('product',views.product),
    path('about',views.about),
    path('contact',views.contact),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout), 
    path('catfilter/<cv>',views.catfilter),     #{in there cv we can write any word}
    path('sort/<sv>',views.sortbyprice),
    path('pricefilter',views.pricefilter),
    path('search',views.search),
    path('productdetail/<pid>',views.productdetail),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('updateqty/<x>/<cid>',views.updateqty),
    path('remove/<cid>',views.remove),
    path('placeorder',views.placeorder),
    path('fetchorder',views.fetchorder),
    path('makepayment',views.makepayment),
    path('paymentsuccess',views.paymentsuccess),
    path('facebook',views.facebook),
    path('instagram',views.instagram),
    path('twitter',views.twitter),
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)