const num1 = parseInt(prompt("Number 1:"));
const func = prompt("Arithmetic operator: +, -, *, /,%");
const num2 = parseInt(prompt("Number 2:"));

// for Adition
if (func === "+") {
  document.write(num1 + num2);

  // for Subtraction
} else if (func === "-") {
  document.write(num1 - num2);
  // For multiplication
} else if (func === "*") {
  document.write(num1 * num2);

  // for Division
} else if (func === "/") {
  document.write(num1 / num2);

  // for Remainder
} else if (func === "%") {
  document.write(num1 % num2);
}
