document.addEventListener("DOMContentLoaded", function() {
    let sizeCount = 1;  // Default size count

    // Add new input box when the "Add New Size" button is clicked
    document.getElementById("add-size-btn").addEventListener("click", function() {
        sizeCount++;
        let newSizeField = document.createElement("input");
        newSizeField.type = "text";
        newSizeField.name = "size_" + sizeCount;
        newSizeField.placeholder = "Size " + sizeCount;
        newSizeField.classList.add("vTextField");
        
        // Append to the size inputs container
        let sizeContainer = document.getElementById("size-inputs-container");
        sizeContainer.appendChild(newSizeField);
    });

    // Hide the size input field if it's empty
    function toggleSizeField() {
        let sizeInputs = document.querySelectorAll("[name^='size_']");
        sizeInputs.forEach(input => {
            if (input.value.trim() === "") {
                input.style.display = "none";
            } else {
                input.style.display = "inline-block";
            }
        });
    }

    toggleSizeField();
});
