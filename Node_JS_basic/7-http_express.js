const express = require('express');
const fs = require('fs').promises;

const app = express();

function countStudents(path) {
  return fs.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.trim().split('\n');
      const students = lines.slice(1).filter((line) => line.length > 0);

      const fields = {};
      for (const student of students) {
        const [firstname, , , field] = student.split(',');
        if (!fields[field]) {
          fields[field] = {
            count: 1,
            students: [firstname],
          };
        } else {
          fields[field].count += 1;
          fields[field].students.push(firstname);
        }
      }

      let output = `Number of students: ${students.length}\n`;
      for (const [field, data] of Object.entries(fields)) {
        output += `Number of students in ${field}: ${data.count}. List: ${data.students.join(', ')}\n`;
      }
      return output;
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  try {
    const database = process.argv[2];
    const studentsData = await countStudents(database);
    res.send(`This is the list of our students\n${studentsData}`);
  } catch (error) {
    res.send(`This is the list of our students\n${error.message}`);
  }
});

const port = 1245;
app.listen(port);

module.exports = app;
