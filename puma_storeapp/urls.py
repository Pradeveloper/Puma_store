from django.urls import path
from puma_storeapp import views
from .views import pdetails
from puma_store import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.home),
    path('Brands/', views.Brands, name='brands'),
    path('pdetails/<int:pid>/', views.pdetails, name='pdetails'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('Register/', views.register),
    path('login/', views.ulogin),
    path('logout/', views.logout_view, name='logout'),
    path('catfilter/<int:cv>/', views.catfilter, name='catfilter'),
    path('sort/<sv>',views.sort),
    path('range/', views.range, name='range'),
    path('addtocart/<int:pid>/', views.addtocart, name='addtocart'),
    path('cart/', views.viewcart, name='viewcart'),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder/',views.placeorder),
    path('makepayment/',views.makepayment),
     ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
