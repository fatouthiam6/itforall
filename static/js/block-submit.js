let form = document.querySelector(".answer");
form.addEventListener("submit", e => {
    let input = form.querySelector("#answer-input");
    if (input.value.length < 1){
        e.preventDefault();
    }
})