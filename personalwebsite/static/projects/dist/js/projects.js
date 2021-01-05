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

// close project details when clicking outside div
document.addEventListener('click', function(event) {
    let projectDetail = document.getElementById('project-detail');
    let isClickInside = projectDetail.contains(event.target);

    if (!isClickInside) {
        projectDetail.innerHTML = "";
    }
});
