function getCookie(name){
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function generateUUID() {
    var d = new Date().getTime();
    if(window.performance && typeof window.performance.now === "function"){
        d += performance.now(); //use high-precision timer if available
    }
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (d + Math.random()*16)%16 | 0;
        d = Math.floor(d/16);
        return (c=='x' ? r : (r&0x3|0x8)).toString(16);
    });
    return uuid;
}

var pre_image_id = "";

function generateImageCode(){
    var cur_image_id = generateUUID();
    $("#image img").attr("src", "/api/imagecode?cur_image_id="+cur_image_id+"&pre_image_id="+pre_image_id);
    pre_image_id = cur_image_id;
}

function sendSMSCode(){
    $("#getphonecode").removeAttr("onclick");
    var mobile = $("#mobile").val();
    if(!mobile){
        $("#mobile-err span").html("请填写手机号")
        $("#mobile-err").show();
        $("#getphonecode").attr("onclick", "sendSMSCode();");
        return;
    }
    var imagecode = $("#imagecode").val();
    if (!imagecode){
        $("#imagecode-err span").html("请填写验证码");
        $("#imagecode-err").show();
        $("#getphonecode").attr("onclick", "sendSMSCode();");
        return;
    }

    var data = {"mobile":mobile, "imagecode":imagecode, "imagecodeid":pre_image_id};  //.............................................
    $.ajax({
        url: "/api/smscode",
        method: "POST",
        headers: {"X-XSRFTOKEN":getCookie("_xsrf")},
        data: JSON.stringify(data),
        contentType: "application/json",
        dataType: "json",
        success: function(data){
            if("0" == data.errcode){
                var timing = 30;
                var timeobj = setInterval(function(){
                    $("#getphonecode").html(timing+"秒");
                    timing = timing-1;
                    if(1 == timing){
                        clearInterval(timeobj);
                        $("#getphonecode").html("获取验证码");
                        $("#getphonecode").attr("onclick", "sendSMSCode();");
                    }
                }, 1000)
            }
            else{
                $("#imagecode-err span").html(data.errmsg);
                $("#imagecode-err").show();
                $("#getphonecode").attr("onclick", "sendSMSCode();");
                if(data.errcode == "4001" || data.errcode == "4002" || data.errcode == "4004"){
                    generateImageCode();
                }
            }
        }
    })
}

$(document).ready(function(){
    generateImageCode();
    $("#mobile").focus(function(){
        $("#mobile-err").hide();
    });
    $("#imagecode").focus(function(){
        $("#imagecode-err").hide();
    });
    $("#phonecode").focus(function(){
        $("#phonecode-err").hide();
    });
    $("#password").focus(function(){
        $("#password-err").hide();
        $("#password2-err").hide();
    });
    $("#password2").focus(function(){
        $("#phonecode2-err").hide();
    });

    $("#form-register").submit(function(e){
        e.preventDefault();

        mobile = $("#mobile").val();
        phonecode = $("#phonecode").val();
        password = $("#password").val();
        password2 = $("#password2").val();

        if(!mobile){
            $("#mobile-err span").html("请填写手机号");
            $("#mobile-err").show();
            return;
        }
        if(!phonecode){
            $("#phonecode-err span").html("请填写手机验证码");
            $("#phonecode-err").show();
            return;
        }
        if(!password){
            $("#password-err span").html("请填写密码");
            $("#password-err").show();
            return;
        }
        if(password != password2){
            $("#password2-err span").html("两次密码不一致");
            $("#password2-err").show();
            return;
        }


        var data = {};
        $("#form-register").serializeArray().map(function(x){
            data[x.name]=x.value;
        })

        $.ajax({
            url: "/api/register",
            method: "POST",
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: "json",
            headers: {"X-XSRFTOKEN": getCookie("_xsrf")},
            success: function(data){
                if("0"==data.errcode){
                    location.href = "/";
                }
                else{
                    $("#phonecode-err span").html(data.errmsg);
                    $("#phonecode-err").show();
                }
            }
        })
    })

})