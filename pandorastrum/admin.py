from django.contrib import admin

from pandorastrum.models import (
    GamesModel,
    GamesDownloadLink,
    GameGenre,
    GameLore,
    GamesGallery,
    SystemRequirements,
    GamesTimeline,
    UpcomingGamesModel,
    PortfolioModel,
    Images,
    BlogModel,
    AuthorModel,
    BlogContentModel,
    AboutTeamImage,
    AboutModel,
    ThanksName
)








# Register your models here.

# games -----------------------------
class Gamestores(admin.TabularInline):
    model = GamesDownloadLink
    extra = 0

class Genre(admin.TabularInline):
    model = GameGenre
    extra = 0

class Lore(admin.TabularInline):
    model = GameLore
    extra = 0
    classes = ["collapse"]

class Gallery(admin.TabularInline):
    model = GamesGallery
    extra = 0
    classes = ["collapse"]

class Requirements(admin.TabularInline):
    model = SystemRequirements
    extra = 0
    classes = ["collapse"]

class Timeline (admin.TabularInline):
    model = GamesTimeline
    extra = 0
    classes = ['collapse']

@admin.register(GamesModel)
class GamesAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ["__str__", "is_slide_featured", "created", "updated", "thumbnail"]
    list_filter = ("released_on","game_title")
    fieldsets = (
        (None, {
            'fields': ("game_title", "game_short_description", "released_on")
        }),
        ('Compatability', {
            'fields': ((), ('pc', 'web', "android", "console"),
                            ("age_rating",),
                            ("single_player", "multiplayer", "current_version", "version_details"),
                       )
        }),
        ('Game Icons', {
            'fields': (("slide_image", "is_slide_featured"),('game_thumbnail', "thumbnail"))
        }),
        ('Read Only Info', {
            'classes': ('collapse',),
            'fields': ('slug', "created")
        }),
    )
    inlines = [Genre, Gamestores, Lore, Gallery, Requirements, Timeline]
    readonly_fields = ('slug', "created", "thumbnail")

@admin.register(UpcomingGamesModel)
class UpcomingAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = ["__str__", "is_active", "created", "updated",]
    list_filter = ("code_name",)
    fieldsets = (
        (None, {
            'fields': ("code_name", "is_active", "game_teaser_description", "game_img")
        }),
        ('Milestones', {
            'fields': ((), ("milestone_first_init", "milestone_second_alpha", "milestone_third_beta"))
        }),
        ('Read Only Info', {
            'classes': ('collapse',),
            'fields': ('slug', "created")
        }),
    )
    readonly_fields = ('slug', "created",)

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

class Team(admin.TabularInline):
    model = AboutTeamImage
    extra = 0

class Thanks(admin.TabularInline):
    model = ThanksName
    extra = 0
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
            'fields' : ("production_address",
                        "production_mobile",
                        "production_email" )
        }),
        ('Operation Address', {
            'fields': ("operation_address",
                       "operation_email")
        }),
        ('Read Only Info', {
            'classes': ('collapse',),
            'fields': ('slug', "created")
        }),
    )

    inlines = [Team, Thanks]
    readonly_fields = ('slug', "created")





admin.site.site_header = "PandorAstrum Administration"
admin.site.index_title = "Configurations"

