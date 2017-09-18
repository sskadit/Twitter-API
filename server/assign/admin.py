from django.contrib import admin

# Register your models here.

from .models import TrendingTweets

class TrendingTweetsAdmin(admin.ModelAdmin):
    # The fields to display and the categories they need to be put into:
	fieldsets = (
        ('Details', {
            'fields': ('no_of_tweets','tweets_date'),
        }),
	)
	list_display = ('no_of_tweets','tweets_date')
	# The criteria for setting up a search feature
	search_fields = ('tweets_date',)
	
	class Meta:
		model = TrendingTweets

admin.site.register(TrendingTweets, TrendingTweetsAdmin)