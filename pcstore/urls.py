"""
URL configuration for pcstore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from component import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("productlist/",views.getallproduct,name='productlist/'),
    path("addcustomer/",views.Addcustomer ,name='addcustomer/'),
    path("cartlist/",views.showcart ,name='cartlist/'),
    path("cartlist/delete/<int:id>",views.deletecart),
    path("cartlist/placeorder",views.showorderform,name="cartlist/placeorder"),
    path("login/",views.login,name="login/"),
    path("logout/",views.logout,name="logout/"),
    path('paymentsuccess/<int:order_id>/<str:payment_id>',views.paysucc,name='payementsuccess/'),
    path("productlist/addcart/<int:pid>",views.addcart,name='addcart'),




    path("cartlist/placeorder",views.showorderform,name="cartlist/placeorder"),
    path("index/",views.index,name="index/"),
    path("About/",views.About,name="About/"),






]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
