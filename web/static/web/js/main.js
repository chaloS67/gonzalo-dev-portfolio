function showSection(id) {
    const panels = document.querySelectorAll(".info-panel");

    panels.forEach(panel => {
        panel.classList.remove("active");
    });

    document.getElementById(id).classList.add("active");
}