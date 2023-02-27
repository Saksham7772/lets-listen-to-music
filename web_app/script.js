
const form = {
    text: document.getElementById('ad__text'),
    button_title: document.getElementById('ad__button_title'),
    button_url: document.getElementById('ad__button_url'),
    view_limit: document.getElementById('ad__view_limit'),
    button: document.querySelector('.button'),
}

function handleInput(e, name) {
    const { value } = e.target
    if (value) {
        form[name].classList.add('filed')
    } else {
        form[name].classList.remove('filed')
    }
}

form.text.oninput = (e) => handleInput(e, 'text')
form.button_title.oninput = (e) => handleInput(e, 'button_title')
form.button_url.oninput = (e) => handleInput(e, 'button_url')
form.view_limit.oninput = (e) => handleInput(e, 'view_limit')
