from django.db import models

# Create your models here.
class TrendingTweets(models.Model):
	no_of_tweets = models.IntegerField(default=0)
	tweets_date = models.DateTimeField(null=True, blank=True)

	def __str__(self):
		return '%d, %s' % (self.no_of_tweets, self.tweets_date)

	def save(self, *args, **kwargs):
		super(TrendingTweets, self).save(*args, **kwargs)