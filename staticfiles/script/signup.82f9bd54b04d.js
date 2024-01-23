function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var number = document.getElementById("number").value;
    var p1 = document.getElementById("p1").value;
    var p2 = document.getElementById("p2").value;

    if (name === "" || email === ""|| p1 === ""||p2==="") {
      document.getElementById('error1').innerHTML="All fields must be filled out"  
    return false
    } 
    else if(p1.length<6) {
        document.getElementById('error1').innerHTML="password must be atleast 6 characters"
    return false
    }
    else if(p1!==p2){
        document.getElementById('error1').innerHTML="password must be same"
    return false  
    }
    else{
        return true
    }
}