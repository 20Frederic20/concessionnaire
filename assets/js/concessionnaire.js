$("#plus").click(
    function() {
        var value = parseInt($(".valeur").val(), 10) + 1;
        $(".valeur").val(value);
    }
)

$("#minus").click(
    function() {
        var value = parseInt($(".valeur").val(), 10) - 1;
        $(".valeur").val(value);
    }
)
$("#Username").hide();
let usernameError = true;
$("#username").keyup(function () {
    validateUsername();
});
function validateUsername() {
    let usernameValue = $("#username").val();
    if (usernameValue.length == "") {
        $("#username").addClass("is-invalid");
        $("#Username").html("Vous devez remplir cette case");
        usernameError = false;
        return false;
    } else if (usernameValue.length < 3 || usernameValue.length > 10) {
        $("#username").addClass("is-invalid");
        $("#Username").show();
        $("#Username").html("Ce champ doit contenir entre 3 et 10 caractères");
        usernameError = false;
        return false;
    } else {
        $("#Username").hide();
    }
}

/*Username validation*/
$("#submitbtn").click(function () {
    validateUsername();
    if ( usernameError == true ) {
        return true;
    } else {    
        return false;
    }
});

/*First name validation*/
$("#first_name").next("small").first().focus()
let firstNameError = true;
$("#first_name").keyup(function () {
    validateFirst();
});
function validateFirst() {
    let firstNameValue = $("#first_name").val();
    if (firstNameValue.length == "") {
        $("#first_name").addClass("is-invalid");
        let small = $("#first_name").next("small").first().focus().show()
        $("#first_name").next("small").first().focus().html("Vous devez remplir cette case");
        firstNameError = false;
        return false;
    } else if (firstNameValue.length < 4) {
        $("#first_name").addClass("is-invalid");
        $("#first_name").next("small").first().focus().show();
        $("#first_name").next("small").first().focus().html("Ce champ doit contenir entre 4 caractères");
        firstNameError = false;
        return false;
    } else {
        $("#first_name").next("small").first().focus().hide();
    }
}

/*Email validation*/
const email = document.getElementById("email");
email.addEventListener("blur", () => {
    let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
    let s = email.value;
    if (regex.test(s)) {
    email.classList.remove("is-invalid");
    emailError = true;
    } else {
    email.classList.add("is-invalid");
    emailError = false;
    }
});


/*Bouton de validation des informations entrés dans le formulaire*/
$("#submitbtn").click(function () {
    validateFirst();
    validateUsername();
    if ( firstNameError == true && usernameError == true ) {
        return true;
    } else {    
        return false;
    }
});