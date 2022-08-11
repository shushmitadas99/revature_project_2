let sBtn = document.getElementById('sBtn');
let tBtn = document.getElementById('tBtn');

sBtn.addEventListener('click', stdLogin);
tBtn.addEventListener('click', tchLogin);

function stdLogin(){

      window.location.href="./s_login.html"
}

function tchLogin(){

      window.location.href="./t_login.html"
}