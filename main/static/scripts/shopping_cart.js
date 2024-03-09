// Вывод скрытого меню регистрации аккаунта

document.getElementById('create-account').addEventListener('change', function () {
	var passwordForm = document.getElementById('password-form');
	var passwordConfirmForm = document.getElementById('password-confirm-form');
	passwordForm.style.display = this.checked ? 'block' : 'none';
	passwordConfirmForm.style.display = this.checked ? 'block' : 'none';
});