export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }

    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }

    // lève un TypeError
    // Si students n'est pas un tableau OU que le tableau "students"
    // contient un student (éléments) qui n'est pas une strings
    if (!Array.isArray(students) || !students.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }

    // stock la valeur verifié dans une propriété privé
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter
  get name() {
    return this._name;
  }

  // Setter + check si la nouvelle valeur est une string
  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Getter
  get length() {
    return this._length;
  }

  // Setter + check si la nouvelle valeur est un nombre
  set length(value) {
    if (typeof value !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // Getter
  get students() {
    return this._students;
  }

  // Setter + check si la nouvelle valeur est un tableau de strings
  set students(value) {
    if (!Array.isArray(value) || !value.every((student) => typeof student === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
