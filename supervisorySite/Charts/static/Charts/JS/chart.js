function ajax() {
    var xhhtp = new XMLHttpRequest();
    xhhtp.onreadystatechange = function () {
        if (this.status == 200 && this.response != "") {
            plotChart(this.response);
        }
    }
    xhhtp.open("GET", "chartJSON", true);
    xhhtp.send();
}

var chartElement = null;
function plotChart(response) {
    response = JSON.parse(response);

    var chart = document.getElementById('myChart').getContext("2d");
    // Chart is not find, but comes from HTML file.
    if (chartElement != null) {
        chartElement.destroy();
    }
    chartElement = new Chart(chart, response);
}

var periodicInterval = setInterval(ajax, 700);
