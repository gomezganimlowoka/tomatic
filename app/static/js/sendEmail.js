function sendEmail() {
    const templateParams = {
        from_name: document.getElementById("name").value,
        from_email: document.getElementById("email").value,
        message: document.getElementById("message").value
    };
    emailjs.send('service_9h8v9qj', 'template_1l7z5s8', templateParams)
        .then(function(response) {
            alert('Message sent successfully!');
        }, function(error) {
            alert('Failed to send message. Please try again later.');
        });
}