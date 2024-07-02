const Settings = {
    host: 'https://ishutin.akulon.codenoobs.ru/api'
}

function onSendRegDataClick() {
    let login = document.getElementById("login").value;
    let password = document.getElementById("password").value;
    let confirm_password = document.getElementById("confirm_password").value;
    if (password != confirm_password){
        let message_element = document.getElementById('flash')
        message_element.innerText = 'Пароль не верный'
        message_element.classList.add('error')
        console.log("Пароль не верный")
        return
    }
    fetch(`${Settings.host}/register`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({'login': login, 'password': password})
    }).then(r => r.json()).then(r => {
        if (r.result==='success'){
            location = 'login.html'
        }
        else{
            let message_element = document.getElementById('flash')
            message_element.innerText = r.message
            message_element.classList.add(r.result)
        }
        // resolve(r)
    }).catch(error => {
        // reject(error)
    });
}

function onSendLogDataClick() {
    let login = document.getElementById("login").value;
    let password = document.getElementById("password").value;
    fetch(`${Settings.host}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({'login': login, 'password': password})
    }).then(r => r.json()).then(r => {
        if (r.result==='success'){
            location = '/enter.html?login='+login
        }
        else{
            let message_element = document.getElementById('flash')
            message_element.innerText = r.message
            message_element.classList.add(r.result)
        }
        // resolve(r)
    }).catch(error => {
        // reject(error)
    });
}
let URLParams = []
function parseURLParams() {
    const urlRawParams = window.location.search.split('&')
    for (const paramName in urlRawParams) {
        const paramParts = urlRawParams[paramName].split('=')
        URLParams[paramParts[0].replace('?', '')] = paramParts[1]
    }
}
parseURLParams()