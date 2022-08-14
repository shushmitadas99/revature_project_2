let t_id = sessionStorage.getItem('t_id');
let t_name = sessionStorage.getItem('t_name');
let t_username = sessionStorage.getItem("username");
let t_email = sessionStorage.getItem('t_email');

window.addEventListener('load', user_window_load);

function user_window_load(){
    console.log(t_name);
    let stdIDP = document.getElementById('tch_id');
    stdIDP.innerHTML = t_id;
    
    let stdName = document.getElementById('tch_name');
    stdName.innerHTML = t_name;

    let stdUsername = document.getElementById('tch_username');
    stdUsername.innerHTML = t_username;

    let stdEmail = document.getElementById('tch_email');
    stdEmail.innerHTML = t_email;
}

