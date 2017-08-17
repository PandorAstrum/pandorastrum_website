from django.conf.urls import url
from pandorastrum.views import (
    redirect_root,
    home_pageView,
    game_pageView,
    portfolio_pageView,
    blog_pageView,
    blog_detailView,
    blog_tagView,
    about_pageView,
    error_pageView
)

urlpatterns = [
    url(r'^$', redirect_root),
    url(r'^home/$', home_pageView, name="home"),
    url(r'^games/$', game_pageView, name="games"),
    url(r'^portfolio/$', portfolio_pageView, name="portfolio"),
    url(r'^blog/$', blog_pageView, name="blog"),
    url(r'^blog/(?P<slug>[-\w]+)/$', blog_tagView.as_view(), name="blog_tagged"),
    url(r'^blog/(?P<id>\d+)/$', blog_detailView, name="detail"),
    url(r'^about/$', about_pageView, name="about"),
    url(r'^error/$', error_pageView, name="error"),
]