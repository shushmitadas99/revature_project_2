let sUsernameLoginInput = document.querySelector("#s-username-login-input")
let sPasswordLoginInput = document.querySelector('#s-password-login-input');
let sLoginButton = document.getElementById('s-login-btn');

if(sLoginButton){
    sLoginButton.addEventListener('click', get_all_details)
}
 

async function get_all_details(){
    let res = await fetch('http://127.0.0.1:8080/slogin', {
        'credentials': 'include',
        'method': 'POST',
        'headers': {'Content-Type': 'application/json'},
        'body': JSON.stringify({
            "username": sUsernameLoginInput.value,
            "password": sPasswordLoginInput.value
        })
    }) 

     if (res.status == 200)
    { 
        let data = await res.json();
        console.log("Logged in!")
        console.log(data);

        sessionStorage.setItem("s_id", data.s_id)
        let s_id = sessionStorage.getItem('s_id')
        console.log(s_id);

        sessionStorage.setItem("s_email", data.s_email)
        let s_email = sessionStorage.getItem('s_email')
        console.log(s_email);

        sessionStorage.setItem("username", sUsernameLoginInput.value)
        let s_username = sessionStorage.getItem("username");
        console.log(s_username);


        window.location.href = '/s_homepage.html'

    }
};