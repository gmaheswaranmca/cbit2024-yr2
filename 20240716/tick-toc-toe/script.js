var cells = ['','','', '','','', '','','']
var turn = 'X', winner = '';
function play(cellIndex){
    if(winner != ''){ alert('Board is played.'); return; }
    if(cells[cellIndex] != ''){ return; } //is played
    cells[cellIndex] = turn;
    turn = (turn == 'X' ? 'O' : 'X'); //turn is given to another player
    winner = whoIsWinner();
    loadBoard();//once cell is changed, load the board
}
function restart() {
    turn = 'X'; winner = '';
    cells = ['','','', '','','', '','',''];
    loadBoard(); // initial board display
}
function loadBoard(){
    for(let I=0; I<9;I++) {
        document.getElementById("box" + (I+1)).innerHTML = cells[I];
    }
    const msgText = `Turn:<span id="turn">${turn}</span><br/>
    Winner:${winner==''?'Playing...':(winner=='D'?'Draw':winner)}`
    document.getElementById("msg").innerHTML = msgText;    
}
function whoIsWinner() { //for winner returns 'X' or 'O'; for draw returns 'D'; else returns ''
    /*const matrix = [[cells[0], cells[1], cells[2]],
                    [cells[3], cells[4], cells[5]],
                    [cells[6], cells[7], cells[8]]]*/
    const winLines = [[0,1,2], [3,4,5], [6,7,8], /* rows */
                    [0,3,6], [1,4,7], [2,5,8], /* cols */
                    [0,4,8], [2,4,6] ]         /* diagonals */
    for(let [left,mid,right] of winLines){
        if(cells[left] !='' && 
            cells[left] == cells[mid] && 
            cells[mid] == cells[right]) { return cells[left]; }
    }
    const cellsPlayedCount = cells.reduce(function(count,eCell){
        return count + (eCell==''?0:1);
        },0);
    return cellsPlayedCount == 9 ? 'D' : '';
}
