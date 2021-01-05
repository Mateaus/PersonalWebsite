function closeProjectDetail(element) {
    const projectDetailDiv = element.parentNode.parentNode;
    projectDetailDiv.parentNode.removeChild(projectDetailDiv);
}

function displayProjectDetail(element) {
    let projectId = element.parentElement.parentElement.id;
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == XMLHttpRequest.DONE) {
            if (xhttp.status == 200) {
                document.getElementById("project-detail").innerHTML = xhttp.responseText;
            }
            else if (xhttp.status == 400) {
                alert("There was an error 400");
            }
            else {
                alert("Something else other than 200 was returned");
            }
        }
    }
    xhttp.open("GET", "detail/" + projectId, true);
    xhttp.send();
}

const learnMoreElements = document.getElementsByClassName('learn-more');
Array.from(learnMoreElements).forEach(element => {
    element.addEventListener('click', () => displayProjectDetail(element));
});

const projectDetailDiv = document.getElementById("project-detail");
projectDetailDiv.addEventListener('click', event => {
    // button was pressed inside detail div
    if (event.target && event.target.nodeName == "BUTTON") {
        // get button classes
        const classes = event.target.className.split(" ");
        // make sure classes of the button matches close button classes
        if (classes) {
            const targetClasses = JSON.stringify(["btn", "close-project"]);
            const selectedBtnClasses = JSON.stringify(classes);
            if (targetClasses === selectedBtnClasses) {
                closeProjectDetail(event.target);
            }
        }
    }
});

// close project details when clicking outside div
document.addEventListener('click', function (event) {
    let projectDetail = document.getElementById('project-detail');
    let isClickInside = projectDetail.contains(event.target);

    if (!isClickInside) {
        projectDetail.innerHTML = "";
    }
});