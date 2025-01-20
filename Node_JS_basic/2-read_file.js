const fs = require('fs');

function countStudents(path) {
  try {
    // Lecture synchronisée du fichier
    const data = fs.readFileSync(path, 'utf8');

    // Diviser le contenu du fichier en lignes
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Supprimer les lignes vides

    // Vérification si le fichier contient un en-tête
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    // Extraire les en-têtes et les données
    const headers = lines[0].split(',');
    const students = lines.slice(1).map((line) => {
      const values = line.split(',');
      const student = {};
      headers.forEach((header, index) => {
        student[header.trim()] = values[index].trim();
      });
      return student;
    });

    // Comptage des étudiants
    console.log(`Number of students: ${students.length}`);

    // Regrouper les étudiants par domaine (FIELD)
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

    // Afficher les résultats pour chaque domaine
    for (const [field, names] of Object.entries(fields)) {
      console.log(
        `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`,
      );
    }
  } catch (err) {
    // En cas d'erreur, lever une exception
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
