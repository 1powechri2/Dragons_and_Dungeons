let signUpField = $('#signUp_field')
let loginField  = $('#login_field')
let links  = $('#links')
let login  = $('#login')
let signUp  = $('#sign_up')

$(document).ready(()=>{
  loginField.hide()
  signUpField.hide()
})

login.on('click', function () {
  links.toggle()
  loginField.toggle()
})
signUp.on('click', function () {
  links.toggle()
  signUpField.toggle()
})
