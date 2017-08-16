from django.db import models
from django.utils.safestring import mark_safe
from pandorastrum.utility import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.utils.html import format_html
# Create your models here.
# games page
class GamesModel (models.Model):
    game_title      = models.CharField(max_length=200)
    released_on     = models.DateField(auto_now=False, auto_now_add=False)
    game_desc       = models.TextField(blank=True, null=True)
    age_rating      = models.IntegerField(blank=True)
    single_player   = models.BooleanField(default=False)
    multiplayer     = models.BooleanField(default=False)
    game_story = models.TextField(blank=True, null=True)

    game_thumbnail  = models.ImageField(upload_to="games")
    slide_image     = models.ImageField(upload_to="games", blank=True)
    def thumbnail(self):
        return mark_safe(u'<img src="%s" />' % (self.game_thumbnail.url))

    thumbnail.allow_tags = True
    thumbnail.short_description = 'Image'
    def slide(self):
        return mark_safe(u'<img src="%s" />' % (self.slide_image.url))

    # thumbnail.allow_tags = True
    slide.short_description = 'Slide'

    web             = models.BooleanField(default=False)
    pc              = models.BooleanField(default=False)
    android         = models.BooleanField(default=False)
    console         = models.BooleanField(default=False)

    slug            = models.SlugField(blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.game_title
    @property
    def title(self):
        return self.game_title

class GamesGallery (models.Model):
    related_to = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    img = models.ImageField(upload_to="gallery", blank=True, null=True)
    img_caption = models.CharField(max_length=500)

    def __str__(self):
        return self.gallery_name

class GamesDownloadLink(models.Model):
    related_to = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    STORE_CHOICES = (
        ('Play', 'Google PlayStore'),
        ('Win', 'Universal Windows AppStore'),
        ('FB', 'Facebook Gameroom'),
        ('Itch', 'Itch.IO'),
        ('Smsg', 'Samsung AppStore'),
        ('Amz', 'Amazon Store'),
    )
    store_name = models.CharField(max_length=4, choices=STORE_CHOICES)
    link = models.URLField(default='')

    def __str__(self):
        return self.store_name

class GamesDev(models.Model):
    related_to = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=400, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to="games", blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class GameRequirements(models.Model):
    related_to = models.ForeignKey(GamesModel, on_delete=models.CASCADE, blank=True, null=True)
    SPEC_CHOICES = (
        ("PC", "Computer"),
        ("ANDRIOD", "Android"),
        ("WEB", "Web"),
        ("OTHERS", "Others")
    )
    spec_for = models.CharField(max_length=10, null=True, blank=True, choices=SPEC_CHOICES)
    spec_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.spec_for

# about us page
class AboutModel(models.Model):
    generic_model = models.CharField(max_length=100, blank=True, null=True)

    pro_address1 = models.CharField(max_length=100, blank=True, null=True)
    pro_address2 = models.CharField(max_length=100, blank=True, null=True)
    pro_city = models.CharField(max_length=100, blank=True, null=True)
    pro_country = models.CharField(max_length=50, blank=True, null=True)
    pro_mobile = models.CharField(max_length=20, blank=True, null=True)
    pro_email = models.EmailField(default='')

    op_address1 = models.CharField(max_length=100, blank=True, null=True)
    op_address2 = models.CharField(max_length=100, blank=True, null=True)
    op_city = models.CharField(max_length=100, blank=True, null=True)
    op_country = models.CharField(max_length=50, blank=True, null=True)
    op_email = models.EmailField(default='')

    slug = models.SlugField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.generic_model

    @property
    def title(self):
        return self.generic_model

class AboutTeamImage(models.Model):
    related_to = models.ForeignKey(AboutModel, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=400)
    img = models.ImageField(upload_to="about", blank=True, null=True)
    fb_url = models.URLField(default='')
    tw_url = models.URLField(default='')
    post_title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class ThanksName(models.Model):
    related_to = models.ForeignKey(AboutModel, on_delete=models.CASCADE, blank=True, null=True)
    name_to_add = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name_to_add



class BlogModel(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title


def rl_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save, sender=GamesModel)
pre_save.connect(rl_pre_save, sender=AboutModel)