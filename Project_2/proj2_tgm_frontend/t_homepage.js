
let t_id = sessionStorage.getItem('t_id')
let t_username = sessionStorage.getItem("username");
let viewCButton = document.getElementById('viewC');
let viewAButton = document.getElementById('viewA');
console.log(t_id)
if(viewCButton){
    viewCButton.addEventListener('click', t_view_courses)
}
 
function t_view_courses(){
    console.log(t_username)
    console.log(t_id)
    window.location.href = '/t_view_courses.html'
};
 
if(viewAButton){
    viewAButton.addEventListener('click',t_view_assignments)
}

function t_view_assignments(){
    window.location.href = '/t_view_assignments.html'
}

