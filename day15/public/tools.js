var x = document.cookie;
function login(data){
    status_login = data
    console.log(status_login)
    if (String(status_login) == "1")
        window.location.href = './home.html'
    }

function app1(){ 
    user = document.getElementById("user") 
    password = document.getElementById("password")
    link = 'http://192.168.1.103:5000/1?user='+user+"&password="+password
    fetch(link)
    .then(request => request.text())
    .then(data => login(data))
}
