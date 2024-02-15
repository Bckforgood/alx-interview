#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as a command-line argument.');
  process.exit(1);
}

const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;

  // Fetch and print character names
  charactersUrls.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error('Unexpected status code:', response.statusCode);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});

