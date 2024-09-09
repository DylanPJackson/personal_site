from django.contrib import admin

from .models import *


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


class PursuitInLine(admin.TabularInline):
    model = Pursuit
    extra = 0


class PursuitTypeAdmin(admin.ModelAdmin):
    inlines = [PursuitInLine]


class BlogPostInLine(admin.TabularInline):
    model = BlogPost
    extra = 0

class LinkInLine(admin.TabularInline):
    model = Link
    extra = 0

class PursuitAdmin(admin.ModelAdmin):
    inlines = [BlogPostInLine, LinkInLine]

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Button)
admin.site.register(Icon)
admin.site.register(NavBar, NavBarAdmin)
admin.site.register(NavSection)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Experience)
admin.site.register(Pursuit, PursuitAdmin)
admin.site.register(PursuitType, PursuitTypeAdmin)
admin.site.register(BlogPost)
admin.site.register(Link)
