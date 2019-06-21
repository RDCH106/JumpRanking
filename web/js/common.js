
var ranking;
var maxranking = 100;  // Max ranking elements (TOP 100)
var apiUrl = "https://server1.mascandobits.es:5030";
var updateFlag;
var updateInterval = 30000;
var datatableOptions = {
                            "order": [[ 1, "desc" ]],
                            "responsive": true
                        };
    
function printRanking(ranking){
    ranking.forEach(function(arrayItem){ 
        $("#ranking tbody").append("<tr><td>"+arrayItem.user
        +"</td><td>"+arrayItem.height
        +"</td></tr>");
    });
    console.log("HTML ranking printed!");   
}

function updateRankingData(){
    $.ajax({type:"GET", url: apiUrl + "/jumpranking/api/v1/registers", dataType: "json", async: true,
        success: function(data) {            
            var rankingData = data.data.slice(0, maxranking);
            var rankingDataArray = [];
            rankingData.forEach(function(arrayItem){
                delete arrayItem.id;
                rankingDataArray.push([arrayItem.user, arrayItem.height]);
                });
            ranking.clear();
            ranking.rows.add(rankingDataArray);
            ranking.draw(false);  // Retain navigation state
            console.log("ranking updated!");  
        }
    });
}
    
function getRanking(){
    
    $.ajax({type:"GET", url: apiUrl + "/jumpranking/api/v1/registers", dataType: "json", async: true,
        success: function(data) {            
            printRanking(data.data.slice(0, maxranking));
            ranking =$("#ranking").DataTable(datatableOptions);
        }
    }).then(function() {
        if(updateFlag){
            setInterval( updateRankingData, updateInterval );
        }        
    });
}

function getParameterByName(name, url) {
    if (!url) { url = window.location.href; }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)");
    var results = regex.exec(url);
    if (!results) { return null; }
    if (!results[2]) { return ""; }
    return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function init(){
    
    $(document).ready(function () {
        updateFlag = getParameterByName('update') === null ? false : getParameterByName('update') === 'true';
        updateInterval = getParameterByName('interval') === null ? updateInterval : parseInt(getParameterByName('interval'), 10);
        getRanking();   
    });
    
    document.onkeyup = function(e) {
        if (e.ctrlKey && e.altKey && e.which === 84) {
            apiUrl = prompt("API URL", "http://jump-api.stt-systems.com:5030");
            getRanking();
        }
    };
    
}