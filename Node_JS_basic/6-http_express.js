const express = require('express');

// Créer une application Express
const app = express();

// Gestion de l'endpoint "/"
app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

// Faire écouter le serveur sur le port 1245
const PORT = 1245;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// Exporter l'application
module.exports = app;
