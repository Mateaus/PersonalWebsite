var currentScreenSize = -1;

/* Handle the different windows sizes here
 * and only call it once per screen size. */
function onWindowResize() {
    var width = window.innerWidth;

    if (width >= 1200 && currentScreenSize != 1200) {
        onLargeScreen();
        currentScreenSize = 1200;
    }
    else if (width < 1200 && width >= 992 && currentScreenSize != 992) {
        onMediumScreen();
        currentScreenSize = 992;
    }

    else if (width < 992 && width >= 768 && currentScreenSize != 768) {
        onSmallScreen();
        currentScreenSize = 768;
    }
    else if (width < 768 && width >= 0 && currentScreenSize != 576) {
        onExtraSmallScreen();
        currentScreenSize = 576;
    }
}

/* Handles events when the screen width is greater or equal to 1200px */
function onLargeScreen() {
    var navBarCollapse = document.getElementById("navbarCollapse");
    navBarCollapse.classList.add("container");

    var navBar = document.getElementsByClassName("navbar")[0];
    if (navBar) {
        navBar.style.justifyContent = "space-between";
    }
}

/* Handles events when the screen width is greater or equal to 992px
 * and less than 1200px */
function onMediumScreen() {
    var navBarCollapse = document.getElementById("navbarCollapse");
    navBarCollapse.classList.add("container");

    var navBar = document.getElementsByClassName("navbar")[0];
    if (navBar) {
        navBar.style.justifyContent = "space-between";
    }
}

/* Handles events when the screen width is greater or equal to 768px
 * and less than 992px */
function onSmallScreen() {
    var navBarCollapse = document.getElementById("navbarCollapse");
    navBarCollapse.classList.remove("container");

    var navBar = document.getElementsByClassName("navbar")[0];
    if (navBar) {
        navBar.style.justifyContent = "flex-start";
    }
}

/* Handles events when the screen width is greater or equal to 0px
 * and less than 768px */
function onExtraSmallScreen() {
    var navBarCollapse = document.getElementById("navbarCollapse");
    navBarCollapse.classList.remove("container");

    var navBar = document.getElementsByClassName("navbar")[0];
    if (navBar) {
        navBar.style.justifyContent = "flex-start";
    }
}

window.addEventListener('load', onWindowResize);
window.addEventListener('resize', onWindowResize);