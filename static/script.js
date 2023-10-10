document.addEventListener("DOMContentLoaded", function () {
    const urlForm = document.getElementById("urlForm");
    const longUrlInput = document.getElementById("longUrl");
    const shortenedUrlSpan = document.getElementById("shortenedUrl");
    const errorSpan = document.getElementById("error");

    urlForm.addEventListener("submit", function (e) {
        e.preventDefault(); // Prevent the default form submission behavior

        // Get the long URL entered by the user
        const longUrl = longUrlInput.value;

        // Check if the input is empty
        if (longUrl.trim() === "") {
            errorSpan.textContent = "Please enter a URL.";
            return; 
        }

        // Regular expression for validating URLs
        const urlPattern = /^(https?:\/\/)?([\w.-]+\.[a-zA-Z]{2,})(\/\S*)?$/;

        if (urlPattern.test(longUrl)) {
            // Make an AJAX request to the Flask server
            fetch("/", {
                method: "POST",
                body: new URLSearchParams({ nm: longUrl }),
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            })
                .then((response) => response.text())
                .then((shortenedUrl) => {
                    // Concatenate the base URL with the short code and display it
                    const baseUrl = window.location.origin;
                    const fullShortenedUrl = `${baseUrl}/${shortenedUrl}`;

                    // Clear any previous error message
                    errorSpan.textContent = "";

                    // Create an anchor (<a>) element and set its attributes
                    const anchor = document.createElement("a");
                    anchor.href = fullShortenedUrl;
                    anchor.textContent = fullShortenedUrl;
                    anchor.target = "_blank"; 

                    // Clear the span and append the anchor element
                    shortenedUrlSpan.innerHTML = "";
                    shortenedUrlSpan.appendChild(anchor);

                    // Clear the input field
                    longUrlInput.value = "";
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        } else {
            // Invalid URL format
            shortenedUrlSpan.innerHTML = "";
            errorSpan.textContent = "Invalid URL format. Please enter a valid URL.";
        }
    });
});
