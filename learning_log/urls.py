from django.contrib import admin
from django.urls import path, include
app_name = 'learning_logs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls'))
]
