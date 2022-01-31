from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('products/', include('products.urls')),
]

if settings.DEBUG: # settings.py에 True이면
    # 미디어 URL로 시작하는 주소가 넘어오면, 2번째인자 경로에서 찾아서 반환
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar # debug_toolbar 사용
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
