const http = require('http');
const fs = require('fs');

const databasePath = process.argv[2];

function getStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);
      const fields = {};

      students.forEach((student) => {
        const values = student.split(',');
        const firstname = values[0].trim();
        const field = values[3].trim();

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      const output = [`Number of students: ${students.length}`];

      Object.keys(fields).forEach((field) => {
        output.push(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      });

      resolve(output.join('\n'));
    });
  });
}

const app = http.createServer((request, response) => {
  response.setHeader('Content-Type', 'text/plain');

  if (request.url === '/') {
    response.statusCode = 200;
    response.end('Hello Holberton School!');
    return;
  }

  if (request.url === '/students') {
    response.statusCode = 200;

    getStudents(databasePath)
      .then((students) => {
        response.end(`This is the list of our students\n${students}`);
      })
      .catch((error) => {
        response.end(
          `This is the list of our students\n${error.message}`,
        );
      });

    return;
  }

  response.statusCode = 404;
  response.end('Not found');
});

app.listen(1245);

module.exports = app;
