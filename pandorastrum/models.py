from django.db import models
from django.utils.safestring import mark_safe
from pandorastrum.utility import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager
# Create your models here.
#================================================================================
# Home page ---------------------------------------------------------------------
#================================================================================
class HomeModel(models.Model):
    home_page_name  = models.CharField(max_length=100, blank=True, null=True)
    facebook_link   = models.URLField(default='')
    twitter_link    = models.URLField(default='')
    twitch_link     = models.URLField(default='')
    youtube_link    = models.URLField(default='')
    patreon_link    = models.URLField(default='')
    event_date      = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    event_name      = models.CharField(max_length=100, blank=True, null=True)
    event_description = models.TextField(max_length=500, blank=True, null=True)
    event_image     = models.ImageField(upload_to="event", blank=True, null=True)
    slug            = models.SlugField(blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.home_page_name
    @property
    def title(self):
        return self.home_page_name
#================================================================================
# Game page ---------------------------------------------------------------------
#================================================================================
class GamesModel (models.Model):
    game_title      = models.CharField(max_length=50, blank=True, null=True)
    released_on     = models.DateField(auto_now=False, auto_now_add=False)
    BLEND_CHOICES   = (
        ("m--blend-gray", "m--blend-gray"),
        ("m--blend-green", "m--blend-green"),
        ("m--blend-red", "m--blend-red"),
        ("m--blend-blue", "m--blend-blue")
    )
    NAV_COLOR_CHOICES = (
        ("m--navbg-gray", "m--navbg-gray"),
        ("m--navbg-green", "m--navbg-green"),
        ("m--navbg-red", "m--navbg-red"),
        ("m--navbg-blue", "m--navbg-blue")
    )
    game_short_description = models.TextField(max_length=200, blank=True, null=True)
    game_thumbnail  = models.ImageField(upload_to="games")
    slide_image     = models.ImageField(upload_to="games", blank=True)
    is_slide_featured = models.BooleanField(default=False)
    slider_blend_mode = models.CharField(max_length=15, choices=BLEND_CHOICES, default='')
    slider_navigation_color = models.CharField(max_length=15, choices=NAV_COLOR_CHOICES, default='')
    def sliderImage(self):
        return mark_safe(u'<img src="%s" width="200" height="50"/>' % (self.slide_image.url))
    sliderImage.allow_tags = True
    sliderImage.short_description = 'Slider'
    def thumbnail(self):
        return mark_safe(u'<img src="%s" height="100"/>' % (self.game_thumbnail.url))
    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image'
    web             = models.BooleanField(default=False)
    pc              = models.BooleanField(default=False)
    android         = models.BooleanField(default=False)
    console         = models.BooleanField(default=False)
    single_player   = models.BooleanField(default=False)
    multiplayer     = models.BooleanField(default=False)
    age_rating      = models.IntegerField(blank=True, null=True)
    current_version = models.CharField(max_length=20,blank=True, null=True)
    version_details = models.TextField(blank=True, null=True)
    slug            = models.SlugField(blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True)
    def get_absolute_url(self):
        return reverse("game_detail", kwargs={"id": self.id})
    def __str__(self):
        return self.game_title
    @property
    def title(self):
        return self.game_title

class GamesDownloadLink(models.Model):
    related_to      = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    is_active       = models.BooleanField(default=False)
    STORE_CHOICES = (
        ('Play', 'Google PlayStore'),
        ('Win', 'Universal Windows AppStore'),
        ('FB', 'Facebook Gameroom'),
        ('Itch', 'Itch.IO'),
        ('Smsg', 'Samsung AppStore'),
        ('Amz', 'Amazon Store'),
    )
    store_name      = models.CharField(max_length=4, choices=STORE_CHOICES)
    link            = models.URLField(default='')
    def __str__(self):
        return self.store_name

class GameGenre(models.Model):
    related_to      = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    GENRE_CHOICES   = {
        ("---" , "---"),
        ("2d" , "2d"),
        ("Arcade" , "Arcade"),
        ("3d" , "3d"),
        ("Action" , "Action"),
        ("Hack N Slash" , "Hack N Slash"),
        ("Beat-em-up" , "Beat-em-up"),
        ("Platformer" , "Platformer"),
        ("Trivia" , "Trivia"),
        ("Puzzle" , "Puzzle"),
        ("Infinite Runner" , "Infinite Runner"),
        ("Adventure" , "Adventure"),
        ("3rd Person" , "3rd Person"),
        ("Shooting" , "Shooting"),
        ("FPS" , "FPS"),
        ("Sports" , "Sports"),
        ("RPG" , "RPG"),
        ("Strategy" , "Strategy"),
        ("Simulation" , "Simulation"),
        ("Racing" , "Racing"),
        ("Driving", "Driving"),
        ("Space" , "Space"),
        ("MMO" , "MMO"),
        ("MOBA" , "MOBA"),
    }
    game_genre      = models.CharField(max_length=20, choices=GENRE_CHOICES, default='')
    def __str__(self):
        return self.game_genre

class GameLore(models.Model):
    related_to      = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    topic_title     = models.CharField(max_length=100, blank=True, null=True)
    is_main         = models.BooleanField(default=False)
    topic           = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.topic_title

class GamesGallery (models.Model):
    related_to      = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    img_title       = models.CharField(max_length=50, blank=True, null=True)
    img             = models.ImageField(upload_to="gallery", blank=True, null=True)
    img_caption     = models.CharField(max_length=500)
    def __str__(self):
        return self.img_title

class SystemRequirements(models.Model):
    related_to      = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    SPEC_CHOICES    = (
        ("PC", "Computer"),
        ("ANDRIOD", "Android"),
        ("WEB", "Web"),
        ("OTHERS", "Others")
    )
    spec_for        = models.CharField(max_length=10, null=True, blank=True, choices=SPEC_CHOICES)
    is_active       = models.BooleanField(default=False)
    spec_details    = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.spec_for

class GamesTimeline(models.Model):
    related_to      = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    title           = models.CharField(max_length=100, blank=True, null=True)
    description     = models.TextField(max_length=500, blank=True, null=True)
    img             = models.ImageField(upload_to="games", blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return self.title

class UpcomingGamesModel(models.Model):
    code_name       = models.CharField(max_length=50, blank=True, null=True)
    is_active       = models.BooleanField(default=False)
    RATING_CHOICES  = (
        ("Teen", "Teen"),
        ("Everyone", "Everyone"),
        ("Mature", "Mature"),
        ("Adult", "Adult"),
    )
    BUSINESS_CHOICES = (
        ("Free To Play" , "Free To Play"),
        ("Demo/Purchase", "Demo/Purchase"),
        ("Online MMO", "Online MMO")
    )
    DEV_CHOICES     = (
        ("Idealization" , "Idealization"),
        ("Concept Art", "Concept Art"),
        ("Story Building", "Story Building"),
        ("Programming", "Programming"),
        ("3D Modelling", "3D Modeling"),
        ("2D Sketching", "2D Sketching"),
        ("Sound Mixing", "Sound Mixing"),
        ("Polishing", "Polishing"),
        ("Testing QA", "Testing QA"),
        ("UI Building", "UI Building")
    )
    game_img        = models.ImageField(upload_to="upcoming", blank=True, null=True)
    milestone_first_init = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    milestone_second_alpha = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    milestone_third_beta = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    game_teaser_description = models.TextField(max_length=500, blank=True, null=True)
    teaser_img_1    = models.ImageField(upload_to="upcoming", blank=True, null=True)
    teaser_img_2    = models.ImageField(upload_to="upcoming", blank=True, null=True)
    rated_for       = models.CharField(max_length=10, choices=RATING_CHOICES, default='')
    key_feature     = models.CharField(max_length=50, blank=True, null=True)
    business_model  = models.CharField(max_length=40, choices=BUSINESS_CHOICES, default='')
    dev_stage       = models.CharField(max_length=40, choices=DEV_CHOICES, default='')
    slug            = models.SlugField(blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.code_name
    @property
    def title(self):
        return self.code_name

#================================================================================
# portfolio page ----------------------------------------------------------------
#================================================================================
class PortfolioModel (models.Model):
    CATEGORY_CHOICES ={
        ("3D", "3d"),
        ("CONCEPT", "Concept"),
        ("UNITY", "Unity"),
        ("UNREAL", "Unreal"),
        ("EXPERIMENTAL", "Experimental")
    }
    project_name    = models.CharField(max_length=200, blank=True, null=True)
    category_type   = models.CharField(max_length=12, choices=CATEGORY_CHOICES)
    is_featured     = models.BooleanField(default=False)
    slug            = models.SlugField(blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.project_name
    @property
    def title(self):
        return self.project_name

class Images(models.Model):
    related_to      = models.ForeignKey(PortfolioModel, on_delete=models.CASCADE, blank=True, null=True, related_name="images")
    image_title     = models.CharField(max_length=200, blank=True, null=True)
    is_featured     = models.BooleanField(default=False)
    image           = models.ImageField(upload_to="portfolio", blank=True, null=True)
    def imageThumb(self):
        return mark_safe(u'<img src="%s" height="100" />' % (self.image.url))
    imageThumb.allow_tags = True
    image_caption   = models.TextField(max_length=500, blank=True, null=True)
    def get_absolute_url(self):
        return reverse("portfolio", kwargs={"id": self.id})
    def __str__(self):
        return self.image_title

#================================================================================
# blog page ---------------------------------------------------------------------
#================================================================================
class AuthorModel(models.Model):
    author_name     = models.CharField(max_length=200, blank=True, null=True)
    author_image    = models.ImageField(upload_to="user", blank=True, null=True)
    def author_image_thumb(self):
        return mark_safe(u'<img src="%s" width="80" height="80"/>' % (self.author_image.url))
    author_image_thumb.allow_tags = True
    author_image_thumb.short_description = 'Author Image'
    author_description = models.TextField(blank=True, null=True)
    slug            = models.SlugField(blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.author_name

    @property
    def title(self):
        return self.author_name

class BlogModel (models.Model):
    blog_title      = models.CharField(max_length=200, blank=True, null=True)
    published_on    = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    blog_author     = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, default='')
    is_featured     = models.BooleanField(default=False)
    is_freebies     = models.BooleanField(default=False)
    is_game_updates = models.BooleanField(default=False)
    is_tips         = models.BooleanField(default=False)
    is_dev_talks    = models.BooleanField(default=False)
    tags            = TaggableManager()
    slug            = models.SlugField(blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

    class Meta:
        ordering = ['-created', ]

    @property
    def title(self):
        return self.blog_title

class BlogContentModel(models.Model):
    SIZE_CHOICES    = (
        ("Left-Side", "Left-Side"),
        ("Right-Side", "Right-Side"),
        ("Full-Width", "Full-Width")
    )
    related_to      = models.ForeignKey(BlogModel, on_delete=models.CASCADE, blank=True, null=True)
    paragraph       = models.TextField(blank=True, null=True)
    is_main = models.BooleanField(default=False)
    image           = models.ImageField(upload_to="blog", blank=True, null=True)
    image_size      = models.CharField(max_length=15, choices=SIZE_CHOICES, default='')
    def __str__(self):
        return str(self.pk)

#================================================================================
# about us page -----------------------------------------------------------------
#================================================================================
class AboutModel(models.Model):
    generic_model       = models.CharField(max_length=100, blank=True, null=True)
    production_address  = models.TextField(max_length=500, blank=True, null=True)
    production_mobile   = models.CharField(max_length=20, blank=True, null=True)
    production_email    = models.EmailField(default='')
    production_country  = models.CharField(max_length=50, blank=True, null=True)
    operation_address   = models.TextField(max_length=500, blank=True, null=True)
    operation_email     = models.EmailField(default='')
    operation_country   = models.CharField(max_length=50, blank=True, null=True)
    services_1          = models.TextField(max_length=500, blank=True, null=True)
    services_2          = models.TextField(max_length=500, blank=True, null=True)
    services_3          = models.TextField(max_length=500, blank=True, null=True)
    services_4          = models.TextField(max_length=500, blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.generic_model
    @property
    def title(self):
        return self.generic_model

class AboutTeamImage(models.Model):
    related_to      = models.ForeignKey(AboutModel, on_delete=models.CASCADE, blank=True, null=True)
    name            = models.CharField(max_length=400)
    img             = models.ImageField(upload_to="about", blank=True, null=True)
    fb_url          = models.URLField(default='')
    tw_url          = models.URLField(default='')
    post_title      = models.CharField(max_length=100, blank=True, null=True)
    def __str__(self):
        return self.name

class ThanksName(models.Model):
    related_to      = models.ForeignKey(AboutModel, on_delete=models.CASCADE, blank=True, null=True)
    name_to_add     = models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name_to_add

# slug saves
def rl_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(rl_pre_save, sender=HomeModel)
pre_save.connect(rl_pre_save, sender=GamesModel)
pre_save.connect(rl_pre_save, sender=AboutModel)
pre_save.connect(rl_pre_save, sender=BlogModel)
pre_save.connect(rl_pre_save, sender=AuthorModel)
pre_save.connect(rl_pre_save, sender=PortfolioModel)
pre_save.connect(rl_pre_save, sender=UpcomingGamesModel)