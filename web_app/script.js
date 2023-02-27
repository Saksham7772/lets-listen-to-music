
const form = {
    text: document.getElementById('ad__text'),
    button_title: document.getElementById('ad__button_title'),
    button_url: document.getElementById('ad__button_url'),
    view_limit: document.getElementById('ad__view_limit'),

    button: document.querySelector('.button'),
}

function checkForm() {
    const text = form.text.getElementsByTagName('input')[0].value
    const button_title = form.button_title.getElementsByTagName('input')[0].value
    const button_url = form.button_url.getElementsByTagName('input')[0].value
    const view_limit = form.view_limit.getElementsByTagName('input')[0].value

    if (text && button_title && button_url && view_limit) {
        form.button.classList.remove('disable')
    } else {
        form.button.classList.add('disable')
    }
}

function handleInput(e, name) {
    const { value } = e.target
    if (value) {
        form[name].classList.add('filed')
    } else {
        form[name].classList.remove('filed')
    }
    checkForm()
}

form.text.oninput = (e) => handleInput(e, 'text')
form.button_title.oninput = (e) => handleInput(e, 'button_title')
form.button_url.oninput = (e) => handleInput(e, 'button_url')
form.view_limit.oninput = (e) => handleInput(e, 'view_limit')

form.button.onclick = () => alert('Done')
