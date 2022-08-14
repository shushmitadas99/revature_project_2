let t_id = sessionStorage.getItem('t_id');
let s_username = sessionStorage.getItem("username");
let c_id = sessionStorage.getItem('c_id');
// let tBody = document.getElementById('s-course-data-output');
let tViewCourseBodyElement = document.querySelector('#t-course-data-output');

window.addEventListener('load', t_course_window_load);

async function t_course_window_load(){
    console.log(c_id);
    let res = await fetch(`http://127.0.0.1:8080/tlogin/${t_id}/c/${c_id}/a`, {
        headers: {
          'Accept': 'application/json'
        }
      });
    // if (res == 200){
        let data = await res.json(); // res.json() returns a promise
        console.log(data["assignments"]); //accessing data using courses as key
        assignment_details_array = data["assignments"] //saving variable as array
        for (let assignments of assignment_details_array){ //looping over array and each element is a dictionary
            console.log(assignments);
            t_course(assignments);
        }
    // }
    
}


function t_course(assignments){
    // let sViewCourseBodyElement = document.querySelector('#s-course-data-output');
    let row = document.createElement('tr');

    // let cIdCell = document.createElement('td');
    // cIdCell.innerHTML = courses.c_id;

    let aIDCell = document.createElement('td');
    aIDCell.innerHTML = assignments.assn;

    let cNameCell = document.createElement('td');
    cNameCell.innerHTML = assignments.c_name;

    let cDescCell = document.createElement('td');
    cDescCell.innerHTML = assignments.c_desc;

    let sNameCell = document.createElement('td');
    sNameCell.innerHTML = assignments.s_name;

    let gradeCell = document.createElement('td');
    gradeCell.innerHTML = assignments.grade;

    let submittedCell = document.createElement('td');
    submittedCell.innerHTML = assignments.submitted;

    let gradeTimeCell = document.createElement('td');
    gradeTimeCell.innerHTML = assignments.grade_time;

    row.appendChild(aIDCell);
    row.appendChild(cNameCell);
    row.appendChild(cDescCell);
    row.appendChild(sNameCell);
    row.appendChild(gradeCell);
    row.appendChild(submittedCell);
    row.appendChild(gradeTimeCell);
    // row.appendChild(checkbox1);

    tViewCourseBodyElement.appendChild(row);
}
