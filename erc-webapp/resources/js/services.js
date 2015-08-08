angular.module('starter.services', [])

.factory('Remote', function($http) {
  var serverAddress = '192.168.1.3';
  var serverPort = 5000;

  return {
    sendHTTP: function(route) {
      $http.get('http://' + serverAddress + ':' + 5000 + route);
    },
    prepareSendHTTP: function(route) {
      return function() {
        $http.get('http://' + serverAddress + ':' + 5000 + route);
      }
    },
    socket: {
      connect: function(route) {
        return io.connect('http://' + serverAddress + ':' + serverPort + route);
      }
    }
  };
});
