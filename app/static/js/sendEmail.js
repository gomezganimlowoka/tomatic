function sendEmail() {
    const templateParams = {
        from_name: document.getElementById("fn1").value,
        from_email: document.getElementById("em1").value,
        message: document.getElementById("ms").value
    };
    emailjs.send('service_fevplkl', 'template_eq71hhl', templateParams)
        .then(function(response) {
            alert('Message sent successfully!');
        }, function(error) {
            alert('Failed to send message. Please try again later.');
        });
}
