var cells = ['','','', '','','', '','','']

var turn = 'X';
function play(cellIndex){
    if(cells[cellIndex] != ''){
        return;
    }
    cells[cellIndex] = turn;
    turn = (turn == 'X' ? 'O' : 'X');
    for(let I=0; I<9;I++) {
        const name = "box" + (I+1);
        const box_tag = document.getElementById(name);
        box_tag.innerHTML = cells[I];
    }
}
function clear() {
    for(let I=0; I<9;I++) {
        const name = "box" + (I+1);
        const box_tag = document.getElementById(name);
        box_tag.innerHTML = cells[I];
    }
}
