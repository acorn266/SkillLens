document.addEventListener("DOMContentLoaded", () => {

    const sliders = document.querySelectorAll(".skill-slider");

    sliders.forEach((slider) => {

        const outputId = slider.dataset.output;
        const output = document.getElementById(outputId);

        if (!output) {
            return;
        }

        output.textContent = slider.value;

        slider.addEventListener("input", () => {

            output.textContent = slider.value;

        });

    });

});