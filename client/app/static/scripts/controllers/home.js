'use strict';

angular.module('clientApp')
  .controller('HomeCtrl', function ($scope, Restangular) {
  	$scope.tweets = '';
  	$scope.more_info = '';
  	$scope.fetchTrends = function(){
  		var response = Restangular.all('assign/fetch_tweets').customGET("");
	  	response.then(function(data){
	  		$scope.tweets = data.tweets;
	  		$scope.more_info = data.more_info;
	  		$scope.message = "Trending Tweets";
	  	});
  	};
  	
});