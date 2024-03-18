// открытие формы для регистрации

document.getElementById('openModalBtn').addEventListener('click', function () {
	document.getElementById('registrationModal').style.display = 'block';
	document.getElementById('registerForm').style.display = 'none';
	document.getElementById('loginForm').style.display = 'block';
});

document.getElementsByClassName('close')[0].addEventListener('click', function () {
	document.getElementById('registrationModal').style.display = 'none';
});

document.getElementsByClassName('close')[1].addEventListener('click', function () {
	document.getElementById('registrationModal').style.display = 'none';
});

document.getElementById('registerLink').addEventListener('click', function () {
	document.getElementById('loginForm').style.display = 'none';
	document.getElementById('registerForm').style.display = 'block';
});

document.getElementById('loginLink').addEventListener('click', function () {
	document.getElementById('registerForm').style.display = 'none';
	document.getElementById('loginForm').style.display = 'block';
});

// Проверка пароля

var myInput = document.getElementById("password");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

myInput.onfocus = function () {
	document.getElementById("message").style.display = "flex";
}

myInput.onblur = function () {
	document.getElementById("message").style.display = "none";
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

// Изменение цвета указателя текущей страницы

if (window.location.href.includes("home")) {
	document.getElementById("home-page").style.color = "violet";
} else if (window.location.href.includes("shopping_cart")) {
	document.getElementById("shopping-cart-page").style.color = "violet";
} else if (window.location.href.includes("blog")) {
	document.getElementById("blog-page").style.color = "violet";
} else if (window.location.href.includes("login")) {
	document.getElementById("openModalBtn").style.color = "violet";
}