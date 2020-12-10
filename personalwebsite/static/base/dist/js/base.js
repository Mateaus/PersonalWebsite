var currentPathName = window.location.pathname;
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
    showNavBarContent();
}

/* Handles events when the screen width is greater or equal to 992px
 * and less than 1200px */
function onMediumScreen() {
    showNavBarContent();
}

/* Handles events when the screen width is greater or equal to 768px
 * and less than 992px */
function onSmallScreen() {
    hideNavBarContent();
}

/* Handles events when the screen width is greater or equal to 0px
 * and less than 768px */
function onExtraSmallScreen() {
    hideNavBarContent();
}

function showNavBarContent() {
    var navBarCollapse = document.getElementById("navbarCollapse");
    navBarCollapse.classList.add("container");

    var activeLink = navBarCollapse.getElementsByClassName("active")[0];
    activeLink.style.display = "block";

    var navBar = document.getElementsByClassName("navbar")[0];
    if (navBar) {
        navBar.style.justifyContent = "space-between";
    }

    var currentViewTitle = document.getElementById("my-current-view");
    currentViewTitle.style.display = "none";
}

function hideNavBarContent() {
    var navBarCollapse = document.getElementById("navbarCollapse");
    navBarCollapse.classList.remove("container");

    var activeLink = navBarCollapse.getElementsByClassName("active")[0];
    activeLink.style.display = "none";

    var navBar = document.getElementsByClassName("navbar")[0];
    if (navBar) {
        navBar.style.justifyContent = "flex-start";
    }

    var currentViewTitle = document.getElementById("my-current-view");
    currentViewTitle.style.display = "block";
    currentViewTitle.textContent = activeLink.text;
}

window.addEventListener('load', onWindowResize);
window.addEventListener('resize', onWindowResize);