from django.db import models
from django.utils.safestring import mark_safe
from pandorastrum.utility import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager
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
#================================================================================
# blog page ---------------------------------------------------------------------
#================================================================================
class AuthorModel(models.Model):
    author_name = models.CharField(max_length=200, blank=True, null=True)
    author_image = models.ImageField(upload_to="user", blank=True, null=True)
    def author_image_thumb(self):
        return mark_safe(u'<img src="%s" />' % (self.author_image.url))
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
    blog_description= models.TextField(blank=True, null=True)
    blog_author     = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, default='')
    is_featured     = models.BooleanField(default=False)
    blog_banner     = models.ImageField(upload_to="blogs", blank=True, null=True)
    def blogBanner(self):
        return mark_safe(u'<img src="%s" height="300" />' % (self.blog_banner.url))
    blogBanner.allow_tags = True
    blogBanner.short_description = 'Blog Banner'
    tags            = TaggableManager()
    slug            = models.SlugField(blank=True, null=True)
    updated         = models.DateTimeField(auto_now=True, auto_now_add=False)
    created         = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})

    def get_month_str(self):
        return self.published_on.strftime("%b %Y")

    def get_day(self):
        return self.published_on.strftime("%d")

    def get_date(self):
        return self.published_on.strftime("%d %b %Y")

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
    attach_banner_here = models.BooleanField(default=False)
    image           = models.ImageField(upload_to="blog", blank=True, null=True)
    image_size      = models.CharField(max_length=15, choices=SIZE_CHOICES, default='')
    def __str__(self):
        return str(self.pk)




def rl_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save, sender=GamesModel)
pre_save.connect(rl_pre_save, sender=AboutModel)
pre_save.connect(rl_pre_save, sender=BlogModel)
pre_save.connect(rl_pre_save, sender=AuthorModel)