// vedio Popup functionality
const videoCards = document.querySelectorAll('.video-card');
const popupOverlay = document.querySelector('.popup-overlay');
const popupIframe = document.querySelector('.popup-content iframe');
const closePopupBtn = document.querySelector('.close-popup');

videoCards.forEach(card => {
    card.addEventListener('click', () => {
        const videoSrc = card.getAttribute('data-video');
        popupIframe.src = videoSrc;
        popupOverlay.classList.add('active');
    });
});

closePopupBtn.addEventListener('click', () => {
    popupOverlay.classList.remove('active');
    popupIframe.src = ''; // Stop the video
});

popupOverlay.addEventListener('click', (e) => {
    if (e.target === popupOverlay) {
        popupOverlay.classList.remove('active');
        popupIframe.src = ''; // Stop the video
    }
});
// Cpp functionality
function runCode() {
            const outputBlock = document.getElementById('output-block');
            outputBlock.innerHTML = "<p>Hello C++ Programming</p>";
}

 // JavaScript Functions for dynamic output
function runHelloWorld() {
    document.getElementById('output-hello-world').innerText = "Hello, World!";
}

function runVariables() {
    const x = 5;
    const y = 10;
    const z = 15;
    document.getElementById('output-variables').innerText = `${x} ${y} ${z}`;
}

function runLoop() {
    let result = '';
    for (let i = 0; i < 5; i++) {
    result += `${i}\n`;
    }
    document.getElementById('output-loop').innerText = result.trim();
}

function runArray() {
    const fruits = ["Apple", "Banana", "Cherry"];
     fruits.push("Date");
     document.getElementById('output-array').innerText = JSON.stringify(fruits);
}
   //   SQL Query Output
function runSQLQuery() {
    const queryOutput = "id | name    | age\n---+---------+----\n 1 | John    | 25\n 2 | Alice   | 30\n 3 | Michael | 35";
    document.getElementById('output-sql-query').innerText = queryOutput;
}
 //  PHP Output
function runPHPExample1() {
    document.getElementById('output-php-hello').innerText = "Hello, PHP!";
}

function runPHPVariables() {
    const name = "John";
    const age = 30;
    document.getElementById('output-php-variables').innerText = `Name: ${name}, Age: ${age}`;
}

function runPHPConditional() {
    const num = 10;
    const result = num % 2 === 0 ? "Even" : "Odd";
    document.getElementById('output-php-conditional').innerText = `The number ${num} is ${result}`;
}