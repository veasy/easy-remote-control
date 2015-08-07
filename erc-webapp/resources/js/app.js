angular.module('starter', ['ionic', 'starter.controllers', 'starter.services'])

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
      'tab-dash': {
        templateUrl: '/resources/templates/tab-remote.html',
        controller: 'RemoteCtrl'
      }
    }
  })

  .state('tab.chats', {
      url: '/chats',
      views: {
        'tab-chats': {
          templateUrl: '/resources/templates/tab-chats.html',
          controller: 'ChatsCtrl'
        }
      }
    })
    .state('tab.chat-detail', {
      url: '/chats/:chatId',
      views: {
        'tab-chats': {
          templateUrl: '/resources/templates/chat-detail.html',
          controller: 'ChatDetailCtrl'
        }
      }
    })

  .state('tab.account', {
    url: '/account',
    views: {
      'tab-account': {
        templateUrl: '/resources/templates/tab-account.html',
        controller: 'AccountCtrl'
      }
    }
  });

  $urlRouterProvider.otherwise('/tab/remote');
});
