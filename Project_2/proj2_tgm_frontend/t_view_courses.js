 let t_id = sessionStorage.getItem('t_id')
let t_username = sessionStorage.getItem("username");
console.log(t_id)

window.addEventListener('load', t_course_window_load);

async function t_course_window_load(){
    let res = await fetch(`http://127.0.0.1:8080/tlogin/${t_id}/c`, {
        headers: {
          'Accept': 'application/json'
        }
      });
    // if (res == 200){
        let data = await res.json(); // res.json() returns a promise
        // sessionStorage.setItem("c_id", data.c_id)
        // let c_id = sessionStorage.getItem('c_id')
        // console.log("course_id" + c_id);

        console.log(data["courses"]); //accessing data using courses as key
        courses_details_array = data["courses"] //saving variable as array
        for (let courses of courses_details_array){ //looping over array and each element is a dictionary
            console.log(courses);
            t_course(courses);
            sessionStorage.setItem("c_id", courses.c_id)
        let c_id = sessionStorage.getItem('c_id')
        console.log("course_id" + c_id);
        }
    // }

    
}

function t_course(courses){
    let tViewCourseBodyElement = document.querySelector('#t-course-data-output');
    let row = document.createElement('tr');

    // let cIdCell = document.createElement('td');
    // cIdCell.innerHTML = courses.c_id;

    let cNameCell = document.createElement('td');
    cNameCell.innerHTML = courses.c_name;

    let cDescCell = document.createElement('td');
    cDescCell.innerHTML = courses.c_desc;

    let sNameCell = document.createElement('td');
    sNameCell.innerHTML = courses.s_name;

    let sEmailCell = document.createElement('td');
    sEmailCell.innerHTML = courses.s_email;

    row.appendChild(cNameCell);
    row.appendChild(cDescCell);
    row.appendChild(sNameCell);
    row.appendChild(sEmailCell);

    tViewCourseBodyElement.appendChild(row);


}