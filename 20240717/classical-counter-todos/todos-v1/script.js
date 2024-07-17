var todos = [];
function add(){
    const item = document.getElementById('todo-item').value;
    todos.push(item); displayToDos();
    document.getElementById('todo-item').value = '';
    document.getElementById('todo-item').focus();
} 

function displayToDos() {
    let rows = '', I=1;
    for(let item of todos){
        rows += `<tr>  <td>${I}</td> <td>${item}</td> 
            <td> <button class="btn btn-danger" 
                onclick="deleteTodo(${I-1});">delete</button> 
                </td> </tr>`;
        I++;
    }
    let table = `<table class="table table-bordered">
    <tr> <th>#</th>  <th>todo item</th> <th></th> </tr>
    ${rows} </table> `;
    document.getElementById('items').innerHTML = table;
} 

function deleteTodo(index) { 
    todos.splice(index,1); /* remove at index 1 element */ 
    displayToDos();
}