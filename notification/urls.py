from django.conf.urls.defaults import *

from notification.views import *


urlpatterns = patterns("",
    url(r"^$", notices, name="notification_notices"),
    url(r"^settings/$", notice_settings, name="notification_notice_settings"),
    url(r"^(\d+)/$", single, name="notification_notice"),
    url(r"^feed/$", feed_for_user, name="notification_feed_for_user"),
    url(r"^mark_all_seen/$", mark_all_seen, name="notification_mark_all_seen"),
    
    # Ajax urls
    url(r"^ajax/mark_all_seen/$", ajax_mark_all_seen, name="notification_ajax_mark_all_seen"),
)
