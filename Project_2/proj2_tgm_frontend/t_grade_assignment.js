let t_id = sessionStorage.getItem('t_id')
let t_username = sessionStorage.getItem("username");
let c_id = sessionStorage.getItem('c_id');
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
    let tViewCourseBodyElement = document.querySelector('#t-course-data-output');
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

    var label1 = document.createElement('label')
    label1.htmlFor = 'A';
    label1.innerHTML = 'A ';
    var radioInput1 = document.createElement('input');
    radioInput1.setAttribute('type', 'radio');
    radioInput1.setAttribute('name', "grade_radio");
    radioInput1.setAttribute('id', assignments.assn);
    radioInput1.setAttribute('value', 'A');
    // var newline1 = document.createElement('br');
    // label1.appendChild(newline1);
    label1.appendChild(radioInput1);
  
    radioInput1.addEventListener("click", ()=>{
      assn = assignments.assn;
      //  gradeCell.innerHTML = "A";
       grade = "A";
      
    })
    radioInput1.addEventListener("click", sush)
    
    var newline1 = document.createElement('br');
    label1.appendChild(newline1);

   //-----------------------------------------------------------------

   var label2 = document.createElement('label')
   label2.htmlFor = 'A';
   label2.innerHTML = 'A ';
   var radioInput2 = document.createElement('input');
   radioInput2.setAttribute('type', 'radio');
   radioInput2.setAttribute('name', "grade_radio");
   radioInput2.setAttribute('id', assignments.assn);
   radioInput2.setAttribute('value', 'B');
   // var newline1 = document.createElement('br');
   // label1.appendChild(newline1);
   label1.appendChild(radioInput1);
 
   radioInput1.addEventListener("click", ()=>{
     assn = assignments.assn;
     //  gradeCell.innerHTML = "A";
      grade = "A";
     
   })
   radioInput1.addEventListener("click", sush)
   
   var newline1 = document.createElement('br');
   label1.appendChild(newline1);

  //-----------------------------------------------------------------

  var label1 = document.createElement('label')
  label1.htmlFor = 'A';
  label1.innerHTML = 'A ';
  var radioInput1 = document.createElement('input');
  radioInput1.setAttribute('type', 'radio');
  radioInput1.setAttribute('name', "grade_radio");
  radioInput1.setAttribute('id', assignments.assn);
  radioInput1.setAttribute('value', 'A');
  // var newline1 = document.createElement('br');
  // label1.appendChild(newline1);
  label1.appendChild(radioInput1);

  radioInput1.addEventListener("click", ()=>{
    assn = assignments.assn;
    //  gradeCell.innerHTML = "A";
     grade = "A";
    
  })
  radioInput1.addEventListener("click", sush)
  
  var newline1 = document.createElement('br');
  label1.appendChild(newline1);

 //-----------------------------------------------------------------

 var label1 = document.createElement('label')
 label1.htmlFor = 'A';
 label1.innerHTML = 'A ';
 var radioInput1 = document.createElement('input');
 radioInput1.setAttribute('type', 'radio');
 radioInput1.setAttribute('name', "grade_radio");
 radioInput1.setAttribute('id', assignments.assn);
 radioInput1.setAttribute('value', 'A');
 // var newline1 = document.createElement('br');
 // label1.appendChild(newline1);
 label1.appendChild(radioInput1);

 radioInput1.addEventListener("click", ()=>{
   assn = assignments.assn;
   //  gradeCell.innerHTML = "A";
    grade = "A";
   
 })
 radioInput1.addEventListener("click", sush)
 
 var newline1 = document.createElement('br');
 label1.appendChild(newline1);

//-----------------------------------------------------------------



    row.appendChild(aIDCell);
    row.appendChild(cNameCell);
    row.appendChild(cDescCell);
    row.appendChild(sNameCell);
    row.appendChild(gradeCell);
    row.appendChild(submittedCell);
    row.appendChild(gradeTimeCell);
    row.appendChild(label1);
    row.appendChild(label2);
    row.appendChild(label3);
    row.appendChild(label4);

    // row.appendChild(checkbox1);

    tViewCourseBodyElement.appendChild(row);


    


    // let cSelectCell = document.createElement('td');
    // cSelectCell.innerHTML = courses.t_email;

    // var label1 = document.createElement('label'); //******************* */
    // label1.htmlFor = 'Approved';
    // label1.innerHTML = 'Approve ';

    // var checkbox1 = document.createElement('input');
    // checkbox1.setAttribute('type', 'checkbox');
    // // radioInput1.setAttribute('name', "status_radio");
    // checkbox1.setAttribute('id', courses.c_id);
    // checkbox1.setAttribute('value', courses.c_id);

    // checkbox1.addEventListener("click", sush)
   
    //  checkbox1.addEventListener("click", sush)


    // row.appendChild(cIdCell);
    // row.appendChild(cNameCell);
    // row.appendChild(cDescCell);
    // row.appendChild(tNameCell);
    // row.appendChild(tEmailCell);
    // row.appendChild(checkbox1);

    // sViewCourseBodyElement.appendChild(row);

    async function sush(){
        // sessionStorage.setItem("c_id", c_id)
        // let c_id = sessionStorage.getItem("c_id");
        // console.log(c_id);

        // let c_id = sessionStorage.setItem(checkbox1.value);
        // console.log(c_id);

        let res = await fetch(`http://127.0.0.1:8080/tlogin/${t_id}/c/${c_id}/a`, {
              'credentials': 'include',
              'method': 'PUT',
              'headers': {'Content-Type': 'application/json'},
              'body': JSON.stringify({
                  "grade": grade
              })
            }) 
            console.log(c_id);
            console.log(t_id);
            console.log(grade);
            window.alert("Your assignment graded. ");
            window.location.href = '/t_homepage.html'
            // if (res.status == 200)
            // {}
      }
}


