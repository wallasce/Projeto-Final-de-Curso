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

function updateValues(response) {
    variables = JSON.parse(response.response);
    changeInnerText("temperature", "The current temperature is: ", variables.temperature);
    changeInnerText("mode", "Mode: ", variables.mode);
    changeInnerText("voltage", "Voltage: ", variables.voltage);
    changeInnerText("setPoint", "SetPoint: ", variables.setPoint);
    changeInnerText("kp", "Kp: ", variables.kp);
    changeInnerText("ki", "Ki: ", variables.ki);
}

var periodicInterval = setInterval(ajax, 700)