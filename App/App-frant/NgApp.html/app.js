// Define the AngularJS module
var app = angular.module('myApp', []);

// Define the AngularJS controller
app.controller('apiController', function($scope, $http) {
    $scope.getData = function() {
        // Send a request to the server-side proxy endpoint
        $http.get('/random-nam/')
            .then(function(response) {
                // Process the response data
                $scope.responseData = response.data;
            })
            .catch(function(error) {
                // Handle errors
                console.log(error);
            });
    };
});
 