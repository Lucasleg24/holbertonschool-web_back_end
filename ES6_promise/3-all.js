import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  // Appeler les deux fonctions et gérer leurs promesses
  // photo = résultat de la promesse uploadPhoto
  // user = résultat de la promesse createUser
  return Promise.all([uploadPhoto(), createUser()])
    .then((results) => {
      const photo = results[0];
      const user = results[1];

      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}

export default handleProfileSignup;
