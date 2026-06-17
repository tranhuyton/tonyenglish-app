const fs = require('fs');
const pdf = require('pdf-parse');

let dataBuffer = fs.readFileSync('public/Reading strategies for the ielts test - Answer Key.pdf');

pdf(dataBuffer).then(function(data) {
    console.log(data.text.substring(0, 3000));
}).catch(err => console.log(err));
