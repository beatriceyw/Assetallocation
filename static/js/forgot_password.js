function emailCheck(){
  var email = document.getElementsByName("email")[0].value

  if (email){
    $.ajax({
      data : JSON.stringify({"email" : email}),
      type : "POST",
      url : "/assetAllocation/forgot_password/emailCheck",
      contentType : "application/json",
      success : function(data) {
          if (data.status == 1){ // 이메일 O
            document.getElementById("emailCheckBtn").classList.add("btn-success");
            document.getElementById("emailCheckBtn").value = "완료"
            document.getElementById("emailCheckBtn").disabled = true;
          } else{                // 이메일 X
            alert("등록된 이메일이 없습니다. 회원가입을 진행해주세요!")
          }
      },
      error : function(error) {
          console.log(error);
      }
    });
  }else{
    alert("이메일 입력 후 비밀번호 변경 가능합니다!")
  }
}

function updatePassword(){
  var password = document.getElementsByName("password")[0].value
  var repeatpassword = document.getElementsByName("repeatPassword")[0].value
  var email = document.getElementsByName("email")[0].value
  var emailCheck = document.getElementById("emailCheckBtn").value

  if(password != repeatpassword){
    alert("비밀번호를 다시 확인하세요.")
    return false;
  }else if(password == repeatpassword && emailCheck == "확인"){
    alert("이메일 중복 확인 후 비밀번호 변경 가능합니다.")
    return false;
  }else if(password == repeatpassword && emailCheck == "완료"){
    $.ajax({
      data : JSON.stringify({"email": email, "password": password}),
      type : "POST",
      url : "/assetAllocation/forgot_password/passwordUpdate",
      contentType : "application/json",
        success : function(data) {
          if(data.status == 1){
            alert("비밀번호 변경이 완료되었습니다. 로그인 후 이용 가능합니다.")
            window.location.href = "/assetAllocation/login";
          }else{
            alert("비밀번호 변경을 재시도 하시기 바랍니다.")
            window.location.href = "/assetAllocation/forgot_password";
          }
        },
        error : function(error) {
            console.log(error);
        }
    });
    return false;
  }
}
