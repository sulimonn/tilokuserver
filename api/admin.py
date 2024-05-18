from django.contrib import admin
from api.models import *


class SubchapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'parent', 'page')
    list_display_links = ('title',)
    list_filter = ('parent',)
    search_fields = ('title', 'description')
    list_per_page = 10
    exclude = ('url',)


class GroupItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'group',)
    list_display_links = ('title',)
    list_filter = ('group',)
    search_fields = ('title', 'description')
    list_per_page = 10
    exclude = ('url',)


class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'parent', 'page')
    list_display_links = ('title',)
    list_filter = ('parent',)
    search_fields = ('title', 'description')
    list_per_page = 10
    exclude = ('url',)


class Exercise1Admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'sub_chapter')
    list_display_links = ('title',)
    list_filter = ('sub_chapter',)
    search_fields = ('title', 'description')
    list_per_page = 10


admin.site.register(Group)
admin.site.register(GroupItem, GroupItemAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Subchapter, SubchapterAdmin)
admin.site.register(Exercise1, Exercise1Admin)
