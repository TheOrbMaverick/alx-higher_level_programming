#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to fetch character details
function fetchCharacter (characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      if (response.statusCode !== 200) {
        reject(new Error(`Failed to fetch character details. Status code: ${response.statusCode}`));
        return;
      }

      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

// Fetch movie details
request(movieUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie details. Status code: ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  const charactersUrls = movie.characters;

  // Fetch character details in the order specified in the response
  Promise.all(charactersUrls.map(fetchCharacter))
    .then(characters => {
      characters.forEach(character => {
        console.log(character);
      });
    })
    .catch(error => {
      console.error(error);
    });
});
