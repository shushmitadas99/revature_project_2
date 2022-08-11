let s_id = sessionStorage.getItem('s_id')
let s_username = sessionStorage.getItem("username");

window.addEventListener('load', s_course_window_load);

async function s_course_window_load(){
    let res = await fetch(`http://127.0.0.1:8080/slogin/${s_id}/c`, {
        headers: {
          'Accept': 'application/json'
        }
      });
    // if (res == 200){
        let data = await res.json(); // res.json() returns a promise
        console.log(data["courses"]); //accessing data using courses as key
        courses_details_array = data["courses"] //saving variable as array
        for (let courses of courses_details_array){ //looping over array and each element is a dictionary
            console.log(courses);
            s_course(courses);
        }
    // }
    
}

function s_course(courses){
    let sViewCourseBodyElement = document.querySelector('#s-course-data-output');
    let row = document.createElement('tr');

    // let cIdCell = document.createElement('td');
    // cIdCell.innerHTML = courses.c_id;

    let cNameCell = document.createElement('td');
    cNameCell.innerHTML = courses.c_name;

    let cDescCell = document.createElement('td');
    cDescCell.innerHTML = courses.c_desc;

    let tNameCell = document.createElement('td');
    tNameCell.innerHTML = courses.t_name;

    let tEmailCell = document.createElement('td');
    tEmailCell.innerHTML = courses.t_email;

    // row.appendChild(cIdCell);
    row.appendChild(cNameCell);
    row.appendChild(cDescCell);
    row.appendChild(tNameCell);
    row.appendChild(tEmailCell);
    
    sViewCourseBodyElement.appendChild(row);
}