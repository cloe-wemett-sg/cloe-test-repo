// Test file for cloe-test-repo — feel free to read, edit, or delete this.
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

function multiply(a, b) {
  return a * b;
}

function divide(a, b) {
  if (b === 0) throw new Error("Division by zero");
  return a / b;
}

function power(base, exp) {
  return Math.pow(base, exp);
}

function factorial(n) {
  if (n < 0) throw new Error("Negative input");
  if (n === 0 || n === 1) return 1;
  return n * factorial(n - 1);
}

function isPrime(n) {
  if (n < 2) return false;
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
  }
  return true;
}

function fibonacci(n) {
  if (n <= 1) return n;
  let a = 0, b = 1;
  for (let i = 2; i <= n; i++) {
    [a, b] = [b, a + b];
  }
  return b;
}

const results = {
  sum: add(10, 5),
  diff: subtract(10, 5),
  product: multiply(4, 7),
  quotient: divide(20, 4),
  squared: power(3, 2),
  fact5: factorial(5),
  prime17: isPrime(17),
  fib10: fibonacci(10),
};

console.log(results);
