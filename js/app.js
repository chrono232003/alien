(function() {
	var app = angular.module('home', ['ngCookies', 'ngSanitize']);

	//directives
	app.directive('header', function() {
		return {
			restrict:"E",
			templateUrl:"directives/header.html"
		}
	});

	app.directive('footer', function() {
		return {
			restrict:"E",
			templateUrl:"directives/footer.html"
		}
	});

//controllers

	//Home page
	app.controller('HomeController', ['$scope', '$http', function($scope, $http) {

		function matrixList(data, n) {
        var grid = [], i = 0, x = data.length, col, row = -1;
        for (var i = 0; i < x; i++) {
            col = i % n;
            if (col === 0) {
                grid[++row] = [];
            }
            grid[row][col] = data[i];
        }
        return grid;
			};

		function conditionArticleHomePage(data) {
			for (var i = 0; i < data.length; i++) {
				data[i].article = data[i].article.substring(0,800) + "...";
			}
			return data;
		}
		$http.get('php/home.php').then(function(response) {
				var storyData = conditionArticleHomePage(response.data);
				$scope.homeList = storyData;
				$scope.repeatRow = matrixList(response.data, 2);
			}).catch(function(e) {
					console.log("Error: " + e);
			});
	}]);

  //story page
	app.controller('GetStoryController', ['$scope', '$http', function($scope, $http) {
		function getStoryID() {
			var IDString = window.location.search;
			return IDString.substring(IDString.indexOf("=")+1);
		}
		var request = $http({
			method: "post",
			url: "php/story.php",
			data: {
				storyId: getStoryID()
			},
			headers: {'Content-Type': 'application/x-www-form-urlencoded' }
		})

		request.then(function(response) {
				$scope.story = response.data[0];
		}).catch(function(e) {
				console.log("Error: " + e);
		});
	}]);

	app.controller('BrowseController', ['$scope', '$http', function($scope, $http) {
		function conditionStoryHomePage(data) {
			for (var i = 0; i < data.length; i++) {
				data[i].Story = data[i].Story.substring(0,300) + "<a href = 'story.html?ID=" + data[i].ID + "'> ... Read More</a>";
			}
			return data;
		}
		$http.get('php/browse.php').then(function(response) {
			$scope.stories = response.data;
		}).catch(function(e) {
				console.log("Error: " + e);
		});
	}]);

})();
