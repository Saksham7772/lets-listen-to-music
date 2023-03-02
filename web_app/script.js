
// TELEGRAM
let tg = window.Telegram.WebApp;
//tg.expand();

tg.MainButton.text = 'Отправить'
//tg.MainButton.color = '#'


// FORM
let formData = {};
const form = document.querySelector('form');

form.addEventListener('input', function(event){
    formData[event.target.name] = event.target.value;
});

form.addEventListener('submit', async function(event){
    event.preventDefault();
    form.classList.add('_sending');

    tg.MainButton.show();
});


Telegram.WebApp.onEvent('mainButtonClicked', function(){
    tg.sendData(JSON.stringify(formData));
});
