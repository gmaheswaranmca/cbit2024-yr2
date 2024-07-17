var count = 0;
function increment() {
    count++;
    document.getElementById('counter-display').innerHTML = count;
}
function decrement() {
    count--;
    document.getElementById('counter-display').innerHTML = count;
}
