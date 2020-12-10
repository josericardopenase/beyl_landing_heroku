
const nombreGalleta = "GalletitaPrivada";



window.onload = () => {

    const cookiePolicyBanner = document.getElementById('privacyBanner');
    const bottonAccept = document.getElementById('privacyAccept');
    const bottonDecline = document.getElementById('privacyDecline');

    bottonAccept.onclick = ()  =>  {
        Cookies.set(nombreGalleta, 'true', {expires: 360});
        activateCookies();
        cookiePolicyBanner.remove();
    }

    bottonDecline.onclick = ()  =>  {
        Cookies.set(nombreGalleta, 'false', {expires: 3});
        cookiePolicyBanner.remove();
    }

    if(!Cookies.get(nombreGalleta) ){
        Cookies.set(nombreGalleta, 'none', {expires: 360});
        cookiePolicyBanner.classList.add('d-flex');
    }else{

        switch(Cookies.get(nombreGalleta)){

            case 'true':
                cookiePolicyBanner.remove();
                activateCookies();
                break;
            case 'false':
                cookiePolicyBanner.remove();
                break;
            case 'none':
                cookiePolicyBanner.classList.add('d-flex');
        }
    }



}

function activateCookies(){

    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-VVFS3B0B64');

    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:2140346,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');


    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'G-RXP585PX3C');

} 