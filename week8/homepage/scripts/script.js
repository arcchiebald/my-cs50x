document.addEventListener("DOMContentLoaded", function () {
  let btn = document.getElementById("button-addon2");
  let input = document.getElementById("userName").value;
  btn.addEventListener("click", function () {
    input = document.getElementById("userName").value;
    document.getElementById("grt").innerHTML =
      "Glad to see you, " + input + "!";
  });

  nameInp = document.getElementById("nameInp");
  btn.onclick = function () {
    if (nameInp.style.display !== "none") {
      nameInp.style.display = "none";
    }
  };
});
