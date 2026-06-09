const arr = ["10. Grammar", "1. Grammar", "11. Grammar", "2. Grammar", "1.1. Grammar", "1.10. Grammar", "1.2. Grammar"];
arr.sort((a,b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }));
console.log(arr);
