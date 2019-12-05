function nameChange(name){
document.getElementById("formTitle").innerHTML(name);
}

firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
console.log(user);
  } else {
    // No user is signed in.
  }
});