from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static
urlpatterns = [
    path("admin_1", views.admin_1, name="admin_1"),
    path("admin_2", views.admin_2, name="admin_2"),
    path("show_ord", views.show_ord, name="show_ord"),
    path("show_driver", views.show_driver, name="show_driver"),
    path("register_car_page", views.register_car_page, name="register_car_page"),
    path("service", views.service, name="service"),
    path("about", views.about, name="about"),
    path("booking", views.booking, name="booking"),
    path("car", views.car, name="car"),
    path("contact", views.contact, name="contact"),
    path("driver", views.driver, name="driver"),
    path("team", views.team, name="team"),
    path("testimonial", views.testimonial, name="testimonial"),
    path("Edit_car_details",views.Edit_car_details,name='Edit_car_details'),
    path("Edit_order_details",views.Edit_order_details,name='Edit_order_details'),
    path("update_car_details",views.update_car_details,name='update_car_details'),
    path("update_order_details",views.update_order_details,name='update_order_details'),
    path("delete_car_detail",views.delete_car_detail,name='delete_car_detail'),
    path("delete_order_detail",views.delete_order_detail,name='delete_order_detail'),
    path("Register_car",views.Register_car,name='Register_car'),
    path('', views.register, name='register'),
    path('login_view', views.login_view, name='login_view'),
    path('logout1', views.logout1, name='logout1'),
    path("index", views.index, name="index"),
    path("driver_regi_1", views.driver_regi_1, name="driver_regi_1"),
    path('order',views.order,name="order"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MDEIA_URL, document_root=settings.MDEIA_ROOT)
