function closeProjectDetail(element) {
    const projectDetailDiv = element.parentNode.parentNode;

    projectDetailDiv.classList.remove("show");
    projectDetailDiv.innerHTML = "";
}

function displayProjectDetail(element) {
    let projectId = element.parentElement.parentElement.id;
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = () => {
        if (xhttp.readyState == XMLHttpRequest.DONE) {
            if (xhttp.status == 200) {
                let projectDetailDiv = document.getElementById("project-detail");
                projectDetailDiv.innerHTML = xhttp.responseText;
                projectDetailDiv.classList.add("show");
                console.log(projectDetailDiv.classList);
            } else if (xhttp.status == 400) {
                alert("There was an error 400");
            } else {
                alert("Something else other than 200 was returned");
            }
        }
    }
    xhttp.open("GET", "detail/" + projectId, true);
    xhttp.send();
}

// Detecting click event here using DOM event delegation
function executeFuncOnClass(e, targetElType, targetClassesArr, callBackFunc) {
    if (e.target && e.target.nodeName === targetElType) {
        let classes = e.target.className.split(" ");
        if (classes) {
            let targetClasses = JSON.stringify(targetClassesArr);
            let selectedElClasses = JSON.stringify(classes);
            if (targetClasses === selectedElClasses) {
                callBackFunc(e.target);
            }
        }
    }
}

const mainProjDiv = document.getElementsByClassName("project-main")[0];
mainProjDiv.addEventListener('click', event =>
    executeFuncOnClass(event, "BUTTON", ["learn-more"], displayProjectDetail));

const projectDetailDiv = document.getElementById("project-detail");
projectDetailDiv.addEventListener('click', event =>
    executeFuncOnClass(event, "BUTTON", ["btn", "close-project"], closeProjectDetail));

// close project details when clicking outside div
document.addEventListener('click', event => {
    let projectDetailDiv = document.getElementById('project-detail');
    let isClickInside = projectDetailDiv.contains(event.target);
    if (!isClickInside) {
        projectDetailDiv.innerHTML = "";
        projectDetailDiv.classList.remove("show");
    }
});