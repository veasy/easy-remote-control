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

  var lastX = 0;
  var lastY = 0;

  $scope.onDrag = function(event)  {
    deltaX = event.gesture.deltaX - lastX
    deltaY = event.gesture.deltaY - lastY

    lastX = event.gesture.deltaX;
    lastY = event.gesture.deltaY;

    socket.emit('mouseDragged', {x:deltaX, y:deltaY});
  };

  $scope.onRelease = function(event) {
    lastX = 0;
    lastY = 0;
  };

  $scope.left = function() {
    socket.emit('mouseLeft', {});
  };
  $scope.right = function() {
    socket.emit('mouseRight', {});
  };
})

.controller('TextCtrl', function($scope, Remote) {
  var socket = Remote.socket.connect('/text');

  var getCharFromKeyCode = function(keyCode) {
    if (keyCode === 8) return 'DELETE';
    if (keyCode === 13) return 'RETURN';
    if (keyCode === 32) return 'SPACE';

    return String.fromCharCode(event.keyCode);
  };

  $scope.sendChar = function(event) {
    socket.emit('char', getCharFromKeyCode(event.keyCode));
  };
});
