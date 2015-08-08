angular.module('starter', ['ionic', 'starter.controllers', 'starter.services', 'starter.directives'])

.run(function($ionicPlatform) {
  $ionicPlatform.ready(function() {
    if (!window.navigator.standalone) {
      var meta = document.createElement("meta");
      var head = document.getElementsByTagName("head")[0];

      meta.setAttribute("name", "apple-mobile-web-app-status-bar-style");
      meta.setAttribute("content", "black-translucent");
      head.appendChild(meta); }
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

  .state('tab.applications', {
    url: '/applications',
    views: {
      'tab-applications': {
        templateUrl: '/resources/templates/tab-applications.html',
        controller: 'ApplicationsCtrl'
      }
    }
  });

  $urlRouterProvider.otherwise('/tab/remote');
});
