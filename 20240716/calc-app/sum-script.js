function calculateSum() {
    //alert("hi programmer")
    const first_box = document.getElementById("first");
    const second_box = document.getElementById("second");
    const result_box = document.getElementById("result");
    const answer_tag = document.getElementById("answer");

    const first = parseInt(first_box.value);
    const second = parseInt(second_box.value);
    const result = first + second;
    result_box.value = result;
    answer_tag.innerHTML = `sum of ${first} and ${second} is ${result}`
}