angular.module('starter.controllers', [])

.controller('RemoteCtrl', function($scope, Remote) {
    $scope.up = Remote.prepareSend('/keys/up');
    $scope.down = Remote.prepareSend('/keys/down');
    $scope.left = Remote.prepareSend('/keys/left');
    $scope.right = Remote.prepareSend('/keys/right');
    $scope.menu = Remote.prepareSend('/keys/escape');
    $scope.play = Remote.prepareSend('/keys/return');
})

.controller('ChatsCtrl', function($scope, Chats) {
  $scope.chats = Chats.all();
  $scope.remove = function(chat) {
    Chats.remove(chat);
  };
})

.controller('ChatDetailCtrl', function($scope, $stateParams, Chats) {
  $scope.chat = Chats.get($stateParams.chatId);
})

.controller('AccountCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
