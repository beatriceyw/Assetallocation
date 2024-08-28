google.charts.load('current', {'packages':['treemap']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Location', 'Parent', 'Market trade volume (size)', 'Market increase/decrease (color)'],
    ['ETF', null, 0, 0],

    // Equity index section
    ['equity index', 'ETF', 21, 300],
    ['Samsung KODEX MSCI World ETF', 'equity index', 1, 300],
    ['Mirae Asset Tiger200 ETF', 'equity index', 1, 250],
    ['Mirae Asset TIGER China A 300 ETF', 'equity index', 1, 200],
    ['Mirae Asset TIGER KOSDAQ 150 ETF', 'equity index', 1, 150],
    ['Mirae Asset TIGER Nasdaq 100 ETF', 'equity index', 1, 100],
    ['iShares MSCI Emerging Markets ETF', 'equity index', 1, 50],
    ['SPDR S&P 500 ETF Trust', 'equity index', 1, 0],
    ['Vanguard Small-Cap Growth Index Fund;ETF', 'equity index', 1, -50],
    ['Vanguard Growth Index Fund;ETF', 'equity index', 1, -100],
    ['Vanguard Value Index Fund;ETF', 'equity index', 1, -150],
    ['Direxion Daily Financial Bull 3x Shares ETF', 'equity index', 1, -200],
    ['Direxion Daily Small Cap Bull 3X ETF', 'equity index', 1, -250],
    ['SAMSUNG KODEX ChiNext ETF(Synth)', 'equity index', 1, -300],
    ['KIM KINDEX Vietnam VN30 ETF-Synth', 'equity index', 1, 300],

    // Theme ETF section
    ['theme ETF', 'ETF', 8, 300],
    ['Clean energy (tech) - renewables', 'theme ETF', 7, 250],
    ['Global X YieldCo & Renewable Energy Income ETF', 'Clean energy (tech) - renewables', 1, 200],
    ['VanEck Vectors Low Carbon Energy ETF', 'Clean energy (tech) - renewables', 1, 150],
    ['First Trust NASDAQ Clean Edge Green Energy Index Fund', 'Clean energy (tech) - renewables', 1, 100],
    ['Invesco WilderHill Clean Energy ETF', 'Clean energy (tech) - renewables', 1, 50],
    ['iShares Global Clean Energy ETF', 'Clean energy (tech) - renewables', 1, 0],
    ['First Trust Global Wind Energy ETF', 'Clean energy (tech) - renewables', 1, -50],
    ['ALPS Clean Energy ETF', 'Clean energy (tech) - renewables', 1, -100],

    ['Lithium and Battery', 'theme ETF', 1, 300],
    ['Global X Lithium & Battery Tech ETF', 'Lithium and Battery', 1, 250],

    ['water', 'theme ETF', 2, 200],
    ['Invesco Water Resources ETF', 'water', 1, 150],
    ['Invesco S&P Global Water Index ETF', 'water', 1, 100],

    ['China consumer', 'theme ETF', 1, 50],
    ['Mirae Asset TIGER China Consumer Theme ETF', 'China consumer', 1, 0],

    ['Platform - FAANG', 'theme ETF', 5, -50],
    ['Alibaba Group Holding ADR Representing 8 Ord Shs', 'Platform - FAANG', 1, -100],
    ['Mirae Asset TIGER MorningStar ExponentialTech ETFH', 'Platform - FAANG', 1, -150],
    ['Direxion Daily Technology Bull 3X Shares ETF', 'Platform - FAANG', 1, -200],
    ['Invesco QQQ Trust Series 1 (FAANG)', 'Platform - FAANG', 1, -250],
    ['Technology Select Sector SPDR Fund', 'Platform - FAANG', 1, -300],

    ['semi conductor', 'theme ETF', 2, 300],
    ['Taiwan Semiconductor Manufacturing ADR Representing Five Ord Shs', 'semi conductor', 1, 250],
    ['VanEck Vectors Semiconductor ETF', 'semi conductor', 1, 200],

    ['ESG', 'theme ETF', 2, 150],
    ['Samsung KODEX MSCI Korea ESG Universal ETF', 'ESG', 1, 100],
    ['Mirae Asset TIGER MSCI Korea ESG Universal ETF', 'ESG', 1, 50],

    ['healthcare and bio tech', 'theme ETF', 5, 0],
    ['Health Care Select Sector SPDR Fund', 'healthcare and bio tech', 1, -50],
    ['Global X Genomics & Biotechnology ETF', 'healthcare and bio tech', 1, -100],
    ['iShares Nasdaq Biotechnology Etf', 'healthcare and bio tech', 1, -150],
    ['Samsung KODEX Synth-US Biotech ETF', 'healthcare and bio tech', 1, -200],
    ['Mirae Asset TIGER Health Care ETF', 'healthcare and bio tech', 1, -250],

    ['remote solution - telemedicine & digital health', 'theme ETF', 2, -300],
    ['Global X Telemedicine & Digital Health ETF (EDOC - 2020.7.29)', 'remote solution - telemedicine & digital health', 1, 300],
    ['medtronic', 'remote solution - telemedicine & digital health', 1, 250],

    ['Fintech', 'theme ETF', 1, 200],
    ['Global X FinTech ETF', 'Fintech', 1, 150],

    ['AI & Robotics', 'theme ETF', 4, 100],
    ['Global X Robotics & Artificial Intelligence ETF', 'AI & Robotics', 1, 50],
    ['First Trust Nasdaq Artificial Intelligence and Robotics ETF', 'AI & Robotics', 1, 0],
    ['iShares Robotics and Artificial Intelligence Multisector ETF', 'AI & Robotics', 1, -50],
    ['ARK Autonomous Technology & Robotics ETF', 'AI & Robotics', 1, -100],

    ['cloud computing', 'theme ETF', 1, -150],
    ['Global X Cloud Computing ETF', 'cloud computing', 1, -200],

    ['game & e-sports', 'theme ETF', 2, -250],
    ['VanEck Vectors Video Gaming and eSports ETF', 'game & e-sports', 1, -300],
    ['Global X Video Games & Esports ETF', 'game & e-sports', 1, 300],

    ['aerospace & defense', 'theme ETF', 1, 250],
    ['iShares US Aerospace & Defense ETF', 'aerospace & defense', 1, 200],

    ['EV and future mobility + self driving + smart mobility + Robotics hw', 'theme ETF', 3, 150],
    ['KraneShares Electric Vehicles and Future Mobility Index ETF', 'EV and future mobility + self driving + smart mobility + Robotics hw', 1, 100],
    ['iShares Self-Driving EV and Tech ETF', 'EV and future mobility + self driving + smart mobility + Robotics hw', 1, 50],
    ['SPDR S&P Kensho Smart Mobility ETF', 'EV and future mobility + self driving + smart mobility + Robotics hw', 1, 0],

    ['cyber security', 'theme ETF', 3, -50],
    ['iShares Cybersecurity and Tech ETF', 'cyber security', 1, -100],
    ['ETFMG Prime Cyber Security ETF', 'cyber security', 1, -150],
    ['First Trust NASDAQ Cybersecurity ETF', 'cyber security', 1, -200],

    ['data sharing', 'theme ETF', 1, -250],
    ['Amplify Transformational Data Sharing ETF', 'data sharing', 1, -300],

    ['OLED', 'theme ETF', 2, 300],
    ['Coherent', 'OLED', 1, 250],
    ['Universal Display', 'OLED', 1, 200],

    ['5G and IOT infra', 'theme ETF', 1, 150],
    ['Global X Internet of Things ETF', '5G and IOT infra', 1, 100],

    ['3D printing', 'theme ETF', 2, 50],
    ['3Dsystems', '3D printing', 1, 0],
    ['Cellink ', '3D printing', 1, -50],

    ['3D sensor', 'theme ETF', 3, -100],
    ['Lumentum', '3D sensor', 1, -150],
    ['Finisar', '3D sensor', 1, -200],
    ['Viavi', '3D sensor', 1, -250],

    // Bond index section
    ['bond index', 'ETF', 6, -300],
    ['Samsung KODEX Treasury Bond ETF', 'bond index', 1, 300],
    ['iShares Core US Aggregate Bond ETF', 'bond index', 1, 250],
    ['iShares US Treasury Bond ETF', 'bond index', 1, 200],
    ['iShares 1-3 Year Treasury Bond ETF', 'bond index', 1, 150],
    ['Vanguard Total Bond Market Index Fund;ETF', 'bond index', 1, 100],
    ['Vanguard Short-Term Bond Index Fund;ETF', 'bond index', 1, 50],

    // High yield bond ETF section
    ['high yield bond ETF', 'ETF', 8, 0],
    ['SPDR Bloomberg Barclays Convertible Securities ETF', 'high yield bond ETF', 1, -50],
    ['iShares iBoxx $ High Yield Corporate Bond ETF', 'high yield bond ETF', 1, -100],
    ['iShares iBoxx $ Inv Grade Corporate Bond ETF', 'high yield bond ETF', 1, -150],
    ['SPDR Bloomberg Barclays High Yield Bond ETF', 'high yield bond ETF', 1, -200],
    ['Global X NASDAQ 100 Covered Call ETF', 'high yield bond ETF', 1, -250],
    ['PIMCO Enhanced Short Maturity Active Exch Tr', 'high yield bond ETF', 1, -300],
    ['Xtrackers USD High Yld Corporate Bd ETF', 'high yield bond ETF', 1, 300],
    ['KB KBSTAR Mid Credit Bond Securities ETF', 'high yield bond ETF', 1, 250],

    // REIT section
    ['REIT', 'ETF', 2, 200],
    ['iShares MBS ETF', 'REIT', 1, 150],
    ['Vanguard Real Estate Index Fund;ETF', 'REIT', 1, 100],

    // Infrastructure section
    ['infra', 'ETF', 5, 50],
    ['Pacer Benchmark Data & Infrastructure RE SCTR', 'infra', 1, 0],
    ['Global X US Infrastructure Development ETF', 'infra', 1, -50],
    ['FlexShares STOXX Global Broad Infrastructure Index Fund', 'infra', 1, -100],
    ['iShares Global Infrastructure ETF', 'infra', 1, -150],
    ['SPDR S&P Global Infrastructure ETF', 'infra', 1, -200],

    // Commodity section
    ['commodity', 'ETF', 10, -250],
    ['Samsung KODEX Gold Futures Special Asset ETF H', 'commodity', 1, -300],
    ['SPDR Gold Shares', 'commodity', 1, 300],
    ['Invesco DB Energy Fund', 'commodity', 1, 250],
    ['Invesco DB Base Metals Fund', 'commodity', 1, 200],
    ['Invesco DB Agriculture Fund', 'commodity', 1, 150],
    ['Mirae Asset TIGER WTI Futures ETF', 'commodity', 1, 100],
    ['Mirae Asset TIGER Metal Futures ETF', 'commodity', 1, 50],
    ['Mirae Asset TIGER Precious Metal Futures ETF', 'commodity', 1, 0],
    ['Global X Uranium ETF', 'commodity', 1, -50],
    ['FlexShares Morningstar Global Upstream Natural Resources Ind…', 'commodity', 1, -100],

    // Money Market Fund (MMF) section
    ['MMF', 'ETF', 3, -150],
    ['SPDR Bloomberg Barclays 1-3 Month T-Bill ETF', 'MMF', 1, -200],
    ['SAMSUNG KODEX KRW CASH PLUS ETF', 'MMF', 1, -250],
    ['MIRAE Asset TIGER Money Market Active ETF', 'MMF', 1, -300],

    // Inverse (short hedge) section
    ['inverse (short hedge)', 'ETF', 3, 300],
    ['Mirae Asset TIGER Inverse Derivatives ETF', 'inverse (short hedge)', 1, 250],
    ['ProShares Short S&P500 ETF', 'inverse (short hedge)', 1, 200],
    ['iPath Series B S&P 500 VIX Short-Term Futures ETN', 'inverse (short hedge)', 1, 150],

    // Income section
    ['income', 'ETF', 4, 100],
    ['iShares Preferred and Income Securities ETF', 'income', 1, 50],
    ['SPDR S&P Dividend ETF', 'income', 1, 0],
    ['iShares Core High Dividend Etf', 'income', 1, -50],
    ['Invesco S&P 500 High Div Low Volatility ETF', 'income', 1, -100]
  ]);

  var tree = new google.visualization.TreeMap(document.getElementById('chart_div'));

  tree.draw(data, {
    minColor: '#a1c4fd',
    maxColor: '#c2e9fb',
    headerHeight: 15,
    fontColor: 'black',
    showScale: false,
    maxPostDepth: 2,
    maxDepth: 1,
    generateTooltip : showFullTooltip,
  });
  
  // tootip 생성
  function showFullTooltip(row, size, value) {
    return '<div style="background:#fff; padding:10px; border-style:solid">' +
            '<span style="font-family:Courier"><b>' + data.getValue(row, 0) +
            '</b></span><br>' +
            '하위 분류: ' + size 
  }

  // 'select' 이벤트 리스너 추가
  google.visualization.events.addListener(tree, 'select', function() {
    var selection = tree.getSelection();
    var selectedItem = selection[0];
    var selectedRow = selectedItem.row;
    var size = data.getValue(selectedRow, 2)
    var stock_name = data.getValue(selectedRow, 0)

    if (size == 1){
      $.ajax({
          data : JSON.stringify({"stock_name" : stock_name}),
          type : "POST",
          url : "/assetAllocation/assetInfo/etf_detail",
          contentType : "application/json",
          success : function(data) {	
              console.log(data)
              if (data){
                document.getElementById("dataTable1").getElementsByTagName('td')[0].innerText = data.NAME
                document.getElementById("dataTable1").getElementsByTagName('td')[1].innerText = data.RIC
                document.getElementById("dataTable1").getElementsByTagName('td')[2].innerText = data.BLOOMBERG_CODE_EX
                document.getElementById("dataTable1").getElementsByTagName('td')[3].innerText = data.TICKER
                document.getElementById("dataTable1").getElementsByTagName('td')[4].innerText = data.ID_ISIN
                document.getElementById("dataTable1").getElementsByTagName('td')[5].innerText = data.FUND_ASSET_CLASS_FOCUS
                document.getElementById("dataTable1").getElementsByTagName('td')[6].innerText = data.Issue_Market_Cap
                document.getElementById("dataTable1").getElementsByTagName('td')[7].innerText = data.CUSIP_Code
              }else {
                document.getElementById("dataTable1").getElementsByTagName('td')[0].innerText = ""
                document.getElementById("dataTable1").getElementsByTagName('td')[1].innerText = ""
                document.getElementById("dataTable1").getElementsByTagName('td')[2].innerText = ""
                document.getElementById("dataTable1").getElementsByTagName('td')[3].innerText = ""
                document.getElementById("dataTable1").getElementsByTagName('td')[4].innerText = ""
                document.getElementById("dataTable1").getElementsByTagName('td')[5].innerText = ""
                document.getElementById("dataTable1").getElementsByTagName('td')[6].innerText = ""
                document.getElementById("dataTable1").getElementsByTagName('td')[7].innerText = ""
              }
          },
          error : function(error) {
              console.log(error);
          }
      });
    }
  });

};
