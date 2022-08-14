let t_id = sessionStorage.getItem('t_id')
let t_username = sessionStorage.getItem("username");
let c_id = sessionStorage.getItem('c_id');
let viewCButton = document.getElementById('viewC');
let viewAButton = document.getElementById('viewA');
let gradeAButton = document.getElementById('gradeA');
let viewPButton = document.getElementById('viewP');

if(viewCButton){
    viewCButton.addEventListener('click', t_view_courses)
}

if(viewAButton){
    viewAButton.addEventListener('click', t_view_assignments)
}

if(gradeAButton){
    gradeAButton.addEventListener('click', t_grade_assignment)
}

if(viewPButton){
    viewPButton.addEventListener('click', t_view_t_profile)
}
 
function t_view_courses(){
    console.log(t_username)
    console.log(t_id)
    window.location.href = '/t_view_courses.html'
};

function t_view_assignments(){
    console.log(t_username)
    console.log(t_id)
    console.log(c_id)
    window.location.href = '/t_view_assignments.html'
};

function t_grade_assignment(){
    console.log(t_username)
    console.log(t_id)
    console.log(c_id)
    window.location.href = '/t_grade_assignment.html'
};

function t_view_t_profile(){
    console.log(t_username)
    console.log(t_id)
    window.location.href = '/t_view_profile.html'
};


let logoutBtn = document.getElementById('logout');

logoutBtn.addEventListener('click', logOut);

async function logOut(){
  console.log("in logout");
  let res = await fetch('http://127.0.0.1:8080/tlogout', {
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