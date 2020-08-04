    Filevalidation = () => { 
        var fileInput =  document.getElementById('selectedFile'); 
            var filePath = fileInput.value; 
            var button = document.getElementById("upload-button"); 
            var allowedExtensions =/(\.jpg|\.jpeg|\.png|\.gif)$/i; 
            var label = document.getElementById('file_label');
            if (!allowedExtensions.exec(filePath)) { 
                label.innerHTML = '<i class="fas fa-exclamation-circle"></i> Please upload an image file'; 
                label.classList.add("error-text");
                label.classList.remove("success-text");
                fileInput.value = ''; 
                button.classList.add("upload-button2");
                button.classList.remove("upload-button3");
                button.classList.remove("upload-button");
                return false; 
            }  
            else  { 
                const size = fileInput.files[0].size / 1024 / 1024; 
                if (size > 10){
                    label.innerHTML = '<i class="fas fa-exclamation-circle"></i> File size must be less than 10 MBs'; 
                    label.classList.add("error-text");
                    label.classList.remove("success-text");
                    fileInput.value = ''; 
                    button.classList.add("upload-button2");
                    button.classList.remove("upload-button3");
                    button.classList.remove("upload-button");
                    return false; 
                }
                button.classList.add("upload-button3");
                button.classList.remove("upload-button2"); 
                button.classList.remove("upload-button");
                label.innerHTML = '<i class="fas fa-check-circle"></i> Upload is successful';
                label.classList.add("success-text");
                label.classList.remove("error-text");
                if (fileInput.files && fileInput.files[0]) { 
                    var reader = new FileReader(); 
                    reader.onload = function(e) { 
                        console.log("Event");
                        console.log(e);
                        document.getElementById("avatar").src = e.target.result;  
                    }; 
                    console.log("Type");
                    console.log(fileInput.files[0]); 
                    reader.readAsDataURL(fileInput.files[0]); 
                } 
            } 
        } 