window.onload = () => {

    const hmenu = document.getElementById("h-menu")
    const imenu = document.getElementById("mobile-menu")

    
    hmenu.onclick = () => {
       hmenu.classList.toggle("h-active")
       imenu.classList.toggle("d-flex")
       document.body.classList.toggle("overflow-hidden")

    }


}

var countDownDate = new Date("Jan 5, 2021 15:37:25").getTime();
var flag = false;
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
  var fixedHeader = document.getElementById('fixed-header')
  // Display the result in the element with id="demo"
  Array.from(document.getElementsByClassName("timer")).map(x=> x.innerHTML = days + " d " + hours + " h "
  + minutes + " m " + seconds + " s ");


  // If the count down is finished, write some text
  if (distance < 0) {
    clearInterval(x);
    Array.from(document.getElementsByClassName("timer")).map(x => x.innerHTML = "EXPIRED");



  }
}, 1000);

window.onscroll = function() {myFunction()};

function myFunction() {

    var fixedHeader = document.getElementById('fixed-header')

    if(document.body.scrollTop>200){
        fixedHeader.classList.add('d-flex')
        fixedHeader.classList.remove('d-none')
        if(flag === false){

            flag = true;

            document.getElementById("fixed-header").animate([
                // keyframes
                { transform: 'translateY(-300px)' }, 
                { transform: 'translateY(0px)' }
                ], { 
                // timing options
                duration: 1000,
            });

        }

    }else{
        if(flag === true){
            document.getElementById("fixed-header").animate([
                // keyframes
                { transform: 'translateY(0px)' }, 
                { transform: 'translateY(-300px)' }
              ], { 
                // timing options
                duration: 1000,
            
              }, );

              flag=false;

            setTimeout(function(){

    
                fixedHeader.classList.add('d-none')
                fixedHeader.classList.remove('d-flex')

            }, 900)
        }
    }
}

