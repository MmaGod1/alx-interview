#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line argument
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// API endpoint for the Star Wars films
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a request to get the film details
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  if (res.statusCode !== 200) {
    console.error(`Error: Failed to fetch data (status code: ${res.statusCode})`);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  // Fetch and display characters in order
  characters.forEach((characterUrl) => {
    request(characterUrl, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error(charErr);
        return;
      }
      if (charRes.statusCode === 200) {
        const character = JSON.parse(charBody);
        console.log(character.name);
      }
    });
  });
});
