from django.contrib import admin

from .models import HomePage, Button, Icon, NavBar, NavSection, Company, Experience, Passion, Project


class ButtonInline(admin.TabularInline):
    model = Button
    extra = 0


class IconInline(admin.TabularInline):
    model = Icon
    extra = 0


class HomePageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["headline"]}),
        (None, {"fields": ["subtitle_1"]}),
        (None, {"fields": ["subtitle_2"]}),
        (None, {"fields": ["picture_path"]})
    ]
    inlines = [ButtonInline, IconInline]


class NavSectionInLine(admin.TabularInline):
    model = NavSection
    extra = 0


class NavBarAdmin(admin.ModelAdmin):
    inlines = [NavSectionInLine]


class ExperienceInLine(admin.TabularInline):
    model = Experience
    extra = 0


class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["logo_picture_path"]}),
        (None, {"fields": ["name"]})
    ]
    inlines = [ExperienceInLine]


class PassionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["background_picture_path"]}),
        (None, {"fields": ["headline"]}),
        (None, {"fields": ["label"]}),
        (None, {"fields": ["description"]}),
    ]


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["thumbnail_picture_path"]}),
        (None, {"fields": ["title"]}),
        (None, {"fields": ["label"]}),
        (None, {"fields": ["description"]}),
    ]


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Button)
admin.site.register(Icon)
admin.site.register(NavBar, NavBarAdmin)
admin.site.register(NavSection)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Experience)
admin.site.register(Passion, PassionAdmin)
admin.site.register(Project, ProjectAdmin)
