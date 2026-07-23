const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const messages = [];
  const originalConsoleLog = console.log;

  console.log = (message) => {
    messages.push(message);
  };

  countStudents(database)
    .then(() => {
      console.log = originalConsoleLog;
      res.type('text/plain');
      res.send(`This is the list of our students\n${messages.join('\n')}`);
    })
    .catch((error) => {
      console.log = originalConsoleLog;
      res.type('text/plain');
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
