# bookmark/admin.py
from django.contrib import admin

from .models import Bookmark

admin.site.register(Bookmark)
# admin 사이트에 북마크 앱을 등록하는 명령어
