from django.conf.urls import url
from pandorastrum.views import (
    redirect_root,
    home_pageView,
    game_pageView,
    game_detailView,
    upcomingView,
    portfolio_pageView,
    blog_pageView,
    blog_detailView,
    about_pageView,
    error_pageView
)

urlpatterns = [
    url(r'^$', redirect_root),
    url(r'^home/$', home_pageView, name="home"),
    url(r'^games/$', game_pageView, name="games"),
    url(r'^games/(?P<id>\d+)/$', game_detailView, name="game_detail"),
    url(r'^upcoming/$', upcomingView, name="upcoming"),
    url(r'^portfolio/$', portfolio_pageView, name="portfolio"),
    url(r'^blog/$', blog_pageView, name="blog"),
    url(r'^blog/(?P<id>\d+)/$', blog_detailView, name="detail"),
    url(r'^about/$', about_pageView, name="about"),
    # url(r'^error/$', error_pageView, name="error"),
]