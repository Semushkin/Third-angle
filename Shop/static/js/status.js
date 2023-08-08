const dropdown = document.getElementById("id_status");

dropdown.addEventListener("change", function() {

  document.getElementById("status_form").submit();
});