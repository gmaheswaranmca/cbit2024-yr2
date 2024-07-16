function calcSquare() {
    calc(1);
} function calcCube() {
    calc(2);
} function calc(menu) {
    const num_box = document.getElementById("num");
    const result_box = document.getElementById("result");
    const answer_tag = document.getElementById("answer");
    const caption_tag = document.getElementById("caption");
    const num = parseInt(num_box.value);
    let result;
    switch(menu) {
        case 1:
            result = num * num;            
            answer_tag.innerHTML = `square of ${num} is ${result}`
            caption_tag.innerHTML ='Square'; break;
        case 2:
            result = num * num * num;            
            answer_tag.innerHTML = `cube of ${num} is ${result}`
            caption_tag.innerHTML ='Cube'; break;
    }
    result_box.value = result;
}