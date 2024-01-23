from django.urls import path
from.import views
app_name='seller'
urlpatterns=[
    path('',views.seller_login,name='seller_login'),
    path('seller_dashboard',views.seller_dashboard,name='sdashboard'),
    path('addpdt/',views.addpdt,name='addpdt'),
    path('pdt_update/<int:pid>',views.pdt_update,name='pdt_update'),
    path('pdt_delete/<int:pid>',views.pdt_delete,name='pdt_delete')
]