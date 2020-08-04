
title = document.getElementById("id_title");
title.addEventListener("input", validateTitle);
title_status = document.getElementById("title_status"); 
title.addEventListener("blur", validateTitleComplete);


function validateTitle(e) {
    title.dataset['pass'] = '0';
    title.classList.remove('border-green', 'border-red');
    title_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
    title_status.innerHTML = '';
    input = title.value.replace(/^\s+/,"");
    title.value = input; 
    var pattern = new RegExp(/[~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/); 
    if (input.length > 20 ) {
        title.classList.add("border-red");
        title_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        title_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You can only use upto 20 characters';
        title.value = input.slice(0, 20);
        input = title.value;
    }
    if (pattern.test(input)) {
        title.classList.add("border-red");
        title_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        title_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You can only use characters and spaces';
        title.value = input.replace(/[~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g, '');
    }
}
function validateTitleComplete(e) {
    title.classList.remove('border-green', 'border-red');
    title_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
    title_status.innerHTML = '';
    input = e.target.value;
    if (input == "" ){
        title.classList.add('border-red');
        title_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        title_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You can\'t leave a mandatory field empty';
        return false;
    }
    if (input.length < 10) {
        title.classList.add('border-red');
        title_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        title_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You must enter more than 10 characters';
        return false;
    }else{
        title.classList.add('border-green');
        title_status.classList.add('validation-success', 'animate__animated', 'animate__bounceIn');
        title_status.innerHTML = '<i class="fas fa-check-square pr-1"></i>Your title has been validated';
        title.dataset['pass'] = '1';
        return true;
    }

}

id_category = document.getElementById("id_category");
id_category.addEventListener("blur", showOkay);
category_status = document.getElementById("category_status"); 
id_category.addEventListener("change", showOkay);
function showOkay(){
    id_category.dataset['pass'] = '0';
    category_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
    category_status.innerHTML = '';
    id_category.classList.remove('border-red', 'border-green');
    if(id_category.value != 'Category'){
        id_category.dataset['pass'] = '1';
        category_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-success');
        category_status.innerHTML = '<i class="fas fa-check-square pr-1 pl-1"></i>Your category has been selected';
        id_category.classList.add('border-green');
        return true;
    }else{
        category_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        category_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1 pl-1"></i>You can\t leave a mandatory field empty';
        id_category.classList.add('border-red');
        return false;
    }
}


id_city = document.getElementById("id_city");
id_city.addEventListener("blur", showOkay2);
id_city.addEventListener("change", showOkay2);
city_status = document.getElementById("city_status"); 

function showOkay2(){
    id_city.dataset['pass'] = '0';
    city_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
    city_status.innerHTML = '';
    id_city.classList.remove('border-red', 'border-green');
    if(id_city.value != 'City'){
        id_city.dataset['pass'] = '1';
        city_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-success');
        city_status.innerHTML = '<i class="fas fa-check-square pr-1 pl-1"></i>Your city has been selected';
        id_city.classList.add('border-green');
        addAreas();
        return true;
    }else{
        city_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        city_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1 pl-1"></i>You can\t leave a mandatory field empty';
        id_city.classList.add('border-red');
        return false;
    }
}
function addAreas() {
    var city =  document.getElementById('id_city').value; 
    var area =  document.getElementById('id_area');

    var lahore = ["Johar Town","Model Town","PIA Road"];
    var karachi = ["K-Town","Nazimabad","Malir"];
    var islamabad = ["DHA","Bahria Town","Gulberg"]; 
    for (o = area.length - 1; o > 0; o--) {
            area.remove(o);
    }  
    if( city == 'Lahore' ){    
        for(var i = 0; i < lahore.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = lahore[i];
            opt.value = lahore[i];
            area.appendChild(opt);
            area.disabled = false;
        }
    }else if( city == 'Karachi'){
        for(var i = 0; i < karachi.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = karachi[i];
            opt.value = karachi[i];
            area.appendChild(opt);
            area.disabled = false;
        }
    }else if( city == 'Islamabad'){
        for(var i = 0; i < islamabad.length; i++) {
            var opt = document.createElement('option');
            opt.innerHTML = islamabad[i];
            opt.value = islamabad[i];
            area.appendChild(opt);
            area.disabled = false;
        }
    }     
}

id_area = document.getElementById("id_area");
id_area.addEventListener("blur", showOkay3);
id_area.addEventListener("change", showOkay3);
area_status = document.getElementById("area_status"); 

function showOkay3(){
    id_area.dataset['pass'] = '0';
    area_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
    area_status.innerHTML = '';
    id_area.classList.remove('border-red', 'border-green');
    if(id_area.value != 'Area'){
        id_area.dataset['pass'] = '1';
        area_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-success');
        area_status.innerHTML = '<i class="fas fa-check-square pr-1 pl-1"></i>Your city has been selected';
        id_area.classList.add('border-green');
        return true;
    }else{
        area_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        area_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1 pl-1"></i>You can\t leave a mandatory field empty';
        id_area.classList.add('border-red');
        return false;
    }
}


address = document.getElementById("id_address");
address_status = document.getElementById("address_status");
address.addEventListener("input", validateAddress);
address.addEventListener("blur", validateAddressComplete);
function validateAddress(e) {
    address.dataset['pass'] = '0';
    address_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
    address.classList.remove('border-red', 'border-green');
    address_status.innerHTML = "";
    input = e.target.value.replace(/^\s+/,"");
    address.value = input;

    if (input.length > 150){
        address.classList.add('border-red');
        address_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        address_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You can\'t enter more than 150 characters';
        address.value = input.slice(0, 150);
        return false;    
    }
    
}
function validateAddressComplete(e) {
    address_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
    address.classList.remove('border-red', 'border-green');
    address_status.innerHTML = "";
    input = e.target.value;
    address.value = input;
    if (input == "" ){
        address.classList.add('border-red');
        address_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        address_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You can\'t leave a mandatory field empty';
        return false;
    }
    if (input.length < 50 ){
        address.classList.add('border-red');
        address_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        address_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You must at least enter 50 characters';
        return false;
    }
    address.dataset['pass'] = '1';
    address.classList.add('border-green');
    address_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-success');
    address_status.innerHTML = '<i class="fas fa-check-square pr-1 pl-1"></i></i>Your address has been validated';
    return false;
   
}

textarea = document.getElementById("id_textarea");
textarea.addEventListener("input", validateTextArea);
function validateTextArea(e) {
    textarea.classList.remove('validation-success');
    input = e.target.value.replace(/^\s+/,"");
    textarea.value = input;
    var pattern = new RegExp(/[~`_@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/); //unacceptable chars
    if (pattern.test(input)) {
        textarea.value = input.replace(/[~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g, '');
        input = textarea.value;
    }  
    if (input.length > 300) {
        textarea.value = input.slice(0, 300);
    } 
}


images = document.getElementById("id_images");
images.addEventListener("change", validateImages);
images_status = document.getElementById("images_status");
id_images__handle = document.getElementById("id_images__handle");

__reverse = document.getElementById("__reverse");


function validateImages(){
    images.dataset['pass'] = '0';
    var allowedExtensions =/(\.jpg|\.jpeg|\.png|\.gif)$/i;
    if (images.files.length > 0) {
        for (var i = 0; i <= images.files.length - 1; i++) {
            var path = images.files[i].name;
            if (!allowedExtensions.exec(path)) { 
                images_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
                images_status.classList.remove("validation-success");
                images_status.innerHTML = '<i class="fas fa-exclamation-circle"></i> Only image files are allowed'; 
                images.value = ''; 
                id_images__handle.innerHTML = "";
                __reverse.style.display = "flex";
                return false; 
            }       
        }
        if (images.files.length <= 3 || images.files.length >= 9){
            images_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
            images_status.classList.remove('validation-success');
            images_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You must upload 4 to 8 pictures';
            images.value = '';
            id_images__handle.innerHTML = "";
            __reverse.style.display = "flex";
            return false;
        }
        var net_size = 0;
        for (var i = 0; i <= images.files.length - 1; i++) {
            net_size = net_size + images.files[i].size; 
        }
        if (net_size > 10000000){
            images_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
            images_status.classList.remove("validation-success");
            images_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>File Size must be lower than 10 MBs';
            images.value = '';
            id_images__handle.innerHTML = "";
            __reverse.style.display = "flex";
            return false;
        }    
        id_images__handle.innerHTML = '';
        __reverse.style.display = "none";
        for (var i = 0; i <= images.files.length - 1; i++) {
            (function(file) {     
                count = 1;           
                var reader = new FileReader();  
                reader.onload = function(e) {  
                    var div = document.createElement('div'); 
                    div.classList.add('img', 'animate__animated', 'animate__zoomIn');
                    var img = document.createElement('img'); 
                    img.src = e.target.result;
                    div.appendChild(img);
                    // if(count == 1){
                    //     var label = document.createElement('label');
                    //     label.classList.add('img-label');
                    //     label.innerHTML = "COVER"; 
                    //     div.appendChild(label);
                    // }
                    id_images__handle.appendChild(div);
                    count++;
                };

                reader.readAsDataURL(file);
            })(images.files[i]);
        }
        images.dataset['pass'] = '1';
        images_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-success');
        images_status.classList.remove("validation-error");
        images_status.innerHTML = '<i class="fas fa-check-circle pr-1"></i>Your upload has been approved';
        return true;
    }
    }

    sitting_capacity = document.getElementById("id_sitting__capacity");
    sitting_capacity.addEventListener("input", validateNumber);
    sitting_capacity.addEventListener("blur", validateNumberComplete);
    sitting__capacity_status = document.getElementById("sitting__capacity_status");

    function validateNumber(e){
        sitting_capacity.dataset['pass'] = '0';
        sitting_capacity.classList.remove('border-red', 'border-green');
        sitting__capacity_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
        sitting__capacity_status.innerHTML = '';
        input = e.target.value.trim();
        sitting_capacity.value = input;
        if(input.length > 4){
            sitting_capacity.classList.add("border-red");
                sitting__capacity_status.classList.add("animate__animated", "animate__bounceIn", "validation-error");
                sitting__capacity_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>Only four figuers are allowed';
                sitting_capacity.value = input.slice(0, 4);
                input = sitting_capacity.value;
        }
        var pattern = new RegExp(/[a-zA-Z~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/); //unacceptable chars
        if (pattern.test(input)) {
            sitting_capacity.classList.add("border-red");
            sitting__capacity_status.classList.add("animate__animated", "animate__bounceIn", "validation-error");
            sitting__capacity_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You can only use numbers';
            sitting_capacity.value = input.replace(/[a-zA-z~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g, '');
        }
    }

    function validateNumberComplete(e){
        sitting_capacity.classList.remove('border-red', 'border-green');
        sitting__capacity_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
        input = e.target.value;
        if( input == ""){
            sitting_capacity.classList.add('border-red');
            sitting__capacity_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
            sitting__capacity_status.innerHTML = "<i class=\"fas fa-exclamation-triangle pr-1\"></i>You can't leave a mandatory field empty";
            return false;
        }else{
            sitting_capacity.dataset['pass'] = '1';
            sitting_capacity.classList.add('border-green');
            sitting__capacity_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-success');
            sitting__capacity_status.innerHTML = '<i class="fas fa-check-circle pr-1"></i>Your price has been approved';
            return true;
        }
    }

parking_capacity = document.getElementById("id_parking__capacity");
parking_capacity.addEventListener("input", validateNumber2);
parking_capacity.addEventListener("blur", validateNumberComplete2);
parking__capacity_status = document.getElementById("parking__capacity_status");
function validateNumber2(e){
    parking_capacity.dataset['pass'] = '0';
    parking_capacity.classList.remove("border-green", "border-red");
    parking__capacity_status.classList.remove("validation-success", "validation-error", "animate__animated", "animate__bounceIn");
    parking__capacity_status.innerHTML = '';    
    input = e.target.value.trim();
    parking_capacity.value = input;

    if(input.length > 4){
        parking_capacity.classList.add("border-red");
        parking__capacity_status.classList.add("animate__animated", "animate__bounceIn", "validation-error");
        parking__capacity_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>Only four figuers are allowed';
        parking_capacity.value = input.slice(0, 4);
        input = parking_capacity.value;
    }
    var pattern = new RegExp(/[a-zA-Z~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/); 
    if (pattern.test(input)) {
        parking_capacity.classList.add("border-red");
        parking__capacity_status.classList.add("animate__animated", "animate__bounceIn", "validation-error");
        parking__capacity_status.innerHTML = '<i class="fas fa-exclamation-triangle pr-1"></i>You can only use numbers';
        parking_capacity.value = input.replace(/[a-zA-Z~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g, '');
    }
}


function validateNumberComplete2(e){
    parking_capacity.classList.remove('border-red', 'border-green');
    parking__capacity_status.classList.remove('animate__animated', 'animate__bounceIn', 'validation-error', 'validation-success');
    input = e.target.value;
    if( input == ""){
        parking_capacity.classList.add('border-red');
        parking__capacity_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-error');
        parking__capacity_status.innerHTML = "<i class=\"fas fa-exclamation-triangle pr-1\"></i>You can't leave a mandatory field empty";
        return false;
    }else{
        parking_capacity.dataset['pass'] = '1';
        parking_capacity.classList.add('border-green');
        parking__capacity_status.classList.add('animate__animated', 'animate__bounceIn', 'validation-success');
        parking__capacity_status.innerHTML = '<i class="fas fa-check-circle pr-1"></i>Your price has been approved';
        return true;
    }
}



function handleClick(myRadio) {
    if( myRadio.checked){
        var div = 
        '<div class="col-6 animate__animated animate__fadeIn" id="price_'+myRadio.id+'">'+
            '<input type="text" onblur="priceBlur(this)" oninput="priceInput(this)" placeholder="'+myRadio.value+'" name="'+myRadio.id+'_price" id="'+myRadio.id+'_price" data-pass="0">'+
            '<label class="" id="'+myRadio.id+'_price_status"></label>'+            
        '</div>'
        $("#price_row").append(div);
    }else{
        rm = "#price_"+myRadio.id;
        $(rm).remove();
   }
    
}
function priceInput(element){
    element.dataset['pass'] = '0';
    $("#"+element.id+"_status").removeClass("animate__anmated animate__bounceIn validation-error validation-success");
    $("#"+element.id+"_status").html('');
    element.classList.remove('border-red', 'border-green');
    input = element.value.trim();
    element.value = input;
    if( input.length > 6){
        $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
        $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Use 4 to 6 digits');
        element.classList.add('border-red');
        element.value = input.slice(0, 6);
        input = element.value;
    }
    var pattern = new RegExp(/[a-zA-z~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/); 
    if (pattern.test(input)) {
        $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
        $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Only numbers allowed');
        element.classList.add('border-red');
        element.value = input.replace(/[a-zA-z~`._@()!#$%\^&*+=\-\[\]\\';,/{}|\\":<>\?]/g, '');
        return false;
    }
    
}

function priceBlur(element){
    $("#"+element.id+"_status").removeClass("animate__anmated animate__bounceIn validation-error validation-success");
    $("#"+element.id+"_status").html('');
    element.classList.remove('border-red', 'border-green');
    input = element.value;
    if( input == ""){        
        $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
        $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Price is mandatory');
        element.classList.add('border-red');
        return true;
    }
    if( input.length > 3 && input.length < 7){   
        element.dataset['pass'] = '1';
        $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-success");
        $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Price validated');
        element.classList.add('border-green');
        return true;
    }else{
        $("#"+element.id+"_status").addClass("animate__anmated animate__bounceIn validation-error");
        $("#"+element.id+"_status").html('<i class="fas fa-exclamation-triangle pl-1 pr-1"></i>Use 4 to 6 digits');
        element.classList.add('border-red');
        return true;
    }
    
}

$('#form').submit(function(event) {
    event.preventDefault();
    let check = true;
    $("form#form :input").each(function(){
        var input = $(this); // This is the jquery object of the input, do what you will
        if(typeof $(this).data('pass') !== 'undefined' && $(this).attr('data-pass') == 0 ) {
            console.log($(this).attr('name')+" "+$(this).attr('data-pass'));
            $(this).focus();
            check = false;
            return false;
        }
    });   
    if(check){
        $(this).unbind('submit').submit();
    }else{
        return false;
    }
    
   })