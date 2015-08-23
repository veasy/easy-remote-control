angular.module('starter', ['ionic', 'starter.controllers', 'starter.services'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {

  });
})

.config(function($stateProvider, $urlRouterProvider) {
  $stateProvider

  .state('tab', {
    url: '/tab',
    abstract: true,
    templateUrl: '/resources/templates/tabs.html'
  })

  .state('tab.remote', {
    url: '/remote',
    views: {
      'tab-remote': {
        templateUrl: '/resources/templates/tab-remote.html',
        controller: 'RemoteCtrl'
      }
    }
  })

  .state('tab.mouse', {
      url: '/mouse',
      views: {
        'tab-mouse': {
          templateUrl: '/resources/templates/tab-mouse.html',
          controller: 'MouseCtrl'
        }
      }
    })

  .state('tab.text', {
    url: '/text',
    views: {
      'tab-text': {
        templateUrl: '/resources/templates/tab-text.html',
        controller: 'TextCtrl'
      }
    }
  });

  $urlRouterProvider.otherwise('/tab/remote');
});
