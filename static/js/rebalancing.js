window.onload = function(){
	google.charts.load('current', {'packages':['corechart']});
    google.charts.load('current', {packages: ['corechart', 'bar']});
    google.charts.setOnLoadCallback(drawChart);
    google.charts.setOnLoadCallback(drawMaterial);

    // 각 자산 목록에 대해 AJAX 요청 보내기
    sendAjaxRequest("MP1", "medium");
    sendAjaxRequest("MP2", "medium");
    sendAjaxRequest("MP3", "medium");
}

// AJAX 요청 함수
function sendAjaxRequest(mp_ver, risk_gauge) {
    var assetList;
    var assetNodeList;
    var start_date;
    var end_date;

    if(mp_ver == "MP1"){
        assetNodeList = document.getElementById("mp1_selectbox").querySelector(".col").querySelectorAll("input[type='hidden']");
        assetList = Array.from(assetNodeList).map(input => input.value);
        start_date = document.getElementById("start_date1").value
        end_date = document.getElementById("end_date1").value
    }else if(mp_ver == "MP2"){
        assetNodeList = document.getElementById("mp2_selectbox").querySelector(".col").querySelectorAll("input[type='hidden']");
        assetList = Array.from(assetNodeList).map(input => input.value);
        start_date = document.getElementById("start_date2").value
        end_date = document.getElementById("end_date2").value
    }else if(mp_ver == "MP3"){
        assetNodeList = document.getElementById("mp3_selectbox").querySelector(".col").querySelectorAll("input[type='hidden']");
        assetList = Array.from(assetNodeList).map(input => input.value);
        start_date = document.getElementById("start_date3").value
        end_date = document.getElementById("end_date3").value
    }
    $.ajax({
        data: JSON.stringify({"mp_ver": mp_ver, "risk_gauge": risk_gauge, "tickers": JSON.stringify(assetList), "start_date": start_date, "end_date": end_date}),
        type: "POST",
        url: "/assetAllocation/rebalancing",
        contentType: "application/json",
        success: function(data) {
            drawChart(mp_ver, assetList, data)
            drawMaterial(mp_ver, assetList, data)
            drawTable(mp_ver, assetList, data)
        },
        error: function(error) {
            console.log(error);
        }
    });
}
// 구글 자산 배분 차트 데이터 설정 및 차트 그리기
function drawChart(mp_ver, assetList, asset_data) {
    if (mp_ver && assetList && asset_data){
        
        var data = new google.visualization.DataTable();

        data.addColumn('string', '자산리스트');
        data.addColumn('number', '자산비중');

        var rows = [];

        for (var i = 0; i < assetList.length; i++) {
            rows.push([assetList[i], asset_data.weights[i]]);
        }

        data.addRows(rows);
        
        if (mp_ver == "MP1"){
            var options = {
                title: 'MP1 자산비중',
                legend: { position: 'none' },
                colors: ['#4e73df', '#858796', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b', '#5a5c69'] // Custom colors
            };
            var chart1 = new google.visualization.PieChart(document.getElementById('piechart1'));
            chart1.draw(data, options);
        }else if(mp_ver == "MP2"){
            var options = {
                title: 'MP2 자산비중',
                legend: { position: 'none' },
                colors: ['#4e73df', '#858796', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b', '#5a5c69'] // Custom colors
            };
            var chart2 = new google.visualization.PieChart(document.getElementById('piechart2'));
            chart2.draw(data, options);
        }else if(mp_ver == "MP3"){
            var options = {
                title: 'MP3 자산비중',
                legend: { position: 'none' },
                colors: ['#4e73df', '#858796', '#1cc88a', '#36b9cc', '#f6c23e', '#e74a3b', '#5a5c69'] // Custom colors
            };
            var chart3 = new google.visualization.PieChart(document.getElementById('piechart3'));
            chart3.draw(data, options);
        }
    }
}
// 구글 연간 누적 수익률, 연간 누적 변동성
function drawMaterial(mp_ver, assetList, asset_data) {
    if (mp_ver && assetList && asset_data){

        var data = new google.visualization.DataTable();
    
        data.addColumn('string', '자산');
        data.addColumn('number', '연간 누적 수익률');
        data.addColumn('number', '연간 누적 변동성');

        var rows = [];

        for (var i = 0; i < assetList.length; i++) {
            rows.push([assetList[i], asset_data.cagr_returns[i], asset_data.cagr_vol[i]]);
        }

        data.addRows(rows);

        var options = {
            title: '연간 누적 수익률, 연간 누적 변동성',
            legend: { position: 'none' },
            series: {
                0: { type: 'bars', color: '#4e73df' }, // Color for bars (cagr_returns)
                1: { type: 'bars', color: '#f6c23e' }   // Color for line (cagr_vol)
              }        
        };

        if (mp_ver == "MP1"){
            var materialChart1 = new google.charts.Bar(document.getElementById('chart_div1'));
            materialChart1.draw(data, options);
        }else if(mp_ver == "MP2"){
            var materialChart2 = new google.charts.Bar(document.getElementById('chart_div2'));
            materialChart2.draw(data, options);
        }else if(mp_ver == "MP3"){
            var materialChart3 = new google.charts.Bar(document.getElementById('chart_div3'));
            materialChart3.draw(data, options);
        }
    }
}
// sharpe ratio, 기대수익률, 변동성 Table 
function drawTable(mp_ver, assetList, asset_data){
    if (mp_ver == "MP1" && asset_data){
        // MP1 Table
        document.getElementById("dataTable1").getElementsByTagName('td')[0].innerText = asset_data.sharpe_ratio
        document.getElementById("dataTable1").getElementsByTagName('td')[1].innerText = asset_data.port_ret
        document.getElementById("dataTable1").getElementsByTagName('td')[2].innerText = asset_data.port_vol
        // Nasdaq Table
        document.getElementById("dataTable2").getElementsByTagName('td')[0].innerText = asset_data.index_port_ret[0]
        document.getElementById("dataTable2").getElementsByTagName('td')[3].innerText = asset_data.index_port_vol[0]
        // s&p500 Table
        document.getElementById("dataTable2").getElementsByTagName('td')[1].innerText = asset_data.index_port_ret[1]
        document.getElementById("dataTable2").getElementsByTagName('td')[4].innerText = asset_data.index_port_vol[1]
        // kospi Table
        document.getElementById("dataTable2").getElementsByTagName('td')[2].innerText = asset_data.index_port_ret[2]
        document.getElementById("dataTable2").getElementsByTagName('td')[5].innerText = asset_data.index_port_vol[2]
    }else if(mp_ver == "MP2" && asset_data){
        // MP2 Table
        document.getElementById("dataTable3").getElementsByTagName('td')[0].innerText = asset_data.sharpe_ratio
        document.getElementById("dataTable3").getElementsByTagName('td')[1].innerText = asset_data.port_ret
        document.getElementById("dataTable3").getElementsByTagName('td')[2].innerText = asset_data.port_vol
        // Nasdaq Table
        document.getElementById("dataTable4").getElementsByTagName('td')[0].innerText = asset_data.index_port_ret[0]
        document.getElementById("dataTable4").getElementsByTagName('td')[3].innerText = asset_data.index_port_vol[0]
        // s&p500 Table
        document.getElementById("dataTable4").getElementsByTagName('td')[1].innerText = asset_data.index_port_ret[1]
        document.getElementById("dataTable4").getElementsByTagName('td')[4].innerText = asset_data.index_port_vol[1]
        // kospi Table
        document.getElementById("dataTable4").getElementsByTagName('td')[2].innerText = asset_data.index_port_ret[2]
        document.getElementById("dataTable4").getElementsByTagName('td')[5].innerText = asset_data.index_port_vol[2]
    }else if(mp_ver == "MP3" && asset_data){
        // MP3 Table
        document.getElementById("dataTable5").getElementsByTagName('td')[0].innerText = asset_data.sharpe_ratio
        document.getElementById("dataTable5").getElementsByTagName('td')[1].innerText = asset_data.port_ret
        document.getElementById("dataTable5").getElementsByTagName('td')[2].innerText = asset_data.port_vol
        // Nasdaq Table
        document.getElementById("dataTable6").getElementsByTagName('td')[0].innerText = asset_data.index_port_ret[0]
        document.getElementById("dataTable6").getElementsByTagName('td')[3].innerText = asset_data.index_port_vol[0]
        // s&p500 Table
        document.getElementById("dataTable6").getElementsByTagName('td')[1].innerText = asset_data.index_port_ret[1]
        document.getElementById("dataTable6").getElementsByTagName('td')[4].innerText = asset_data.index_port_vol[1]
        // kospi Table
        document.getElementById("dataTable6").getElementsByTagName('td')[2].innerText = asset_data.index_port_ret[2]
        document.getElementById("dataTable6").getElementsByTagName('td')[5].innerText = asset_data.index_port_vol[2]
    }
}
function remove_btn(btn_class){
    btn_class.parentElement.parentElement.parentElement.remove()
}
function add_btn(btn_class){
    var selectedOptionText = btn_class.options[btn_class.selectedIndex].text
    var selectedOptionValue = btn_class.options[btn_class.selectedIndex].value
    var slectedCount = btn_class.parentElement.nextElementSibling.childElementCount
    var colorOption = btn_class.parentElement.nextElementSibling.lastElementChild.className
    var colorOptionClass
    if (slectedCount == 7){
        alert("선택할 수 있는 자산 개수는 7개 입니다.")
    }else{
        if(colorOption == "card mr-3 border-left-primary h-100"){
            colorOptionClass = "card mr-3 border-left-secondary h-100"
        }else if(colorOption == "card mr-3 border-left-secondary h-100"){
            colorOptionClass = "card mr-3 border-left-success h-100"
        }else if(colorOption == "card mr-3 border-left-success h-100"){
            colorOptionClass = "card mr-3 border-left-info h-100"
        }else if(colorOption == "card mr-3 border-left-info h-100"){
            colorOptionClass = "card mr-3 border-left-warning h-100"
        }else if(colorOption == "card mr-3 border-left-warning h-100"){
            colorOptionClass = "card mr-3 border-left-danger h-100"
        }else if(colorOption == "card mr-3 border-left-danger h-100"){
            colorOptionClass = "card mr-3 border-left-dark h-100"
        }else if(colorOption == "card mr-3 border-left-dark h-100"){
            colorOptionClass = "card mr-3 border-left-primary h-100"
        }
        
        btn_class.parentElement.nextElementSibling.insertAdjacentHTML('beforeend', 
            "<div class='" + colorOptionClass + "'>" +
                "<div class='row no-gutters align-items-center'>" +
                    "<div class='col mr-2'>" +
                        "<div class='row no-gutters align-items-center'>" +
                            "<div class='col-auto'>" +
                                "<div class='card-body p-2'>" + selectedOptionText + "</div>" +
                                "<input type='hidden' value='"+ selectedOptionValue + "'>" +
                            "</div>" +
                        "</div>" +
                    "</div>" +
                    "<div class='col-auto'>" + 
                        "<button class='btn' onclick='remove_btn(this)'>X</button>" +
                    "</div>" +
                "</div>" +
            "</div>"
        )
        // sendAjaxRequest
        var slectedCount = btn_class.parentElement.nextElementSibling.childElementCount
        if (slectedCount == 7){
            var mp_ver = btn_class.closest('.card-body').previousElementSibling.querySelector('h6').textContent
            var risk_gauge = btn_class.closest('.card-body').previousElementSibling.querySelector('select').value
            if(mp_ver == "MP1"){
                if(risk_gauge = "Risk gauge"){
                    sendAjaxRequest(mp_ver, "medium")
                }else{
                    sendAjaxRequest(mp_ver, risk_gauge)
                }
            }else if(mp_ver == "MP2"){
                if(risk_gauge = "Risk gauge"){
                    sendAjaxRequest(mp_ver, "medium")
                }else{
                    sendAjaxRequest(mp_ver, risk_gauge)
                }
            }else if(mp_ver == "MP3"){
                if(risk_gauge = "Risk gauge"){
                    sendAjaxRequest(mp_ver, "medium")
                }else{
                    sendAjaxRequest(mp_ver, risk_gauge)
                }
            } 
        }
    }
}