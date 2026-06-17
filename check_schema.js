const u29 = require('./unit29.json');
console.log('Keys of part 0:', Object.keys(u29.parts[0]));
if (u29.parts[0].exercises) {
  console.log('Exercises:', u29.parts[0].exercises.length);
  console.log('Keys of first exercise:', Object.keys(u29.parts[0].exercises[0]));
  if (u29.parts[0].exercises[0].questions) {
    console.log('Questions:', u29.parts[0].exercises[0].questions.length);
  }
}
