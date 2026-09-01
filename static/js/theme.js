/* =========================================
   THEME TOGGLE
========================================= */

document.addEventListener("DOMContentLoaded", () => {

    const html = document.documentElement;

    const themeToggle =
        document.getElementById("theme-toggle");


    if (!themeToggle) {
        console.warn(
            "Theme toggle button not found."
        );

        return;
    }


    /* =====================================
       CURRENT THEME
    ===================================== */

    const currentTheme =
        html.getAttribute("data-theme") || "light";


    html.setAttribute(
        "data-theme",
        currentTheme
    );


    /* =====================================
       TOGGLE
    ===================================== */

    themeToggle.addEventListener(
        "click",
        () => {

            const current =
                html.getAttribute("data-theme");


            const newTheme =
                current === "dark"
                    ? "light"
                    : "dark";


            html.setAttribute(
                "data-theme",
                newTheme
            );


            localStorage.setItem(
                "portfolio-theme",
                newTheme
            );

        }
    );

});