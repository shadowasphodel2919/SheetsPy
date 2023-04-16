document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("subCell").addEventListener("click", function() {
    console.log("Clicked");
    var col = document.getElementById("column").value;
    var row = document.getElementById("row").value;
    fetch("/get-data?column=" + col + "&row=" + row)
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        var dataDiv = document.getElementById("resCell");
        dataDiv.innerHTML = "Data: " + data;
      });
  });
});