/* =========================================
   ABOUT TABS
========================================= */

const aboutTabs =
    document.querySelectorAll(".about__tab");

const aboutPanels =
    document.querySelectorAll(".about__panel");


aboutTabs.forEach((tab) => {

    tab.addEventListener("click", () => {

        const target =
            tab.dataset.tab;


        /* Reset tabs */

        aboutTabs.forEach((item) => {

            item.classList.remove("active");

            item.setAttribute(
                "aria-selected",
                "false"
            );

        });


        /* Hide panels */

        aboutPanels.forEach((panel) => {

            panel.classList.remove("active");

            panel.hidden = true;

        });


        /* Activate clicked tab */

        tab.classList.add("active");

        tab.setAttribute(
            "aria-selected",
            "true"
        );


        /* Show matching panel */

        const targetPanel =
            document.querySelector(
                `[data-panel="${target}"]`
            );


        if (targetPanel) {

            targetPanel.hidden = false;

            targetPanel.classList.add("active");

        }

    });

});


            /* =====================================
               UPDATE TABS
            ===================================== */

            aboutTabs.forEach((item) => {

                const isActive =
                    item === tab;

                item.classList.toggle(
                    "active",
                    isActive
                );

                item.setAttribute(
                    "aria-selected",
                    isActive
                        ? "true"
                        : "false"
                );

            });


            /* =====================================
               UPDATE PANELS
            ===================================== */

            aboutPanels.forEach((panel) => {

                const isActive =
                    panel.dataset.panel === target;


                panel.classList.toggle(
                    "active",
                    isActive
                );


                panel.hidden =
                    !isActive;

            });

