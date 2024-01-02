class BrowserLive {
    constructor() {
        this.form = document.getElementById('form-setup');
        this.form.addEventListener('reset', this.reset);
        this.form.addEventListener('submit', this.submit);

        this.selectBreakpoint = this.form.elements['breakpoint'];
        this.selectBreakpoint.addEventListener('change', this.updateBreakpoint);

        this.selectBrowser = this.form.elements['browser'];
        this.selectBrowser.addEventListener('change', this.updateBrowser);

        this.selectDevice = this.form.elements['device'];
        this.selectDevice.addEventListener('change', this.updateDevice);

        this.selectDisplay = this.form.elements['display'];
        this.selectDisplay.addEventListener('change', this.updateDisplay);

        this.inputHeight = this.form.elements['height'];
        this.inputHeight.addEventListener('input', this.updateDimension);

        this.inputWidth = this.form.elements['width'];
        this.inputWidth.addEventListener('input', this.updateDimension);
    }

    reset = async (event) => {
        event.preventDefault();

        const response = await fetch('/api/browser/stop');

        const json = await response.json();

        console.log(json);
    };

    submit = async (event) => {
        event.preventDefault();

        const formData = new FormData(this.form);

        const response = await fetch('/api/browser/start', {
            body: formData,
            method: 'POST',
        });

        const json = await response.json();

        console.log(json);
    };

    updateBreakpoint = (event) => {
        console.log('SELECT BREAKPOINT', { event });

        this.selectDevice.value = '';
        this.updateInputDimension(event.target);
    };

    updateBrowser = (event) => {
        console.log('SELECT BROWSER', { event });
    };

    updateDevice = (event) => {
        console.log('SELECT DEVICE', { event });

        this.selectBreakpoint.value = '';
        this.updateInputDimension(event.target);
    };

    updateDimension = (event) => {
        console.log('INPUT DIMENSION', { event });

        this.selectDevice.value = '';
        this.selectBreakpoint.value = '';
    };

    updateDisplay = (event) => {
        console.log('SELECT DISPLAY', { event });
    };

    updateInputDimension = (selectElement) => {
        const { selectedOptions } = selectElement;
        const selectedOption = selectedOptions[0];
        const { height, width } = selectedOption.dataset;

        this.updateInputHeight(height);
        this.updateInputWidth(width);
    };

    updateInputHeight = (value) => {
        this.inputHeight.value = value;
    };

    updateInputWidth = (value) => {
        this.inputWidth.value = value;
    };
}

new BrowserLive();
