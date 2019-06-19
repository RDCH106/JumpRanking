
var ranking;
var maxranking = 100;  // Max ranking elements (TOP 100)
var api_url = "http://192.168.1.224:5000"
    
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
            ranking =$("#ranking").DataTable( 
            {
                "order": [[ 1, "desc" ]],
                "responsive": true
            } );
        }
    });
}

function init(region){
    
    $(document).ready(function () {
         getRanking(region);
         $("#selection").val(region);    
    });
    
}