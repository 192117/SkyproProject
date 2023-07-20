from django.contrib import admin

from resumes.models import Resume


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):

    list_display = ('title', 'grade', 'experience', 'specialty', 'status')
    list_filter = ('title', 'grade', 'experience', 'specialty', 'status')
    search_fields = ('title', 'grade', 'experience', 'specialty', 'status')
