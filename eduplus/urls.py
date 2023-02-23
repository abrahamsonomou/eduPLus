from django.contrib import admin
from django.urls import path,include, re_path
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as ckeditor_views
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _ 

urlpatterns = i18n_patterns(
    ################# Admin ####################
    path('admin/', admin.site.urls),
    ################# End Admin ####################


    path('', include('core.urls')),

    # path(r'',include('core.urls')),
    # path('api/', include('api.urls')),
   
   
    ############ Authentification #######################
    # path('api-auth/', include('rest_framework.urls')),
    # # path('accounts/', include('users.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),


    ############ End Authentification #######################

    ####################### CKEditor ################################
    # CKEditor urls, don' user include to remove @staff_user_required!
    # path('upload/', ckeditor_views.upload, name='ckeditor_upload'),
    # path('browse/', ckeditor_views.browse, name='ckeditor_browse'),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    ####################### End CKEditor ################################

    ##################### rosetta pour la traduction ####################
    path('rosetta/', include('rosetta.urls')),
    ##################### End rosetta  ####################

)+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
    re_path(r'^rosetta/', include('rosetta.urls'))
    ]


