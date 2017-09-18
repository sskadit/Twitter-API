from rest_framework import serializers
from .models import TrendingTweets

class TrendingTweetsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TrendingTweets
        fields = ('id', 'no_of_tweets', 'tweets_date')