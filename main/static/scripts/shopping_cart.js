// Вывод скрытого меню регистрации аккаунта

document.getElementById('create-account').addEventListener('change', function () {
	var passwordForm = document.getElementById('password-form');
	var passwordConfirmForm = document.getElementById('password-confirm-form');
	passwordForm.style.display = this.checked ? 'block' : 'none';
	passwordConfirmForm.style.display = this.checked ? 'block' : 'none';
});

// Проверка пароля

var myRegInput = document.getElementById("reg-password");
var regLetter = document.getElementById("reg-letter");
var regCapital = document.getElementById("reg-capital");
var regNumber = document.getElementById("reg-number");
var regLength = document.getElementById("reg-length");

myRegInput.onfocus = function () {
	document.getElementById("reg-message").style.display = "flex";
}

myRegInput.onblur = function () {
	document.getElementById("reg-message").style.display = "none";
}

myRegInput.onkeyup = function () {
	var lowerCaseLetters = /[a-z]/g;
	if (myRegInput.value.match(lowerCaseLetters)) {
		regLetter.classList.remove("invalid");
		regLetter.classList.add("valid");
	} else {
		regLetter.classList.remove("valid");
		regLetter.classList.add("invalid");
	}

	var upperCaseLetters = /[A-Z]/g;
	if (myRegInput.value.match(upperCaseLetters)) {
		regCapital.classList.remove("invalid");
		regCapital.classList.add("valid");
	} else {
		regCapital.classList.remove("valid");
		regCapital.classList.add("invalid");
	}

	var numbers = /[0-9]/g;
	if (myRegInput.value.match(numbers)) {
		regNumber.classList.remove("invalid");
		regNumber.classList.add("valid");
	} else {
		regNumber.classList.remove("valid");
		regNumber.classList.add("invalid");
	}

	if (myRegInput.value.length >= 8) {
		regLength.classList.remove("invalid");
		regLength.classList.add("valid");
	} else {
		regLength.classList.remove("valid");
		regLength.classList.add("invalid");
	}
}