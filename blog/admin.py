from django.contrib import admin
from .models import Post
from .models import CV
from .models import Education
from .models import Work

class WorkValueInline(admin.TabularInline):
    model = Work
    extra = 1

class EducationValueInline(admin.TabularInline):
    model=Education
    extra=1

class CVAdmin(admin.ModelAdmin):
    inlines = [WorkValueInline,EducationValueInline]


admin.site.register(Post)
admin.site.register(Education)
admin.site.register(Work)
admin.site.register(CV, CVAdmin)
