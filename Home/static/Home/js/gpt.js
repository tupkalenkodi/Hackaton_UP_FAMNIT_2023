function ProcessSaveGptRequest() {
    let character = $('#character').val();
    let theme = $('#theme').val();
    let csrf_token = $('input[name=csrfmiddlewaretoken]').val();
    let outputArea = document.getElementById('output-area')

    if (character !== null) {
        $.ajax({
            type: "POST",
            url: "process_gpt_request",
            data: {
                'character': character,
                'theme': theme,
                'csrfmiddlewaretoken': csrf_token,
            },
            // Intentionally using success callback
            success: function (response) {
                $('#gpt-output').html(response.output);

                outputArea.style.display = 'block';
                let marginVh = 35; // Adjust this value as needed
                let marginPx = marginVh * window.innerHeight / 100; // Convert vh to pixels
                let desiredScrollPosition = outputArea.offsetTop - marginPx + 100;
                window.scrollTo({top: desiredScrollPosition, behavior: 'smooth'});
            },
            error: function (xhr, status, error) {
                console.error("AJAX Error:", error);
            }
        });
    }
    else {
        let errorMessage = document.getElementById('error-message');
        errorMessage.style.display = 'block';

        let marginVh = 35;
        let marginPx = marginVh * window.innerHeight / 100;
        let desiredScrollPosition = errorMessage.offsetTop - marginPx + 100;
        window.scrollTo({top: desiredScrollPosition, behavior: 'smooth'});
    }
}