function ajax() {
    var xhhtp = new XMLHttpRequest();
    xhhtp.onreadystatechange = function () {
        if (this.status == 200 && this.response != "") {
            updateValues(this);
        }else if (this.status == 500){
            window.location.href = 'error'
        }
    }
    xhhtp.open("GET", "ajax/getOPCValues", true);
    xhhtp.send();
}

function changeInnerText(id, message, value) {
    document.getElementById(id).innerText = message + value;
}

function changeLabelForm(id, message, value) {
    element = document.getElementById(id);
    if (element !== document.activeElement) {
        element.value = value;
    }
}

function disableElement(id) {
    document.getElementById(id).disabled = true
}

function enableElement(id) {
    document.getElementById(id).disabled = false
}

// Change the Choice Field Mode.
function changeModeSelect(value) {
    formMode = document.getElementById("modeForm");
    option = formMode.querySelector("input[value=" + value + "]")
    option.checked = true;

    if (value == 'A') {
        enableElement('setPoint');
        enableElement('ki');
        enableElement('kp');
        disableElement('voltage');
    }else if (value == 'M') {
        disableElement('setPoint');
        disableElement('ki');
        disableElement('kp');
        enableElement('voltage');
    }
}

function updateValues(response) {
    variables = JSON.parse(response.response);
    changeInnerText("temperature", "Temperature: ", variables.temperature);
    changeInnerText("voltageSensor", "Voltage: ", variables.voltage);
    changeLabelForm("voltage", "Voltage: ", variables.voltage);
    changeLabelForm("setPoint", "SetPoint: ", variables.setPoint);
    changeLabelForm("kp", "Kp: ", variables.kp);
    changeLabelForm("ki", "Ki: ", variables.ki);
    changeModeSelect(variables.mode);
}

var periodicInterval = setInterval(ajax, 700)