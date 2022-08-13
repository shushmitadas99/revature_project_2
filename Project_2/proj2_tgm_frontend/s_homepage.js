let s_id = sessionStorage.getItem('s_id')
let s_username = sessionStorage.getItem("username");
let c_id = sessionStorage.getItem('c_id');
let viewCButton = document.getElementById('viewC');
let viewAButton = document.getElementById('viewA');
let submitAButton = document.getElementById('submitA');
let viewPButton = document.getElementById('viewP');

if(viewCButton){
    viewCButton.addEventListener('click', s_view_courses)
}

if(viewAButton){
    viewAButton.addEventListener('click', s_view_assignments)
}

if(submitAButton){
    submitAButton.addEventListener('click', s_submit_assignment)
}

if(viewPButton){
    viewPButton.addEventListener('click', s_view_s_profile)
}
 
function s_view_courses(){
    console.log(s_username)
    console.log(s_id)
    window.location.href = '/s_view_courses.html'
};

function s_view_assignments(){
    console.log(s_username)
    console.log(s_id)
    console.log(c_id)
    window.location.href = '/s_view_assignments.html'
};

function s_submit_assignment(){
    console.log(s_username)
    console.log(s_id)
    console.log(c_id)
    window.location.href = '/s_submit_assignment.html'
};

function s_view_s_profile(){
    console.log(s_username)
    console.log(s_id)
    window.location.href = '/s_view_profile.html'
};


let logoutBtn = document.getElementById('logout');

logoutBtn.addEventListener('click', logOut);

async function logOut(){
  console.log("in logout");
  let res = await fetch('http://127.0.0.1:8080/slogout', {
        'credentials': 'include',
        'method': 'POST',
        'headers': {'Content-Type': 'application/json'},

    })
    
    if (res.status == 200){
      let data = await res.json();
      console.log(data);
      window.location.href="./index.html"
  }
}