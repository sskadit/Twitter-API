'use strict';

angular.module('clientApp', [
    'ngCookies',
    'ngMessages',
    'ngSanitize',
    'ui.router',
    'restangular',
    'ui.bootstrap',
    'clientApp.envConstants',
    // 'ngMap',
    // 'clientApp.envConstants',
    'moment-picker',
])
.config(function(RestangularProvider, envBaseDomain) {
    RestangularProvider.setBaseUrl(envBaseDomain);
})
.config(function ($locationProvider, $urlRouterProvider, $stateProvider, $httpProvider) {
    $locationProvider.html5Mode(true);
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    
    // $httpProvider.interceptors.push('responseInterceptor');

    $stateProvider
      .state('home', {
        url: '/',
        controller: 'HomeCtrl',
        templateUrl: 'static/views/home.html'
      })
      
      .state('otherwise', {
        url: '*path',
        templateUrl: 'static/views/404.html'
      });
})
  .run(function($rootScope, $state, envBaseDomain){   
    $rootScope.baseUrl = envBaseDomain;
    $rootScope.$on('$stateChangeError', function(event) {
      $state.go('404');
    });
})
  .run(function($rootScope, $location, $window){
   if($location.host() == 'www.adi.com'){
     $window.ga('create', 'UA-89508909-1', 'auto');
     $rootScope.$on('$stateChangeSuccess', function (event) {
         $window.ga('send', 'pageview', $location.path());
     });
   }
 });