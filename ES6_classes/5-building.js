export default class Building {
  constructor(sqft) {
    // vérifie si l'instance actuelle n'est pas crée par Building
    // et si cette sous-instance n'as pas de propriété "evacuationWarningMessage"
    if (this.constructor !== Building && !this.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }
}
