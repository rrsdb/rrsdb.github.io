function rrsdb_page_init() {

  /* Loads the sidebar. TODO make this cleaner somehow? */
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    var container = document.getElementById("sidebar");
    container.innerHTML = this.responseText;
    
    document.getElementById("modulus_search_button").addEventListener("click", function() {
      var search_text = document.getElementById("modulus_search_text").value.trim();

      if (search_text === "") return;

      window.location.href = "https://rrsdb.github.io/identities_by_product.html#mod" + search_text;
    });
  }

  xhttp.open("GET", "https://rrsdb.github.io/sidebar.html", true);
  xhttp.send();

  /* For touch screen devices. Toggles sidebar visibility. */
  document.getElementById("mobile_dropdown_menu_button").addEventListener("click", function() {
    if (document.getElementById("sidebar").style.display == "block") {
      document.getElementById("sidebar").style.display = "none";
      document.getElementById("main").style.display = "block";
    } else {
      document.getElementById("sidebar").style.display = "block";
      document.getElementById("main").style.display = "none";
    } 
  });
}
