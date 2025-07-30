// get elements by ID (maybe change to querySelector later?)
const welcome = document.getElementById('welcome');
const signup = document.getElementById('signup');
const login = document.getElementById('login');

function showSignUp() {
  welcome.classList.add('hidden');
  login.classList.add('hidden');
  signup.classList.remove('hidden');
}

function showLogin() {
  welcome.classList.add('hidden');
  signup.classList.add('hidden');
  login.classList.remove('hidden');
}

function showWelcome() {
  signup.classList.add('hidden');
  login.classList.add('hidden');
  welcome.classList.remove('hidden');
}

// toggle pass visibility
function togglePassword(id, icon) {
  const input = document.getElementById(id);
  if (input.type === 'password') {
    input.type = 'text';
    icon.classList.remove('fa-eye');
    icon.classList.add('fa-eye-slash');
  } else {
    input.type = 'password';
    icon.classList.remove('fa-eye-slash');
    icon.classList.add('fa-eye');
  }
}

// Unused function I was testing
// function debugLog() {
//   console.log('debug');
// }