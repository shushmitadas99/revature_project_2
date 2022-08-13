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

    // let cSelectCell = document.createElement('td');
    // cSelectCell.innerHTML = courses.t_email;

    // var label1 = document.createElement('label'); //******************* */
    // label1.htmlFor = 'Approved';
    // label1.innerHTML = 'Approve ';

    var checkbox1 = document.createElement('input');
    checkbox1.setAttribute('type', 'checkbox');
    // radioInput1.setAttribute('name', "status_radio");
    checkbox1.setAttribute('id', courses.c_id);
    checkbox1.setAttribute('value', courses.c_id);

    checkbox1.addEventListener("click", sush)
   
    //  checkbox1.addEventListener("click", sush)


    // row.appendChild(cIdCell);
    row.appendChild(cNameCell);
    row.appendChild(cDescCell);
    row.appendChild(tNameCell);
    row.appendChild(tEmailCell);
    row.appendChild(checkbox1);

    sViewCourseBodyElement.appendChild(row);

    async function sush(){
        sessionStorage.setItem("c_id", checkbox1.value)
        let c_id = sessionStorage.getItem("c_id");
        console.log(c_id);

        // let c_id = sessionStorage.setItem(checkbox1.value);
        // console.log(c_id);

        let res = await fetch(`http://127.0.0.1:8080/slogin/${s_id}/c/${c_id}/a`, {
              'credentials': 'include',
              'method': 'POST',
              'headers': {'Content-Type': 'application/json'},
              'body': JSON.stringify({
                  "grade": null
              })
            }) 
            window.alert("Your assignment was submitted. Please visit'View Assignments' page to view all your assignments.");
            window.location.href = '/s_homepage.html'
            // if (res.status == 200)
            // {}
      }
}