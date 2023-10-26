var csrftoken = document.getElementsByName('csrfmiddlewaretoken')[0].value

function addEventsToInput(id, ajaxFunction) {
    var inputElement = document.getElementById(id);
    
    inputElement.onblur = function() {
        var xhhtp = new XMLHttpRequest();
        xhhtp.open("POST", ajaxFunction, true);
        xhhtp.setRequestHeader("X-CSRFToken", csrftoken); 
        xhhtp.send(String(this.value));
    }

    inputElement.onkeydown = function(event) {
        if (event.key == 'Enter'){
            event.preventDefault();
            this.blur();
        }
    }
}

function addAjxaOnChangeRadioForm(id, ajaxFunction) {
    document.getElementById(id).onchange = function() {
        var value = this.querySelector('input[name=mode]:checked').value;
    
        var xhhtp = new XMLHttpRequest();
            xhhtp.open("POST", ajaxFunction, true);
            xhhtp.setRequestHeader("X-CSRFToken", csrftoken); 
            xhhtp.send(value);
    }
}

addAjxaOnChangeRadioForm('modeForm', 'ajax/setOPCMode')
addEventsToInput('setPoint', 'ajax/setOPCSetPoint');
addEventsToInput('ki', 'ajax/setOPCKi')
addEventsToInput('kp', 'ajax/setOPCKp')
addEventsToInput('voltage', 'ajax/setOPCVoltage');