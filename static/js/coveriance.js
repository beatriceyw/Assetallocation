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
    }
}
function mp_data(mp_ver){
    var cov_data;
    var assetNodeList;

    if (mp_ver == "MP1"){
        cov_data = document.forms[1]
        assetNodeList = document.getElementById("mp1_selectbox").querySelector(".col").querySelectorAll("input[type='hidden']")
    }else if(mp_ver == "MP2"){
        cov_data = document.forms[2]
        assetNodeList = document.getElementById("mp2_selectbox").querySelector(".col").querySelectorAll("input[type='hidden']")
    }else if(mp_ver == "MP3"){
        cov_data = document.forms[3]
        assetNodeList = document.getElementById("mp3_selectbox").querySelector(".col").querySelectorAll("input[type='hidden']")
    }
 
    var assetList = Array.from(assetNodeList).map(input => input.value)
    data = new FormData();
    data.append("mp_ver", mp_ver);
    data.append("start_date", cov_data.children[0].getElementsByTagName('input')[0].value);
    data.append("end_date", cov_data.children[0].getElementsByTagName('input')[1].value);
    data.append("tickers", JSON.stringify(assetList));

    $.ajax({
        data : data,
        type : "POST",
        url : "/assetAllocation/coveriance",
        contentType : false,
        enctype : 'multipart/form-data',
        processData : false,
        success : function(data) {	
            if(data.result == 1 && mp_ver == "MP1"){
                document.getElementById("dataTable1").innerHTML = data.covar_html_thead + data.covar_html_tbody
            }else if(data.result == 1 && mp_ver == "MP2"){
                document.getElementById("dataTable2").innerHTML = data.covar_html_thead + data.covar_html_tbody
            }else if(data.result == 1 && mp_ver == "MP3"){
                document.getElementById("dataTable3").innerHTML = data.covar_html_thead + data.covar_html_tbody
            }		
        },
        error : function(error) {
            console.log(error);
        }
    });

}
