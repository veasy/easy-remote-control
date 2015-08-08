angular.module('starter.controllers', [])

.controller('RemoteCtrl', function($scope, Remote) {
  $scope.up = Remote.prepareSendHTTP('/keys/up');
  $scope.down = Remote.prepareSendHTTP('/keys/down');
  $scope.left = Remote.prepareSendHTTP('/keys/left');
  $scope.right = Remote.prepareSendHTTP('/keys/right');
  $scope.menu = Remote.prepareSendHTTP('/keys/escape');
  $scope.play = Remote.prepareSendHTTP('/keys/return');
})

.controller('MouseCtrl', function($scope, Remote) {
  var socket = Remote.socket.connect('/mouse');

  $scope.onDrag = function(event)  {
  $scope.xCenter = event.gesture.center.pageX;
  $scope.yCenter = event.gesture.center.pageY;
  $scope.xEvent = event.gesture.deltaX;
  $scope.yEvent = event.gesture.deltaY;

    socket.emit('mouseDragged', {data: {x:event.gesture.deltaX, y:event.gesture.deltaY} });
  };
})

.controller('ApplicationsCtrl', function($scope) {
  $scope.settings = {
    enableFriends: true
  };
});
