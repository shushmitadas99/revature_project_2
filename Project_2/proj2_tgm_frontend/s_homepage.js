let s_id = sessionStorage.getItem('s_id')
let s_username = sessionStorage.getItem("username");
let viewCButton = document.getElementById('viewC');

if(viewCButton){
    viewCButton.addEventListener('click', s_view_courses)
}
 
function s_view_courses(){
    console.log(s_username)
    console.log(s_id)
    window.location.href = '/s_view_courses.html'
};
