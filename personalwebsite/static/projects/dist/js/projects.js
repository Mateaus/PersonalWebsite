function closeProjectDetail(closeBtn) {
    const projectDetailDiv = closeBtn.parentNode.parentNode;
    projectDetailDiv.parentNode.removeChild(projectDetailDiv);
}