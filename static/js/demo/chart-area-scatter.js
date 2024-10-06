var xyValue = []
var myChart
var tooltip_data

window.onload = function(){
  var assetNodeList = document.querySelector("div.col").querySelectorAll("div.card-body.p-2");
  var assetList = Array.from(assetNodeList).map(div => div.innerText)

  myChart = new Chart("myChart", {
    type: "scatter",
    data: {
      datasets: [{
        pointRadius: 3,
        pointBackgroundColor: "rgb(0,0,255)",
        data: xyValue
      }]
    },
    options: {
      scales: {
          xAxes: [{
              scaleLabel: {
                  display: true,
                  labelString: '변동성' // X축 제목
              }
          }],
          yAxes: [{
              scaleLabel: {
                  display: true,
                  labelString: '기대수익률' // Y축 제목
              }
          }]
      },
      legend: {
        display: false,
        // position: 'bottom'
      },
      tooltips: {
          enabled: true,
          callbacks: {
            title:  function(){
              return '자산비중';
            },
            label: function (tooltipItem) {
              let result = assetList.map((label, index) => `${label} : ${tooltip_data[tooltipItem.index][index]}`);
              return result; 
            }
          
          }
      }
    }
  });

  sendAjaxRequest()
}

// AJAX 요청 함수
function sendAjaxRequest() {
  var date = document.forms[1];
  var assetNodeList = document.querySelector("div.col").querySelectorAll("input[type='hidden']");
  var assetList = Array.from(assetNodeList).map(input => input.value)
  
  data = new FormData();
  data.append("start_date", date.children[0].getElementsByTagName('input')[0].value);
  data.append("end_date", date.children[0].getElementsByTagName('input')[1].value);
  data.append("tickers", JSON.stringify(assetList));

  $.ajax({
    data : data,
    type : 'POST',
    url : "/assetAllocation/expectedReturn/efficientFrontier",
    contentType : false,
    enctype : 'multipart/form-data',
    processData : false,
    success : function(data) {
        const expectedReturn = JSON.parse(data)
        for(i=0; i<100; i++){
          xyValue[i]= {x:expectedReturn.vol_arr[i], y:expectedReturn.ret_arr[i]} 
        }
        tooltip_data = expectedReturn.all_weights
        myChart.update();
    },
    error : function(error) {
        console.log(error);
    }
  });
}
  
       