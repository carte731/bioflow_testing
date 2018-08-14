var client = require('./scp2')

function submitting(request, require){

    var q1 = document.forms['question']['tq1'].value;
    
    var q2 = document.forms['question']['tq2'].value;
    var q3 = document.forms['question']['tq3'].value;

    for(var i = 1; i <= 3; i++){
        if(eval('q' + i) == ''){
            alert("Please enter in all values.");
        }
    }

    alert("testing_1")


    // var spawn = require('child_process').spawn;

    // client.scp('testSEND.txt', 'carte731@login.msi.umn.edu:~', function(err) {
    // })

    client.scp('testSEND.txt', {
        host: '@login.msi.umn.edu',
        username: 'carte731',
        password: 'RockY!1065&',
        path: '~'
    }, function(err) {})

    alert("testing_2")

}