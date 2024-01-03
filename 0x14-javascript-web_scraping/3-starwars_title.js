#!/usr/bin/node
// script that prints the title of a start war movie where the episode matches a given integer
const axios = require('axios');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API endpoint
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the specified URL
axios.get(url)
  .then(response => {
    // Print the title of the movie
    console.log(`Title: ${response.data.title}`);
  })
  .catch(error => {
    // Print the error message if the request fails
    console.error(error.message);
  });
