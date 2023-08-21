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

function updateValues(response) {
    variables = JSON.parse(response.response);
    document.getElementById("temperature").innerText = "The current temperature is " + variables.temperature;
}

var periodicInterval = setInterval(ajax, 1000)