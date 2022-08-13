let s_id = sessionStorage.getItem('s_id');
let s_name = sessionStorage.getItem('s_name');
let s_username = sessionStorage.getItem("username");
let s_email = sessionStorage.getItem('s_email');

window.addEventListener('load', user_window_load);

function user_window_load(){
    console.log(s_name);
    let stdIDP = document.getElementById('std_id');
    stdIDP.innerHTML = s_id;
    
    let stdName = document.getElementById('std_name');
    stdName.innerHTML = s_name;

    let stdUsername = document.getElementById('std_username');
    stdUsername.innerHTML = s_username;

    let stdEmail = document.getElementById('std_email');
    stdEmail.innerHTML = s_email;
}

