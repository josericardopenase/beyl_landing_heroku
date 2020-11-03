window.onload = () => {

    const hmenu = document.getElementById("h-menu")
    const imenu = document.getElementById("mobile-menu")

    
    hmenu.onclick = () => {
       hmenu.classList.toggle("h-active")
       imenu.classList.toggle("d-flex")
       document.body.classList.toggle("overflow-hidden")

    }


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

