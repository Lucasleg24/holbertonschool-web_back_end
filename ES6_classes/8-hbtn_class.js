export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // si main appel un nombre cette méthode sera automatiquement appelé
  valueOf() {
    return this._size;
  }

  // si main appel une string cette méthode sera automatiquement appelé
  toString() {
    return this._location;
  }
}
