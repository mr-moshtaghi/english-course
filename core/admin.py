from django.contrib import admin

from core.models import Course, Video, Word, CourseUser, VideoUser, WordUser


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title']


class WordAdmin(admin.ModelAdmin):
    list_filter = ['type']
    list_display = ['english_word', 'translate', 'type']


class CourseUserAdmin(admin.ModelAdmin):
    list_display = ['course', 'user']


class VideoUserAdmin(admin.ModelAdmin):
    list_display = ['video', 'user']


class WordUserAdmin(admin.ModelAdmin):
    list_display = ['word', 'user']


admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(CourseUser, CourseUserAdmin)
admin.site.register(VideoUser, VideoUserAdmin)
admin.site.register(WordUser, WordUserAdmin)
