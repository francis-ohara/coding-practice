// Question 1
let textarea = document.getElementById("textInput");
let paragraph = document.getElementById("wordCount");

textarea.addEventListener("input", () => {
    let numberOfWords = textarea.value.split(" ").length;
    paragraph.textContent = "Words: " + numberOfWords;
})

// Question 2
let inputBox = document.getElementById("textInput");
let submitBtn = document.getElementById("submitButton");

inputBox.addEventListener("input", () => {
    let charCount = inputBox.value.length;

    if (charCount >= 10) {
        submitBtn.disabled = false;
    }
});
