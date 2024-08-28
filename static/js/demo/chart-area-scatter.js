
// var xyValue = [];
// var tooltip_data

// var myChart = new Chart("myChart", {
//   type: "scatter",
//   data: {
//     datasets: [{
//       pointRadius: 4,
//       pointBackgroundColor: "rgb(0,0,255)",
//       data: xyValue
//     }]
//   },
//   options: {
//     legend: {
//       display: false,
//       position: 'bottom'
//     },
//     tooltips: {
//         enabled: true,
//         callbacks: {
//           title:  function(){
//             return '자산비중';
//           },
//           afterBody:  function(tooltipData){
//             z = tooltip_data[tooltipData[0].index]
//             return `${z}`; 
//           },
//           label: function (tooltipData) {
//               var labels = [
//                 ['IGLB(장기투자채권)'],
//                 ['HYG(고수익채권)'],
//                 ['SPY(S&P500)'],
//                 ['MBB(모기지)'],
//                 ['SOXX(반도체)'], 
//                 ['URA(핵)'],
//                 ['PAVE(인프라)'],
//               ]
//               return `${labels}`; 
//           }, 
//         }
//     }
//   }
// });

// $.ajax({
//   async : true,
//   type : 'POST',
//   //expectedReturn value(0~100)
//   data : JSON.stringify({"expectedReturn": "0"}),
//   url : "/assetAllocation/expectedReturn/efficientFrontier",
//   dataType : "json",
//   contentType : "application/json; charset=UTF-8",
//   success : function(data) {
//       const expectedReturn = JSON.parse(data)
//       for(i=0; i<100; i++){
//         xyValue[i]= {x:expectedReturn.vol_arr[i], y:expectedReturn.ret_arr[i]} 
//       }
//       tooltip_data = expectedReturn.all_weights
//       // sharpe_ratio 
//       $(".sharpe_ratio").text(expectedReturn.sharpe_arr.toFixed(2))
//       //수익률
//       $(".IGLB_return").text(expectedReturn.returns[0] * 100 + '%')
//       $(".HYG_return").text(expectedReturn.returns[1] * 100 + '%')
//       $(".SPY_return").text(expectedReturn.returns[2] * 100 + '%') 
//       $(".MBB_return").text(expectedReturn.returns[3] * 100 + '%')
//       $(".SOXX_return").text(expectedReturn.returns[4] * 100 + '%')
//       $(".URA_return").text(expectedReturn.returns[5] * 100 + '%')
//       $(".PAVE_return").text(expectedReturn.returns[6] * 100 + '%')
//       expectedReturnOnchange(50)
//       myChart.update();
//   },
//   error : function(error) {
//       console.log(error);
//   }
// });
     
// function expectedReturnOnchange(value){
//   $(".IGLB_proportion").text((tooltip_data[value-1][0]*100).toFixed(2) + "%")
//   $(".HYG_proportion").text((tooltip_data[value-1][1]*100).toFixed(2) + "%")
//   $(".SPY_proportion").text((tooltip_data[value-1][2]*100).toFixed(2) + "%")
//   $(".MBB_proportion").text((tooltip_data[value-1][3]*100).toFixed(2) + "%")
//   $(".SOXX_proportion").text((tooltip_data[value-1][4]*100).toFixed(2) + "%")
//   $(".URA_proportion").text((tooltip_data[value-1][5]*100).toFixed(2) + "%")
//   $(".PAVE_proportion").text((tooltip_data[value-1][6]*100).toFixed(2) + "%")
//   // $(".KR10YT_return").text((tooltip_data[value-1][7]*100).toFixed(2) + "%")
// }