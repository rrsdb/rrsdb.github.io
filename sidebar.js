function rrsdb_page_init() {

  /* Loads the sidebar. TODO make this cleaner somehow? */
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    var container = document.getElementById("sidebar");
    container.innerHTML = this.responseText;
    
    document.getElementById("modulus_search_button").addEventListener("click", function() {
      var search_text = document.getElementById("modulus_search_text").value.trim();

      if (search_text === "") return;

      window.location.href= "../identities-by-modulus.html#mod" + search_text;
    });
  }

  xhttp.open("GET", "../sidebar.html", true);
  xhttp.send();

  /* For touch screen devices. Toggles sidebar visibility. */
  document.getElementById("mobile_dropdown_menu_button").addEventListener("click", function() {
    document.getElementById("sidebar").style.display = (document.getElementById("sidebar").style.display == "block") ? "none" : "block";
  });
}