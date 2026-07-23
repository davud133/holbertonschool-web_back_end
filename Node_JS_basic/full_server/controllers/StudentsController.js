import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    const databasePath = process.argv[2];

    readDatabase(databasePath)
      .then((fields) => {
        const output = ['This is the list of our students'];

        Object.keys(fields)
          .sort((first, second) => first.localeCompare(
            second,
            undefined,
            { sensitivity: 'base' },
          ))
          .forEach((field) => {
            output.push(
              `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
            );
          });

        response.status(200).send(output.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const databasePath = process.argv[2];

    readDatabase(databasePath)
      .then((fields) => {
        response.status(200).send(`List: ${fields[major].join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}
