from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.admin import AdminSite
from book.forms import AuthAdminForm

class MyAdminSite(AdminSite):
    admin.site.login_form = AuthAdminForm
    admin.site.login_template = 'new/cus_login.html'
    admin.site.logout_template = 'new/logout.html'

my_admin_site = MyAdminSite()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logo/', include('Logo.urls')),
    path('pro_banner/', include('Pro_banner.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/colors/', include('colorList.urls')),
    path('api/types/', include('type.urls')),
    path('api/weblinks/', include('weblink.urls')),
    path('api/sizes/', include('proSize.urls')),
    path('api/product/', include('product.urls')),
    path('api/craft/', include('craft.urls')),
    path('api/enquiries/',include('enquirie.urls')),
    path('api/carousel/', include('carosel.urls')),
    path('api/', include('app.urls')),
    path('api/info/', include('contactinfo.urls')),
    path('api/reviews/', include('reviews.urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
