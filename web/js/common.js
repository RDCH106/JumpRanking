
var ranking;
var maxranking = 100;  // Max ranking elements (TOP 100)
var api_url = "http://192.168.1.224:5000"
var update_interval = 5000
var datatable_options = {
                            "order": [[ 1, "desc" ]],
                            "responsive": true
                        } 
    
function printRanking(ranking){
    ranking.forEach(function(arrayItem){            
            $("#ranking tbody").append("<tr><td>"+arrayItem.user
            +"</td><td>"+arrayItem.height
            +"</td></tr>");
        });
        
}
    
function getRanking(region){
    
    $.ajax({type:"GET", url: api_url + "/jumpranking/api/v1/registers", dataType: "json", async: true,
        success: function(data) {            
            printRanking(data.data.slice(0, maxranking));
            ranking =$("#ranking").DataTable(datatable_options);
        }
    });
}

function init(region){
    
    $(document).ready(function () {
         getRanking(region);
         $("#selection").val(region);    
    });
    
    document.onkeyup = function(e) {
        if (e.ctrlKey && e.altKey && e.which == 84) {
            api_url = prompt("API URL", "http://jump-api.stt-systems.com:5030");
            getRanking(region);
        }
    };
    
}