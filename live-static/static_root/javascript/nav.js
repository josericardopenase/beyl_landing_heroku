window.onload = () => {

    const hmenu = document.getElementById("h-menu")
    const imenu = document.getElementById("mobile-menu")

    
    hmenu.onclick = () => {
       hmenu.classList.toggle("h-active")
       imenu.classList.toggle("d-flex")
       document.body.classList.toggle("overflow-hidden")

    }

    console.log("hello")

// Set the date we're counting down to


    /* const header = document.getElementById('header')
    header.onclick = () => console.log("he clicado")

    onscroll = () => {

        console.log(scrollY)
        
        if(scrollY > 120){
            header.style.position = "fixed";
            header.style.backgroundColor = "white";
            header.style.zIndex = 300;
        }
        if(scrollY < 120){
            console.log("cambiamos")
            header.style.position = "absolute";
            header.style.backgroundColor = "transparent";
        }
    } */
}

var countDownDate = new Date("Jan 5, 2021 15:37:25").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = ("0" + Math.floor(distance / (1000 * 60 * 60 * 24))).slice(-2);
  var hours = ("0" + Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))).slice(-2);
  var minutes = ("0" + Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60))).slice(-2);
  var seconds = ("0" + Math.floor((distance % (1000 * 60)) / 1000)).slice(-2);

  // Display the result in the element with id="demo"
  document.getElementById("timer").innerHTML = days + " : " + hours + " : "
  + minutes + " : " + seconds;

  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("timer").innerHTML = "EXPIRED";
  }
}, 1000);