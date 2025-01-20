const http = require('http');
const fs = require('fs').promises;

// Fonction pour lire et analyser le fichier CSV
async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    if (lines.length <= 1) {
      return 'Number of students: 0';
    }

    const headers = lines[0].split(',');
    const students = lines.slice(1).map((line) => {
      const values = line.split(',');
      const student = {};
      headers.forEach((header, index) => {
        student[header.trim()] = values[index].trim();
      });
      return student;
    });

    const totalStudents = `Number of students: ${students.length}`;
    const fields = {};
    students.forEach((student) => {
      const { field } = student;
      if (field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(student.firstname);
      }
    });

    let fieldDetails = '';
    for (const [field, names] of Object.entries(fields)) {
      fieldDetails += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
    }

    return `${totalStudents}${fieldDetails}`;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

// Créer le serveur HTTP
const app = http.createServer(async (req, res) => {
  const { url } = req;

  if (url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');

    // Lire le fichier passé en argument
    const databasePath = process.argv[2];
    if (!databasePath) {
      res.end('This is the list of our students\nCannot load the database');
      return;
    }

    try {
      const studentData = await countStudents(databasePath);
      res.end(`This is the list of our students\n${studentData}`);
    } catch (err) {
      res.end('This is the list of our students\nCannot load the database');
    }
  } else {
    res.statusCode = 404;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Not Found');
  }
});

// Faire écouter le serveur sur le port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

// Exporter le serveur
module.exports = app;
