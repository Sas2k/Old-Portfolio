Submit_button = document.getElementById("Submit_Button");

let submit = () => {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let message = document.getElementById("message").value;
    var link = "mailto:sas8.communications@gmail.com"
             + "?subject=" + encodeURIComponent(`Message from ${name} | ${email}`)
             + "&body=" + encodeURIComponent(`${message}`);
    
    window.location.href = link;
};
