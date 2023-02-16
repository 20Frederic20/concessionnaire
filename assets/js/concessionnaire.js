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

// Username validation
$("#Username").hide();
let usernameError = true;
$("#username").keyup(function() {
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

/*First name validation*/
$("#first_name").next("small").first().focus().hide()
let firstNameError = true;
$("#first_name").keyup(function() {
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
        $("#email").next("small").first().focus().html("Ce champ doit etre rempli avec un format d'email valide");
        emailError = false;
    }
});

// Password validation
$("#Password").hide();
let passwordError = true;
$("#password").keyup(function() {
    validatePassword();
});

function validatePassword() {
    let passwordValue = $("#password").val();
    if (passwordValue.length == "") {
        $("#password").addClass("is-invalid");
        $("#Password").show();
        $("#Password").html("Vous devez remplir cette case");
        passwordError = false;
        return false;
    } else if (passwordValue.length < 8) {
        $("#password").addClass("is-invalid");
        $("#Password").show();
        $("#Password").html("Ce champ doit contenir au moins 8 caractères");
        passwordError = false;
        return false;
    } else {
        $("#Password").hide();
    }
}

// Validate Confirm Password
$("#confirm_password").next("small").first().focus().hide();
let confirmPasswordError = true;
$("#confirm_password").keyup(function() {
    validateConfirmPassword();
});

function validateConfirmPassword() {
    let confirmPasswordValue = $("#confirm_password").val();
    let passwordValue = $("#password").val();
    if (passwordValue != confirmPasswordValue) {
        $("#confirm_password").addClass("is-invalid");
        $("#confirm_password").next("small").first().focus().show();
        $("#confirm_password").next("small").first().focus().html("Les mots de passe ne sont pas les memes");
        confirmPasswordError = false;
        return false;
    } else {
        $("#confirm_password").next("small").first().focus().hide();
    }
}


/*Bouton de validation des informations entrés dans le formulaire*/
$("#submitbtn").click(function() {
    validateFirst();
    validateUsername();
    if (firstNameError == true && usernameError == true && emailError == true && passwordError == true && confirmPasswordError == true) {
        return true;
    } else {
        return false;
    }
});