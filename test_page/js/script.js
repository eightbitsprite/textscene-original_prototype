window.onload = function() {
    console.log("window loaded.");
    init();
}

function init() {
    console.log(data);
    var testButton = document.getElementById("testButton");
    testButton.addEventListener("click", printer);
    //printer(data);
}

printer = function() {
    var index = 0;
    var i = 1;

    var input = data

    function nextLine() {
        if (index < input.lines.length) {
            text = input.lines[index];
            nodeCreate(text);

            index = index + 1
        }
    }

    nextLine();

    setInterval(function () {
        nextLine()
    }, 2000); 
}

nodeCreate = function(text) {
    var ele = document.createElement("div");
    ele.setAttribute( 'class', 'textbox');
    ele.innerHTML = textProcess(text);
    console.log(text);
    console.log(ele);
    setTimeout(function () {
        document.getElementById('logbox').appendChild(ele);
    }, 700*text.time);
}

textProcess = function(text) {

    if (text.keyword !== "") {
        console.log("Keyword: " + text.keyword);
        return "";
    }
    var string = text.line;
    if (text.speaker.length) {
        var speaker = text.speaker;
        if (text.emote.length) {
            speaker = speaker + " (<em>" + text.emote + "</em>)";
        }
        return speaker + ": " + string;
    }
    return "<em>" + string + "</em>";
}
/*
function loadJSON(callback) {

    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', '..\\test.out', false);
    xobj.onreadystatechange = function() {
        if (xobj.readyState == 4 && xobj.status == "200") {
            callback(xobj.responseText);
        }
    };

    xobj.send(null);
}

function init() {
    loadJSON( function(response) {
        var actual_JSON = JSON.parse(response);
    });
}
*/

