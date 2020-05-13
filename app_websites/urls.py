from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('assets/', views.assets_page, name="assets-page"),
    path('partlists/', views.partlists_page, name="partlists-page"),
    path('partlists/<partlist_path>', views.partlist_page, name="partlist-page"),
    path('<brand_path>/', views.brand_page, name="brand-page"),
    path('<brand_path>/partlists', views.brand_partlists_page, name="brand-partlists-page"),
    path('<brand_path>/<series_path>/', views.series_page, name="series-page"),
    path('<brand_path>/<series_path>/<model_path>/', views.model_page, name="model-page"),
    path('<brand_path>/<series_path>/<model_path>/<machine_path>', views.machine_page, name="machine-page"),
]

