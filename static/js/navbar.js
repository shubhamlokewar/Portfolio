/* =========================================
   NAVBAR
========================================= */

document.addEventListener("DOMContentLoaded", () => {

    const navbar =
        document.querySelector(".navbar");

    const toggle =
        document.querySelector("#navbar-toggle");

    const menu =
        document.querySelector("#navbar-menu");

    const links =
        document.querySelectorAll(".navbar__menu a");


    /* =====================================
       SAFETY CHECK
    ===================================== */

    if (!navbar || !toggle || !menu) {
        return;
    }


    /* =====================================
       SCROLL EFFECT
    ===================================== */

    const updateNavbar = () => {

        navbar.classList.toggle(
            "scrolled",
            window.scrollY > 20
        );

    };


    updateNavbar();


    window.addEventListener(
        "scroll",
        updateNavbar,
        { passive: true }
    );


    /* =====================================
       MOBILE MENU
    ===================================== */

    toggle.addEventListener("click", () => {

        const isOpen =
            menu.classList.toggle("active");


        toggle.classList.toggle(
            "active",
            isOpen
        );


        toggle.setAttribute(
            "aria-expanded",
            String(isOpen)
        );

    });


    /* =====================================
       CLOSE MENU AFTER LINK CLICK
    ===================================== */

    links.forEach((link) => {

        link.addEventListener("click", () => {

            menu.classList.remove("active");

            toggle.classList.remove("active");

            toggle.setAttribute(
                "aria-expanded",
                "false"
            );

        });

    });


    /* =====================================
       CLOSE WHEN CLICKING OUTSIDE
    ===================================== */

    document.addEventListener("click", (event) => {

        if (
            !navbar.contains(event.target) &&
            menu.classList.contains("active")
        ) {

            menu.classList.remove("active");

            toggle.classList.remove("active");

            toggle.setAttribute(
                "aria-expanded",
                "false"
            );

        }

    });


    /* =====================================
       CLOSE WITH ESCAPE
    ===================================== */

    document.addEventListener("keydown", (event) => {

        if (
            event.key === "Escape" &&
            menu.classList.contains("active")
        ) {

            menu.classList.remove("active");

            toggle.classList.remove("active");

            toggle.setAttribute(
                "aria-expanded",
                "false"
            );

            toggle.focus();

        }

    });


    /* =====================================
       RESET MOBILE MENU ON DESKTOP
    ===================================== */

    window.addEventListener("resize", () => {

        if (window.innerWidth > 900) {

            menu.classList.remove("active");

            toggle.classList.remove("active");

            toggle.setAttribute(
                "aria-expanded",
                "false"
            );

        }

    });

});