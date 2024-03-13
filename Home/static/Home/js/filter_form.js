function submitFormOnChange() {
        const selectElement = document.getElementById("chosen_character");
        selectElement.addEventListener("change", function() {
            // Automatically submit the form when the selection changes
            document.getElementById("filter_form").submit();
        });
    }
