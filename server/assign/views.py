from django.shortcuts import render
from rest_framework.response import Response

import tweepy

from .models import TrendingTweets
from .serializers import TrendingTweetsSerializer
from rest_framework import status, viewsets
from rest_framework.decorators import list_route
from datetime import datetime

# Create your views here.


class TrendingTweetsViewSet(viewsets.ModelViewSet):
	queryset = TrendingTweets.objects.all()
	serializer_class = TrendingTweetsSerializer

	

	@list_route()
	def fetch_tweets(self,request):

		def save_simple(model_serializer, data, instance=None, partial=False):
			object_serialized = model_serializer(instance=instance, data=data, partial=partial)
			object_serialized.is_valid(raise_exception=True)
			model_object = object_serialized.save()
			return model_object

		try:
			dit = {}
			CONSUMER_KEY = 'CONSUMER_KEY'
			CONSUMER_SECRET = 'CONSUMER_SECRET'
			OAUTH_TOKEN = 'OAUTH_TOKEN'
			OAUTH_TOKEN_SECRET = 'OAUTH_TOKEN_SECRET'
			auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
			auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
			api = tweepy.API(auth)
			# api = twitter.api()
			max_tweets = 300
			trends1 = api.trends_place(1)
			# place = input("Enter you place")
			# trends = set([trend[place] for trend in data[0]['trends1']])
			hashtags = [trend['name'] for trend in trends1[0]['trends'] if trend['name'].startswith('#')]
			tweets_object = {}
			tweets_object['no_of_tweets'] = len(hashtags)
			tweets_object['tweets_date'] = datetime.now()
			tweets = save_simple(TrendingTweetsSerializer, tweets_object)
			serializer = TrendingTweetsSerializer(tweets)
			
			return Response(status=status.HTTP_200_OK, data={"more_info": serializer.data,'tweets':hashtags})
		except Exception as e:
			return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, data={"message": "Unable to fetch Tweets!"})