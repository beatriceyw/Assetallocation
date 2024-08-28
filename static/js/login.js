function loginCheck(){
    var data = new FormData(document.forms[0])

    $.ajax({
        data : data,
        type : "POST",
        url : "/assetAllocation/login",
        contentType : false,
        enctype : 'multipart/form-data',
        processData : false,
        success : function(data) {
            if(data.result == 0){
                if(data.message == "password"){
                    alert("비밀번호 확인 바랍니다")
                }else{
                    alert("등록된 유저가 없습니다. 회원가입을 진행하시기 바랍니다.")
                }
                window.location.href = "/assetAllocation/login";
            }else if(data.result == 1 && data.message == "redirect"){
                window.location.href = "/assetAllocation/dashboard";
            }
        },
        error : function(error) {
            console.log(error);
        }
    });

    return false;
}