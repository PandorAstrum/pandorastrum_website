from django.contrib import admin

from pandorastrum.models import (
    GameRequirements,
    GamesDev,
    GamesDownloadLink,
    GamesGallery,
    GamesModel,
    AboutTeamImage,
    AboutModel,
    ThanksName,
    BlogModel,
    AuthorModel,
    BlogContentModel,
    PortfolioModel,
    Images
)
class Requirements(admin.TabularInline):
    model = GameRequirements
    extra = 1
    classes = ["collapse"]

class Dev (admin.TabularInline):
    model = GamesDev
    extra = 1
    classes = ['collapse']

class Download(admin.TabularInline):
    model = GamesDownloadLink
    extra = 1
    classes = ['collapse']

class Gallery(admin.TabularInline):
    model = GamesGallery
    extra = 1
    classes = ["collapse"]

# Register your models here.
@admin.register(GamesModel)
class GamesAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ["__str__", "created", "updated", "thumbnail"]
    list_filter = ('released_on',"game_title")
    fieldsets = (
        (None, {
            'fields': ('game_title', "game_desc", "game_story", "released_on")
        }),
        ('Compatability', {
            'fields': (('single_player', 'multiplayer'), ("age_rating",), ('pc', 'web', "android", "console"))
        }),
        ('Slide and Thumb', {
            'classes': ('collapse',),
            'fields': (('game_thumbnail', "thumbnail"),("slide_image", "slide"))
        }),
        ('Read Only Info', {
            'classes': ('collapse',),
            'fields': ('slug', "created")
        }),
    )

    inlines = [Download, Requirements, Gallery, Dev]
    readonly_fields = ('slug', "created", "thumbnail", "slide")

class Team(admin.TabularInline):
    model = AboutTeamImage
    extra = 1

class Thanks(admin.TabularInline):
    model = ThanksName
    extra = 1
    classes = ["collapse"]

@admin.register(AboutModel)
class AboutAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ["__str__", "created", "updated"]
    list_filter = ('updated', "generic_model")
    fieldsets = (
        (None, {
            'fields': ('generic_model', )
        }),
        ('Production Studio Address', {
            'fields' : ("pro_address1",
                        "pro_address2",
                        "pro_city",
                        "pro_country",
                        "pro_mobile",
                        "pro_email" )
        }),
        ('Operation Address', {
            'fields': ("op_address1",
                       "op_address2",
                       "op_city",
                       "op_country",
                       "op_email")
        }),
        ('Read Only Info', {
            'classes': ('collapse',),
            'fields': ('slug', "created")
        }),
    )

    inlines = [Team, Thanks]
    readonly_fields = ('slug', "created")

# portfolio -------------------------
class Image(admin.TabularInline):
    model = Images
    extra = 0

@admin.register(PortfolioModel)
class PortfolioAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ["__str__", "category_type", "created", "updated"]
    list_filter = ("category_type","updated",)
    fieldsets = (
        (None, {
            'fields': ((), ("project_name", "category_type"))
        }),
        ('Read Only Info', {
            'classes': ('collapse',),
            'fields': ('slug', "created")
        }),
    )

    inlines = [Image]
    readonly_fields = ('slug', "created",)

# blog ----------------------------------
class BlogContent(admin.TabularInline):
    model = BlogContentModel
    extra = 0

@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ["__str__", "is_featured" ,"created", "updated"]
    list_editable = ('is_featured',)
    list_filter = ('updated',)
    fieldsets = (
        (None, {
            'fields': (("is_featured"),('blog_title', "published_on", "blog_author"))
        }),
        ('Blog Details', {
            'fields': (('blog_description', "blog_banner"), ("blogBanner",))
        }),
        ('Tags', {
            'fields': ("tags",)
        }),
        ('Read Only Info', {
            'classes': ('collapse',),
            'fields': ('slug', "created")
        }),
    )

    inlines = [BlogContent]
    readonly_fields = ('slug', "created", "blogBanner")

@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ["__str__", "created", "updated"]
    list_filter = ('updated', 'author_name')
    fieldsets = (
        (None, {
            'fields': ('author_name', "author_description", "author_image", "author_image_thumb")
        }),
        ('Read Only Info', {
            'classes': ('collapse',),
            'fields': ('slug', "created")
        }),
    )

    readonly_fields = ('slug', "created", "author_image_thumb")

admin.site.site_header = "PandorAstrum Administration"
admin.site.index_title = "Configurations"

