document.addEventListener('DOMContentLoaded', function () {
    const container = document.querySelector('#id_sizes'); // the widget textarea

    if (container && container.tagName === 'TEXTAREA') {
        // Hide the default textarea
        container.style.display = 'none';

        const form = container.closest('form');

        const wrapper = document.createElement('div');
        wrapper.id = 'sizes-wrapper';

        // Load existing sizes from textarea JSON
        let values = [];
        try {
            values = JSON.parse(container.value);
        } catch (e) {}

        function renderFields() {
            wrapper.innerHTML = '';
            values.forEach((val, idx) => {
                const input = document.createElement('input');
                input.type = 'text';
                input.value = val;
                input.className = 'vTextField';
                input.style.marginBottom = '4px';
                input.oninput = () => {
                    values[idx] = input.value;
                    container.value = JSON.stringify(values);
                };
                wrapper.appendChild(input);
            });
        }

        renderFields();

        const addBtn = document.createElement('button');
        addBtn.type = 'button';
        addBtn.innerText = 'Add size';
        addBtn.className = 'button';
        addBtn.onclick = () => {
            values.push('');
            renderFields();
            container.value = JSON.stringify(values);
        };

        form.insertBefore(wrapper, container);
        form.insertBefore(addBtn, container);
    }
});
