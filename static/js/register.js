function registerInfoCheck(){
  var password = document.getElementsByName("password")[0].value
  var repeatpassword = document.getElementsByName("repeatPassword")[0].value
  var emailDoubleCheck = document.getElementById("emailDoubleCheckBtn").value

  if(password != repeatpassword){
    alert("비밀번호를 다시 확인하세요.")
  }else if(password == repeatpassword && emailDoubleCheck == "사용가능"){
    this.parentNode.submit()
  }
}

function emailDoubleCheck(){
  var email = document.getElementsByName("email")[0].value
  if (email){
    $.ajax({
      data : JSON.stringify({"email" : email}),
      type : "POST",
      url : "/assetAllocation/register/emailDoubleCheck",
      contentType : "application/json",
      success : function(data) {
        if (data.status == 0){ // 로그인 중복 X
            document.getElementById("emailDoubleCheckBtn").classList.add("btn-success");
            document.getElementById("emailDoubleCheckBtn").value = "사용가능"
            document.getElementById("emailDoubleCheckBtn").disabled = True;
          }else{                // 로그인 중복 O
            alert("이미 등록된 이메일입니다!")
          }
      },
      error : function(error) {
          console.log(error);
      }
    });
  }else{
    alert("이메일 입력 후 중복체크 가능합니다!")
  }
}