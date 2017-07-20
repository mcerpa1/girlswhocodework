var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "dictionary.txt";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  var test = "work please";
    document.getElementById("results").innerHTML = test;
  var pw = document.getElementById("pw").value.toLowerCase();

for
(var i = 0; i < wordsList.length; i++){

  if(wordsList[i] == pw)
  {var resultsStr = "Weak Password";
  document.getElementById("results").innerHTML = resultsStr;
  break;}

  if(wordsList[i] != pw)
  {var resultsStr = "Password Valid";
  document.getElementById("results").innerHTML = resultsStr;}
}
