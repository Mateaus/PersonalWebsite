function truncateText(string, charIndex) {
    var stringCount = string.length;
    if (stringCount <= charIndex) {
        return string;
    }

    /* TODO: Find the closest empty char to truncate. */
    return string.substring(0, charIndex) + ' ...';
}

function ellipsisPostOverviews() {
    var truncateAtIndex = 200;
    var text = document.getElementsByClassName("post-overview");

    for (i = 0; i < text.length; i++) {
        var t = truncateText(text[i].textContent, truncateAtIndex)
        text[i].textContent = t;
    }
}

window.addEventListener('load', ellipsisPostOverviews);