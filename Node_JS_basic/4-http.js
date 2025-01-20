const http = require('http');

// Créer le serveur HTTP
const app = http.createServer((req, res) => {
  // Définir les en-têtes de réponse
  res.statusCode = 200; // Code 200 = OK
  res.setHeader('Content-Type', 'text/plain'); // Réponse en texte brut

  // Contenu de la réponse
  res.end('Hello Holberton School!');
});

// Faire écouter le serveur sur le port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is listening on port ${PORT}`);
});

// Exporter le serveur pour réutilisation
module.exports = app;
