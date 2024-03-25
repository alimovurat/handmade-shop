// Проверка пароля

var myInput = document.getElementById("account-password");
var letter = document.getElementById("account-letter");
var capital = document.getElementById("account-capital");
var number = document.getElementById("account-number");
var length = document.getElementById("account-length");

myInput.onfocus = function () {
	document.getElementById("account-message").style.display = "flex";
}

myInput.onblur = function () {
	document.getElementById("account-message").style.display = "none";
}

myInput.onkeyup = function () {
	var lowerCaseLetters = /[a-z]/g;
	if (myInput.value.match(lowerCaseLetters)) {
		letter.classList.remove("invalid");
		letter.classList.add("valid");
	} else {
		letter.classList.remove("valid");
		letter.classList.add("invalid");
	}

	var upperCaseLetters = /[A-Z]/g;
	if (myInput.value.match(upperCaseLetters)) {
		capital.classList.remove("invalid");
		capital.classList.add("valid");
	} else {
		capital.classList.remove("valid");
		capital.classList.add("invalid");
	}

	var numbers = /[0-9]/g;
	if (myInput.value.match(numbers)) {
		number.classList.remove("invalid");
		number.classList.add("valid");
	} else {
		number.classList.remove("valid");
		number.classList.add("invalid");
	}

	if (myInput.value.length >= 8) {
		length.classList.remove("invalid");
		length.classList.add("valid");
	} else {
		length.classList.remove("valid");
		length.classList.add("invalid");
	}
}