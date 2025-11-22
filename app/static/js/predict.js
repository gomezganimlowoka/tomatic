document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("upload-form");
  const resultDiv = document.getElementById("result");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    resultDiv.textContent = "Predicting...";

    const formData = new FormData(form);

    try {
      const response = await fetch("/predict", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        resultDiv.textContent =
          "Error: " + (errorData.error || "Prediction failed");
        return;
      }

      const data = await response.json();
      resultDiv.innerHTML = `
        <h3>Prediction: ${data.predicted_label}</h3>
        <p><strong>Cause:</strong> ${data.cause}</p>
        <p><strong>Prevention:</strong> ${data.prevention}</p>
        <img src="${data.uploaded_file_url}" alt="Uploaded Leaf Image" style="max-width: 300px; margin-top: 10px;" />
      `;
    } catch (error) {
      resultDiv.textContent = "Error: " + error.message;
    }
  });
});
