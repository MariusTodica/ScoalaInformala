from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('locations/', include('first_app.urls')),
    path('companies/', include('first_app1.urls')),
    path('profile/', include('userprofile.urls')),
    path('api/', include('myapi.urls'))

]