document.addEventListener("DOMContentLoaded", function () {
    let sizeCount = document.querySelectorAll('input[name^="size_"]').length;

    // Add new size input field
    document.getElementById("add-new-size").addEventListener("click", function (e) {
        e.preventDefault();
        sizeCount++;
        const newSizeField = document.createElement("div");
        newSizeField.innerHTML = `
            <label for="id_size_${sizeCount}">Size ${sizeCount + 1}:</label>
            <input type="text" name="size_${sizeCount}" required>
        `;
        document.getElementById("size-fields").appendChild(newSizeField);
    });
});
