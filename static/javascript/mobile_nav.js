window.addEventListener('load', pepe) 

function pepe(){

    const b1 = document.getElementById("botonocultar");
    const v2 = document.getElementById("botonocultar1");
    const hmenu = document.getElementById("h-menu");
    const imenu = document.getElementById("mobile-menu")


    b1.onclick = () => {

        hmenu.classList.toggle("h-active")
        imenu.classList.toggle("d-flex")
        document.body.classList.toggle("overflow-hidden")
    }

    v2.onclick = () => {

        hmenu.classList.toggle("h-active")
        imenu.classList.toggle("d-flex")
        document.body.classList.toggle("overflow-hidden")
    }

    hmenu.onclick = () => {  

        hmenu.classList.toggle("h-active")
        imenu.classList.toggle("d-flex")
        document.body.classList.toggle("overflow-hidden")

    }



}