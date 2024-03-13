async function copyText(text_id) {
    const outputElement = document.getElementById(text_id);
    const textToCopy = outputElement.textContent;
    const copyButton = document.querySelector('.copy-button');
    const copiedText = 'Copied!'; // New text for the button


    try {
        await navigator.clipboard.writeText(textToCopy);

        copyButton.innerHTML = copiedText;
        setTimeout(function() {
        copyButton.innerHTML = '<i class="fa-regular fa-clipboard"></i> Copy';
    }, 5000);

    } catch (error) {
        console.error('Error copying text:', error);
    }
}
