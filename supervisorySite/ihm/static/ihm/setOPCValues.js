var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

document.getElementById('setPoint').onblur = function() {
    var xhhtp = new XMLHttpRequest();
    xhhtp.open("POST", "ajax/setOPCSetPoint", true);
    xhhtp.setRequestHeader("X-CSRFToken", csrftoken); 
    xhhtp.send(String(this.value));
}

document.getElementById('setPoint').onkeyup = function(event) {
    var keyCode = event.code || event.key;
    if (keyCode == 'Enter'){
        this.blur()
    }
}