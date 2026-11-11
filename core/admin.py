from django.contrib import admin
from .models import Category, Project, Skill, Experience, Service, ContactMessage ,Achievement
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type', 'order')
    list_filter = ('skill_type',)
    search_fields = ('name', 'description')    


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'institution', 'kind', 'period', 'order')
    list_filter = ('kind',)
    list_editable = ('order',)   # change the order directly from the list page    


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # 'featured' hata diya hai, ab sirf wahi fields hain jo model me hain
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'description', 'tech_stack')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'kind', 'issuer', 'date_text', 'order')
    list_filter = ('kind',)
    list_editable = ('order',)   # change the order directly from the list page
    search_fields = ('title', 'issuer')    

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order')
    list_editable = ('order',)   # change the order directly from the list page