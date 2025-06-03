from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.admin import AdminSite
from book.forms import AuthAdminForm
from django.contrib.auth import views as auth_views

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
    path('api/enquiries/', include('enquirie.urls')),
    path('api/carousel/', include('carosel.urls')),
    path('api/', include('app.urls')),
    path('api/info/', include('contactinfo.urls')),
    path('api/reviews/', include('reviews.urls')),

    # Password reset URLs
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
