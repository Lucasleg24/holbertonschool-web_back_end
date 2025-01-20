const fs = require('fs').promises;

async function countStudents(path) {
  try {
    // Lire le fichier de manière asynchrone
    const data = await fs.readFile(path, 'utf8');

    // Diviser le contenu du fichier en lignes
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    // Si le fichier ne contient pas d'étudiants (lignes vides ou seulement l'en-tête)
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }

    // Extraire les en-têtes (première ligne du fichier)
    const headers = lines[0].split(',');

    // Mapper chaque ligne du fichier en un étudiant (en tant qu'objet)
    const students = lines.slice(1).map((line) => {
      const values = line.split(',');
      const student = {};
      headers.forEach((header, index) => {
        student[header.trim()] = values[index].trim();
      });
      return student;
    });

    // Afficher le nombre total d'étudiants
    console.log(`Number of students: ${students.length}`);

    // Créer un objet pour regrouper les étudiants par domaine
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

    // Afficher le nombre d'étudiants par domaine et la liste de leurs prénoms
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (err) {
    // Si le fichier est introuvable ou une erreur survient, rejeter avec un message d'erreur
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
