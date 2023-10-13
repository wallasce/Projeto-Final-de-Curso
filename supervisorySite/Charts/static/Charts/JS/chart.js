function ajax() {
    var xhhtp = new XMLHttpRequest();
    xhhtp.onreadystatechange = function () {
        if (this.status == 200 && this.response != "") {
            plotChart(this.response)
        }
    }
    xhhtp.open("GET", "chartJSON", true);
    xhhtp.send();
}

function plotChart(response) {
    var chart = document.getElementById('myChart').getContext("2d");
    // Chart is not find, but comes from HTML file.
    new Chart(chart, {
        type: 'line', 
        data: JSON.parse(response),
        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
    });
}

ajax()
