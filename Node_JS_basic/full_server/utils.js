import fs from 'fs/promises';

const readDatabase = (filePath) => fs.readFile(filePath, 'utf8')
  .then((data) => {
    const lines = data.trim().split('\n');
    const students = lines.slice(1).filter((line) => line.length > 0);
    const fields = {};

    students.forEach((student) => {
      const [firstname, , , field] = student.split(',');
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    return fields;
  })
  .catch(() => {
    throw new Error('Cannot load the database');
  });

export default readDatabase;
