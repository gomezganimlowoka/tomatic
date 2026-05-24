function sendEmail() {
    const templateParams = {
        from_name: document.getElementById("fn1").value,
        from_email: document.getElementById("em1").value,
        message: document.getElementById("msg1").value  
    };

   emailjs.send('service_fevplkl', 'template_eq71hhl', templateParams)
    .then(function(response) {
        document.getElementById("success-msg").classList.remove("d-none");
        setTimeout(function() {
            document.getElementById("success-msg").classList.add("d-none");
        }, 5000);
    }, function(error) {
        document.getElementById("error-msg").classList.remove("d-none");
        setTimeout(function() {
            document.getElementById("error-msg").classList.add("d-none");
        }, 5000);
    });

}

// Attach to form submit
document.querySelector("form").addEventListener("submit", function(e) {
    e.preventDefault();
    sendEmail();
});

function onSubmit() {
    const btn = document.getElementById("btn-send");
    btn.innerText = "Sending...";
    btn.disabled = true;

    // Clears all fields at once instead of one by one
    document.querySelector("form").reset();
}
