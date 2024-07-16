var first = '', second = '', operator = '';

function calc(val) {
    const box = document.getElementById('result');
    if( val == '=' ) {
        let result = eval(`${first} ${operator} ${second}`);
        first = result; second = ''; operator ='';
    } else if( val == '+' || val == '-' || val == '*' || val == '/' ) {
        operator = val;
    } else if( val == 'C' ) {
        first = ''; operator = ''; second = '';
    } else {
        if(operator == '') 
            first += val; 
        else 
            second += val; 
    } 
    let display = `${first} ${operator} ${second}`
    display = display.trim();
    if(display == '') display = '0';
    box.value = display;
}

/*
function calc(val) {
    const box = document.getElementById('result');
    if( val == '=' ) {
        let result, ifirst = parseInt(first), isecond = parseInt(second);
        if( operator == '+') { 
            result = ifirst + isecond;
        } else if( operator == '-') {
            result = ifirst - isecond;
        }else if( operator == '*') { 
            result = ifirst * isecond;
        } else if( operator == '/') {
            result = parseInt(ifirst / isecond);
        }
        first = result; second = ''; operator ='';
    } else if( val == '+' || val == '-' || val == '*' || val == '/' ) {
        operator = val;
    } else if( val == 'C' ) {
        first = ''; operator = ''; second = '';
    } else {
        if(operator == '') 
            first += val; 
        else 
            second += val; 
    } 
    let display = `${first} ${operator} ${second}`
    display = display.trim();
    if(display == '') display = '0';
    box.value = display;
}
*/