function ajax() {
    var xhhtp = new XMLHttpRequest();
    xhhtp.onreadystatechange = function () {
        if (this.status == 200 && this.response != "") {
            updateValues(this);
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

// Change the Choice Field Mode.
function changeModeSelect(value) {
    formMode = document.getElementById("mode");
    option = formMode.querySelector("input[value=" + value + "]")
    option.checked = true;
}

function updateValues(response) {
    variables = JSON.parse(response.response);
    changeInnerText("temperature", "The current temperature is: ", variables.temperature);
    changeInnerText("voltage", "Voltage: ", variables.voltage);
    changeLabelForm("setPoint", "SetPoint: ", variables.setPoint);
    changeLabelForm("kp", "Kp: ", variables.kp);
    changeLabelForm("ki", "Ki: ", variables.ki);
    changeModeSelect(variables.mode);
}

var periodicInterval = setInterval(ajax, 700)