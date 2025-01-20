// Afficher le message de bienvenue
console.log('Welcome to Holberton School, what is your name?');

// Gestion de l'entrée utilisateur via stdin
process.stdin.on('data', (input) => {
  // Supprimer les espaces et les sauts de ligne de l'entrée utilisateur
  const name = input.toString().trim();

  // Afficher le nom de l'utilisateur
  console.log(`Your name is: ${name}`);

  // Fermer le programme proprement
  console.log('This important software is now closing');
  process.exit();
});
