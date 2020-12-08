window.addEventListener('load', pepe) 

function pepe(){

    const hmenu = document.getElementById("h-menu");
    const imenu = document.getElementById("mobile-menu")


    hmenu.onclick = () => {  

        hmenu.classList.toggle("h-active")
        imenu.classList.toggle("d-flex")
        document.body.classList.toggle("overflow-hidden")

    }



}