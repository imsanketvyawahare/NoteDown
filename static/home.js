$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.parallax').parallax();
});


const btn = document.getElementById("slider")
const slider1 = document.getElementById("slider1")
const slider2 = document.getElementById("slider2")

btn.addEventListener("click",()=>{
  if(slider2.style.display == "none"){
    slider1.style.display = "none";
    slider2.style.display = "block";
  }
  else{
    slider1.style.display = "block";
    slider2.style.display = "none";
  }
})

