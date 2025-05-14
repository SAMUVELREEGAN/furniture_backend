from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logo/', include('Logo.urls')),
    path('pro_banner/', include('Pro_banner.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/colors/', include('colorList.urls')),
    path('api/types/', include('type.urls')),
     path('api/weblinks/', include('weblink.urls')),
     path('api/sizes/', include('proSize.urls')),
      path('api/product/', include('product.urls'))

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
