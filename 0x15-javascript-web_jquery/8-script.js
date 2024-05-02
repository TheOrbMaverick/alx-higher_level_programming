$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Iterate over each movie in the data
    data.results.forEach(function (movie) {
        // Create a new list item for each movie title and append it to the UL
        $('<li>').text(movie.title).appendTo('#list_movies');
    });
});
