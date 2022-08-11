let sBtn = document.getElementById('sBtn');
let tBtn = document.getElementById('tBtn');

sBtn.addEventListener('click', stdLogin);

function stdLogin(){

      window.location.href="./s_login.html"
}



tBtn.addEventListener('click', tchLogin);

function tchLogin(){

      window.location.href="./t_login.html"
}