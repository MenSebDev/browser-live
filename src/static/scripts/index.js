class BrowserStack {
    constructor() {
        this.form = document.querySelector('form');
        this.form.addEventListener('change', this.dispatchChange);
        this.form.addEventListener('submit', this.start);
        this.form.addEventListener('reset', this.stop);

        this.selectBrowser = this.form.elements['browser'];
        this.selectDevice = this.form.elements['device'];
        this.selectBreakpoint = this.form.elements['breakpoint'];

        this.inputHeight = this.form.elements['height'];
        this.inputWidth = this.form.elements['width'];

        console.log(
            this.selectBreakpoint,
            this.selectDevice,
            this.inputHeight,
            this.inputWidth,
        );
    }

    dispatchChange = (event) => {
        const { target } = event;

        switch (target) {
            case this.selectBrowser:
                return this.onSelectBrowser(event);
            case this.selectBreakpoint:
                this.selectDevice.value = '';
                return this.onSelectBreakpoint(event);
            case this.selectDevice:
                this.selectBreakpoint.value = '';
                return this.onSelectDevice(event);
            default:
                console.log('UNHANDLE EVENT', event);
        }
    };

    updateInputHeight = (value) => {
        this.inputHeight.value = value;
    };

    updateInputWidth = (value) => {
        this.inputWidth.value = value;
    };

    updateInputSize;

    onSelectBrowser = (event) => {
        console.log('SELECT BROWSER', event);
    };

    onSelectDevice = (event) => {
        console.log('SELECT DEVICE', event);

        const { selectedOptions } = this.selectDevice;
        const selectedOption = selectedOptions[0];
        const { height, width } = selectedOption.dataset;

        this.updateInputHeight(height);
        this.updateInputWidth(width);
    };

    onSelectBreakpoint = (event) => {
        console.log('SELECT BREAKPOINT', event);

        const { selectedOptions } = this.selectBreakpoint;
        const selectedOption = selectedOptions[0];
        const { height, width } = selectedOption.dataset;

        this.updateInputHeight(height);
        this.updateInputWidth(width);
    };

    start = async (event) => {
        event.preventDefault();

        const formData = new FormData(this.form);

        if (this.selectDevice.value !== 'custom') {
            formData.append(this.inputHeight.name, this.inputHeight.value);
            formData.append(this.inputWidth.name, this.inputWidth.value);
        }

        const response = await fetch('/api/browser/start', {
            body: formData,
            method: 'POST',
        });

        const json = await response.json();

        console.log(json);
    };

    stop = async (event) => {
        event.preventDefault();

        const response = await fetch('/api/browser/stop');

        const json = await response.json();

        console.log(json);
    };
}

new BrowserStack();
