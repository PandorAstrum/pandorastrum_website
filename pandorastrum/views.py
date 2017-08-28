import datetime
from functools import reduce

from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView

from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from urllib.parse import quote_plus
import operator
from django.db.models import Q
from pandorastrum.models import (
    GamesModel,
    GamesDownloadLink,
    SystemRequirements,
    GameGenre,
    GameLore,
    GamesGallery,
    GamesTimeline,
    UpcomingGamesModel,
    AboutModel,
    AboutTeamImage,
    ThanksName,
    BlogModel,
    BlogContentModel,
    PortfolioModel,
    Images
)
# Redirection of root url
def redirect_root(request):
    return redirect("/home/")

# Create your views here.
def home_pageView(request):
    # queryset =
    context = {

    }
    return render(request, "index.html", context)
# gamebox block ---------------------------------------------------------------------------
def game_pageView(request):
    queryset = GamesModel.objects.all().order_by("-created")
    upcoming = UpcomingGamesModel.objects.filter(is_active=True)
    context = {
        "games" : queryset,
        "upcoming" : upcoming
    }
    return render(request, "games.html", context)

def game_detailView(request, id, **kwargs):
    instance = get_object_or_404(GamesModel, id=id)
    game_stores = GamesDownloadLink.objects.filter(related_to=instance.id)
    sys_req = SystemRequirements.objects.filter(related_to=instance.id)
    game_genre = GameGenre.objects.filter(related_to=instance.id)
    game_lore = GameLore.objects.filter(related_to=instance.id)
    gallery = GamesGallery.objects.filter(related_to=instance.id)
    timeline = GamesTimeline.objects.filter(related_to=instance.id)
    # year month
    date_field = 'completion_date'
    archive = {}
    years = timeline.dates(date_field, 'year')[::-1]
    for date_year in years:
        object = timeline.filter(completion_date__year=date_year.year)
        archive[date_year] = object

    archive = sorted(archive.items(), reverse=True)

    context = {
        "instance" : instance,
        "stores" : game_stores,
        "requirements" : sys_req,
        "genre" : game_genre,
        "lore" : game_lore,
        "gallery" : gallery,
        "archive" : archive
    }
    return render(request, "game_detail.html", context)

# upcoming block ---------------------------------------------------------------------------
def upcomingView(request):
    upcoming = UpcomingGamesModel.objects.filter(is_active=True)

    context = {
        "upcoming" : upcoming,

    }
    return render(request, "upcoming.html", context)

# portfolio block --------------------------------------------------------------------------
def portfolio_pageView(request, **kwargs):
    portfolio_3d = PortfolioModel.objects.filter(category_type__iexact="3D")
    portfolio_3d_images = []
    for i in portfolio_3d:
        portfolio_3d_images.append(Images.objects.filter(related_to=i))

    portfolio_concept = PortfolioModel.objects.filter(category_type__iexact="Concept")
    portfolio_concept_images = []
    for i in portfolio_concept:
        portfolio_concept_images.append(Images.objects.filter(related_to=i))

    portfolio_unity = PortfolioModel.objects.filter(category_type__iexact="Unity")
    portfolio_unity_images = []
    for i in portfolio_unity:
        portfolio_unity_images.append(Images.objects.filter(related_to=i))

    portfolio_unreal = PortfolioModel.objects.filter(category_type__iexact="Unreal")
    portfolio_unreal_images = []
    for i in portfolio_unreal:
        portfolio_unreal_images.append(Images.objects.filter(related_to=i))

    portfolio_exp = PortfolioModel.objects.filter(category_type__iexact="Experimental")
    portfolio_exp_images = []
    for i in portfolio_exp:
        portfolio_exp_images.append(Images.objects.filter(related_to=i))

    context = {
        "3d" : portfolio_3d_images,
        "Concept" : portfolio_concept_images,
        "Unity" : portfolio_unity_images,
        "Unreal" : portfolio_unreal_images,
        "Experimental" : portfolio_exp_images
    }
    return render(request, "portfolio.html", context)

# blog normal block ------------------------------------------------------------------------
def blog_pageView(request, tag_slug=None, **kwargs):
    blog_list   = BlogModel.objects.all().order_by("-created")
    # paginator
    paginator   = Paginator(blog_list, 10) # Show 25 contacts per page
    page        = request.GET.get('page')
    try:
        blog_list = paginator.page(page)
    except PageNotAnInteger:
        blog_list = paginator.page(1)
    except EmptyPage:
        blog_list = paginator.page(paginator.num_pages)

    # tags
    tag_list = Tag.objects.all()
    tag_slugs = request.GET.get("tag_slug")
    if tag_slugs:
        blog_list = BlogModel.objects.filter(tags__slug=tag_slugs)
        # paginator
        paginator = Paginator(blog_list, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage:
            blog_list = paginator.page(paginator.num_pages)

    # search
    query = request.GET.get("q")
    if query:
        query_list = query.split()
        blog_list = BlogModel.objects.filter(
                    reduce(operator.and_,(Q(blog_title__icontains=q) for q in query_list)) |
                    reduce(operator.and_, (Q(tags__slug__icontains=q) for q in query_list))
        )
        # paginator
        paginator = Paginator(blog_list, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage:
            blog_list = paginator.page(paginator.num_pages)

    # year month
    date_field = 'published_on'
    archive = {}
    years = BlogModel.objects.all().dates(date_field, 'year')[::-1]
    for date_year in years:
        months = BlogModel.objects.filter(published_on__year=date_year.year).dates(date_field, 'month')
        archive[date_year] = months

    archive = sorted(archive.items(), reverse=True)
    ym = request.GET.get("y_m")
    if ym:
        yy = ym.split("-")
        blog_list= BlogModel.objects.filter(published_on__year=yy[0]).filter(published_on__month=yy[1])
        # paginator
        paginator = Paginator(blog_list, 10)  # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            blog_list = paginator.page(page)
        except PageNotAnInteger:
            blog_list = paginator.page(1)
        except EmptyPage:
            blog_list = paginator.page(paginator.num_pages)


    context = {
        "blog" : blog_list,
        "tags" : tag_list,
        "archive" : archive
    }
    return render(request, "blog.html", context)

# details single blog block ----------------------------------------------------------------
def blog_detailView(request, id, **kwargs):
    instance = get_object_or_404(BlogModel, id=id)
    blog_content = BlogContentModel.objects.filter(related_to=instance.id)
    share_str = quote_plus(instance.blog_description+" -By "+instance.blog_author.author_name)
    linkedin_msg = quote_plus(instance.blog_title)
    context = {
        "instance" : instance,
        "content" : blog_content,
        "summery_msg" : share_str,
        "title_msg" : linkedin_msg
    }
    return render(request, "blog_detail.html", context)



def about_pageView(request):
    queryset = AboutModel.objects.all()
    team = AboutTeamImage.objects.all()
    thanks = ThanksName.objects.all()
    pro_address = AboutModel.objects.values_list('production_address', flat=True)[0]
    pro_mob = AboutModel.objects.values_list("production_mobile", flat=True)[0]
    pro_email = AboutModel.objects.values_list("production_email", flat=True)[0]
    op_address = AboutModel.objects.values_list("operation_address", flat=True)[0]
    op_email = AboutModel.objects.values_list("operation_email", flat=True)[0]
    context = {
        "about" : queryset,
        "team" : team,
        "ty" : thanks,
        "production_address" : pro_address,
        "production_mobile" : pro_mob,
        "production_email" : pro_email,
        "operation_address" : op_address,
        "operation_email" : op_email
    }
    return render(request, "about.html", context)

def error_pageView(request):
    # queryset =
    context = {

    }
    return render(request, "error.html", context)


from django.shortcuts import render_to_response
from django.template import RequestContext
def handler404(request):
    response = render_to_response('error.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response




