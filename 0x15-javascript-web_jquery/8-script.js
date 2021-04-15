// Fetches and lists the title for all movies by using this URL.
$.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (const film of data.results) {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  }
});
