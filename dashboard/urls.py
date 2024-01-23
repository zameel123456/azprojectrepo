from django.urls import path
from.import views
app_name='dashboard'

urlpatterns=[
    path('',views.indexhome,name="home"),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('newhomepage',views.newhomepage,name='newhomepage'),
    path('contact',views.contactus,name='contactus'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('seat/',views.seat,name='seat'),
    path('steering/',views.steering,name='steering'),
    path('subwoofer/',views.subwoofer,name='subwoofer'),
    path('alloys/',views.alloys,name='alloys'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cartpage,name='cart'),
    path('remove_from_cart/<int:product_id>',views.remove_from_cart,name='remove_from_cart'),
    path('logout/',views.logout,name='logout')
  
]