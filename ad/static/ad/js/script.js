function addMenu(){
  $("#AddControll").empty();
  var NoOfRec = $("#id_menu").val();
  if (NoOfRec > 0) {
    createControll(NoOfRec);
  }
}
      

  function createControll(NoOfRec) {
    var tbl = "";

    for (i = 1; i <= NoOfRec; i++) {

      tbl = 
      "<div class=\"menu-box animate__animated animate__fadeIn\">\n"+
      "<label class=\"menu-main-heading\">Menu "+i+"</label><br>"+ 

      "<label class=\"menu-heading\">Menu Title</label><br>"+
      "<input onblur=\"menuTitleBlur(this)\" oninput=\"menuTitleInput(this)\" type=\"text\" id=\"menu_title_"+i+"\" placeholder=\"Title\" name=\"menu_title_"+i+"\" data-pass=\"0\">"+
      "<label class=\"\" id=\"menu_title_"+i+"_status\"></label><br>"+

      "<label class=\"menu-heading\">Menu Price</label><br>" +
      "<input onblur=\"menuPriceBlur(this)\" oninput=\"menuPriceInput(this)\" id=\"menu_price_"+i+"\" name=\"menu_price_"+i+"\" placeholder=\"Price\" name=\"menu_price_"+i+"\" data-pass=\"0\">"+
      "<label class=\"\" id=\"menu_price_"+i+"_status\"></label><br>"+

      "<label class='menu-heading'>Menu Description</label><br>" +
      "<textarea onblur=\"menuDescriptionBlur(this)\" oninput=\"menuDescriptionInput(this)\" id=\"menu_description_"+i+"\" name=\"menu_description_"+i+"\" style=\"width: 100%;\" placeholder='Description' data-pass=\"0\"></textarea>"+
      "<label class=\"\" id=\"menu_description_"+i+"_status\"></label><br>"+

      "</div>";
      $("#AddControll").append(tbl);
    }

  }

function menuTitleInput(element){
  element.dataset['pass'] = '0';
  $("#"+element.id+"_status").removeClass("animate__anmated animate__bounceIn validation-error validation-success");
  $("#"+element.id+"_status").html('');
  $("#"+element.id).removeClass("border-red border-green");
  input =  $("#"+element.id).val().replace(/^\s+/,"");
  $("#"+element.id).val( input)

  if( input.length > 20){
    $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
    $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Title can\'t exceed 20 characters');
    $("#"+element.id).addClass("border-red");
    $("#"+element.id).val(input.slice(0, 20));
    input = $("#"+element.id).val();
  }

  var pattern = new RegExp(/[~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/); 
  if (pattern.test(input)) {
      $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
      $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Only alphabets are allowed');
      $("#"+element.id).addClass("border-red");
      parking_capacity.value = $("#"+element.id).val(input.replace(/[~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g, ''));
  }
}

function menuTitleBlur(element){
  $("#"+element.id+"_status").removeClass("animate__anmated animate__bounceIn validation-error validation-success");
  $("#"+element.id+"_status").html('');
  $("#"+element.id).removeClass("border-red border-green");
  input = element.value;
  if( input == ""){        
      $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
      $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Title is mandatory');
      $("#"+element.id).addClass("border-red");
      return true;
  }
  if( input.length > 5 ){   
      element.dataset['pass'] = '1';
      $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-success");
      $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Your title has been validated');
      $("#"+element.id).addClass("border-green");
      return true;
  }else{
      $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
      $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>You need to use 5 to 20 characters');
      element.classList.add('border-red');
      return true;
  }
  
}

function menuDescriptionInput(element) {
  element.dataset['pass'] = '0';
  $("#"+element.id+"_status").removeClass("animate__anmated animate__bounceIn validation-error validation-success");
  $("#"+element.id+"_status").html('');
  $("#"+element.id).removeClass("border-red border-green");
  input = $("#"+element.id).val().replace(/^\s+/,"");

  $("#"+element.id).val(input);
  if (input.length > 300) {
    $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
    $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Title can\'t exceed 300 characters');
    $("#"+element.id).addClass("border-red");
    $("#"+element.id).val(input.slice(0, 300));
    input = $("#"+element.id).val();
  } 

}

function menuDescriptionBlur(element) {
  $("#"+element.id+"_status").removeClass("animate__anmated animate__bounceIn validation-error validation-success");
  $("#"+element.id+"_status").html('');
  $("#"+element.id).removeClass("border-red border-green");
  input = $("#"+element.id).val();
  $("#"+element.id).val(input);

  if( input == ""){        
    $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
    $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Description is mandatory');
    $("#"+element.id).addClass("border-red");
    return true;
}
if( input.length > 99 ){   
    element.dataset['pass'] = '1';
    $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-success");
    $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Your description has been validated');
    $("#"+element.id).addClass("border-green");
    return true;
}else{
    $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
    $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>You need to use upto 100 characters');
    element.classList.add('border-red');
    return true;
}

}

function menuPriceInput(element){
  element.dataset['pass'] = '0';
  $("#"+element.id+"_status").removeClass("animate__anmated animate__bounceIn validation-error validation-success");
  $("#"+element.id+"_status").html('');
  $("#"+element.id).removeClass("border-red border-green");
  input =  $("#"+element.id).val().trim();
  $("#"+element.id).val(input);

  if( input.length > 6){
      $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
      $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Use 4 to 6 digits');
      $("#"+element.id).addClass('border-red');
      $("#"+element.id).val(input.slice(0, 6));
      input =  $("#"+element.id).val();
  }
  var pattern = new RegExp(/[a-zA-z~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/); 
  if (pattern.test(input)) {
      $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
      $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Only numbers allowed');
      $("#"+element.id).addClass('border-red');
      $("#"+element.id).val(input.replace(/[[a-zA-z~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g, ''));
      return false;
  }
  
}

function menuPriceBlur(element){
  $("#"+element.id+"_status").removeClass("animate__anmated animate__bounceIn validation-error validation-success");
  $("#"+element.id+"_status").html('');
  $("#"+element.id).removeClass("border-red border-green");
  input = $("#"+element.id).val().trim();
  $("#"+element.id).val(input);

  if( input == ""){        
    $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
    $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Price is mandatory');
    $("#"+element.id).addClass("border-red");
    return true;
}
if( input.length > 3 ){   
    element.dataset['pass'] = '1';
    $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-success");
    $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Your price has been validated');
    $("#"+element.id).addClass("border-green");
    return true;
}else{
    $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
    $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>You need to use 4 to 6 digits');
    element.classList.add('border-red');
    return true;
}

}