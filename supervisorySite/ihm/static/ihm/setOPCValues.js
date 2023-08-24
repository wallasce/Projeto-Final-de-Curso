var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

function addEventsToInput(id, ajaxFunction) {
    var inputElement = document.getElementById(id);
    
    inputElement.onblur = function() {
        var xhhtp = new XMLHttpRequest();
        xhhtp.open("POST", ajaxFunction, true);
        xhhtp.setRequestHeader("X-CSRFToken", csrftoken); 
        xhhtp.send(String(this.value));
    }

    inputElement.onkeyup = function(event) {
        var keyCode = event.code || event.key;
        if (keyCode == 'Enter'){
            this.blur();
        }
    }
}

addEventsToInput('setPoint', 'ajax/setOPCSetPoint');
addEventsToInput('ki', 'ajax/setOPCKi')
addEventsToInput('kp', 'ajax/setOPCKp')