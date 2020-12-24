var currentScreenSize = -1;

/* Handle the different windows sizes here
 * and only call the functions once per screen size. */
function onWindowResize() {
    var width = window.innerWidth;

    if (isLargeScreen(width)) {
        onLargeScreen();
        currentScreenSize = 1200;
    }
    else if (isMediumScreen(width)) {
        onMediumScreen();
        currentScreenSize = 992;
    }
    else if (isSmallScreen(width)) {
        onSmallScreen();
        currentScreenSize = 768;
    }
    else if (isExtraSmallScreen(width)) {
        onExtraSmallScreen();
        currentScreenSize = 576;
    }
}

function isLargeScreen(width) {
    return width >= 1200 && currentScreenSize != 1200;
}

function isMediumScreen(width) {
    return width < 1200 && width >= 992 && currentScreenSize != 992;
}

function isSmallScreen(width) {
    return width < 992 && width >= 768 && currentScreenSize != 768;
}

function isExtraSmallScreen(width) {
    return width < 768 && width >= 0 && currentScreenSize != 576;
}

/* Handles events when the screen width is greater or equal to 1200px */
function onLargeScreen() {
    showDesktopNavBar();
}

/* Handles events when the screen width is greater or equal to 992px
 * and less than 1200px */
function onMediumScreen() {
    showDesktopNavBar();
}

/* Handles events when the screen width is greater or equal to 768px
 * and less than 992px */
function onSmallScreen() {
    showMobileNavBar();
}

/* Handles events when the screen width is greater or equal to 0px
 * and less than 768px */
function onExtraSmallScreen() {
    showMobileNavBar();
}

function showDesktopNavBar() {
    var navBarCollapse = document.getElementById("navbarCollapse");
    navBarCollapse.classList.add("container");

    var activeLink = navBarCollapse.getElementsByClassName("active")[0];
    if (activeLink) {
        activeLink.style.display = "block";

        var currentViewTitle = document.getElementById("my-current-view");
        currentViewTitle.style.display = "none";
        currentViewTitle.textContent = "";
    }

    var navBar = document.getElementsByClassName("navbar")[0];
    if (navBar) {
        navBar.style.justifyContent = "space-between";
    }
}

function showMobileNavBar() {
    var navBarCollapse = document.getElementById("navbarCollapse");
    navBarCollapse.classList.remove("container");

    var activeLink = navBarCollapse.getElementsByClassName("active")[0];
    if (activeLink) {
        activeLink.style.display = "none";

        var currentViewTitle = document.getElementById("my-current-view");
        currentViewTitle.style.display = "block";
        currentViewTitle.textContent = activeLink.text;
    }

    var navBar = document.getElementsByClassName("navbar")[0];
    if (navBar) {
        navBar.style.justifyContent = "flex-start";
    }
}

window.addEventListener('load', onWindowResize);
window.addEventListener('resize', onWindowResize);