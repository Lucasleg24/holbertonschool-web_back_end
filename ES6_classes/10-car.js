export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  // Getter qui renvoie une class de type Car
  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    // appel le constructeur de la class instancié par le getter
    const ModelCar = this.constructor[Symbol.species];
    // Crée et retourne un nouvelle instance spécifiée par la constante Species.
    return new ModelCar();
  }
}
