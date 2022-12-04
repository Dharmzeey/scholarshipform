let attestation = document.querySelector("#id_attestation");
let submitButton = document.querySelector("#submit");

attestation.addEventListener('click', displayButton)

function displayButton() {
  if (attestation.checked) {
    submitButton.style.display = 'block'
  } else {
    submitButton.style.display = 'none'
  }
}