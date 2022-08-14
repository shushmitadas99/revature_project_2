let tUsernameLoginInput = document.querySelector("#t-username-login-input")
let tPasswordLoginInput = document.querySelector('#t-password-login-input');
let tLoginButton = document.getElementById('t-login-btn');

if(tLoginButton){
    tLoginButton.addEventListener('click', get_all_details)
}
 

async function get_all_details(){
    let res = await fetch('http://127.0.0.1:8080/tlogin', {
        'credentials': 'include',
        'method': 'POST',
        'headers': {'Content-Type': 'application/json'},
        'body': JSON.stringify({
            "username": tUsernameLoginInput.value,
            "password": tPasswordLoginInput.value
        })
    }) 

     if (res.status == 200)
    { 
        let data = await res.json();
        console.log("Logged in!")
        console.log(data);

        sessionStorage.setItem("t_id", data.t_id)
        let t_id = sessionStorage.getItem('t_id')
        console.log(t_id);

        sessionStorage.setItem("t_name", data.t_name)
        let t_name = sessionStorage.getItem('t_name')
        console.log(t_name);

        sessionStorage.setItem("t_email", data.t_email)
        let t_email = sessionStorage.getItem('t_email')
        console.log(t_email);

        sessionStorage.setItem("username", tUsernameLoginInput.value)
        let t_username = sessionStorage.getItem("username");
        console.log(t_username);


        window.location.href = '/t_homepage.html'

    }
};