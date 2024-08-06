#!/usr/bin/node

const request = require('request');

const getCharacters = async (movieId) => {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    const data = JSON.parse(body);
    const characters = data.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(error);
          return;
        }

        const characterData = JSON.parse(body);
        console.log(characterData.name);
      });
    });
  });
};

if (process.argv.length !== 3) {
  console.log('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
getCharacters(movieId);
