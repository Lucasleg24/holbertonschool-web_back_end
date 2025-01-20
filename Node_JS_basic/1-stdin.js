// Import du module process pour gérer les entrées/sorties
process.stdout.write('Welcome to Holberton School, what is your name?\n');

// Création d'un écouteur pour l'entrée standard
process.stdin.on('data', (data) => {
  // Affichage du nom saisi
  process.stdout.write(`Your name is: ${data}`);
});

// Écouteur pour détecter la fin de l'entrée (Ctrl+D ou pipe)
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
