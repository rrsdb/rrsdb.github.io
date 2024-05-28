function rrsdb_page_init() {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    var container = document.getElementById("sidebar");
    container.innerHTML = this.responseText;
    
    document.getElementById("modulus_search_button").addEventListener("click", function() {
      var search_text = document.getElementById("modulus_search_text").value.trim();

      if (search_text === "") return;

      window.location.href= "https://rrsdb.github.io/identities_by_product.htmll#mod" + search_text;
    });
  }

  xhttp.open("GET", "https://rrsdb.github.io/sidebar.html", true);
  xhttp.send();
}
