// Event listener callback function
function adderButtonCallback(_event) {
  // Default values for adder inputs
  const adder_values = {left: 0, right: 0};

  // Obtain referances to input HTML elements
  const adder_element_left = document.getElementById('adder--left');
  const adder_element_right = document.getElementById('adder--right');

  // Ensure that inputs are numbers befor overwriting defaults
  if (!isNaN(adder_element_left.value)) {
    adder_values['left'] = Number(adder_element_left.value);
  }
  if (!isNaN(adder_element_right.value)) {
    adder_values['right'] = Number(adder_element_right.value);
  }

  // Obtain referacne to output HTML element and assign new value
  const adder_element_results = document.getElementById('adder--results');
  adder_element_results.value = adder_values['left'] + adder_values['right'];
}


// Allow page to load fully prior to adding event listeners to any elements
window.addEventListener('load', function (_event) {
  const adder_element_button = document.getElementById('adder--button');
  adder_element_button.addEventListener('click', adderButtonCallback);
});
