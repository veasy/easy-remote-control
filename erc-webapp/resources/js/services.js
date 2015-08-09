angular.module('starter.services', [])

.factory('Remote', function($http) {
  var serverAddress = '192.168.1.35';
  var serverPort = 5000;

  return {
    sendHTTP: function(route) {
      $http.get(route);
    },
    prepareSendHTTP: function(route) {
      return function() {
        $http.get(route);
      }
    },
    socket: {
      connect: function(route) {
        return io.connect(route);
      }
    }
  };
});
