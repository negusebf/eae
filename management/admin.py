from django.contrib import admin
from management.models import (HomeView, 
								Trending, 
								HomeBaseText, 
								PostsPage, 
								AboutVideo, 
								EmailSubscriptions, 
								FeedBackSubmission, 
								EmailSender,
								ManualAdsManager)
from embed_video.admin import AdminVideoMixin
# Register your models here.

class HomeViewListing(AdminVideoMixin, admin.ModelAdmin):
	list_display = ('title', 'published_date')
	list_display_links = ('title', 'published_date')
	list_filter = ('author',)
	list_per_page = 18
	#list_editable = ()
	search_fields = ('title',)

class SubscribersList(admin.ModelAdmin):
	list_display = ('subscriber_email', 'is_subscriber_active')
	list_display_links = ('subscriber_email',)
	list_filter = ('subscriber_email',)
	list_per_page = 18
	list_editable = ('is_subscriber_active',)
	search_fields = ('subscriber_email',)


class EmailSenderList(admin.ModelAdmin):
	list_display = ('e_from', 'to', 'subject', 'purpose', 'sent_on')
	list_display_links = ('subject',)
	list_filter = ('subject',)
	list_per_page = 18
	list_editable = ('sent_on',)
	search_fields = ('subject',)



admin.site.register(HomeView, HomeViewListing)

admin.site.register(Trending, HomeViewListing)

admin.site.register(HomeBaseText)

admin.site.register(PostsPage)

admin.site.register(AboutVideo)

admin.site.register(EmailSubscriptions, SubscribersList)

admin.site.register(FeedBackSubmission)

admin.site.register(EmailSender, EmailSenderList)

admin.site.register(ManualAdsManager)

