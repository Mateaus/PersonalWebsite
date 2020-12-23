function dateSpacer() {
    var date = document.getElementsByClassName("post-date");
    
    /* Creation and Updated dates are visible. */

    if (date) {

        var creationDate = date[0];

        console.log(date);

        if (date.length > 1) {
            creationDate.style.margin = "0 8px 0 0";
        } else {
            creationDate.style.margin = "0";
        }

    }
}

// window.addEventListener('load', dateSpacer);