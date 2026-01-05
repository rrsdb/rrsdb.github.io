function rrsdb_page_init() {
  document.getElementById("modulus_search_button").addEventListener("click", function() {
    var search_text = document.getElementById("modulus_search_text").value.trim();
    
    if (search_text === "") return;

    window.location.href = "https://rrsdb.github.io/identities_by_product.html#mod" + search_text;
  });

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

  /* In the specific case that a link is followed from the touch screen drop
   * down menu that only changes the #, hide the menu. */
  window.addEventListener("hashchange", function() {
    document.getElementById("sidebar").style.display = "none";
    document.getElementById("main").style.display = "block";
  });

  /* Search the document for the references. This can be done in a better way. */
  var split1 = document.body.textContent.split("[");

  for (var split2 in split1) {
    ref = split2.substring(0, split2.indexOf("]")

    document.getElementById("rrsdb_bib_" + ref).style.display = "block";
  }

document.body.textContent = part1[0] + part1[1].substring(part1[1].indexOf("\n"));
}

// Returns the expansion of poly1 * poly2.
function rrsdb_product(terms, poly1, poly2)
{
  var coefficients = new Array(terms).fill(0);

  for (var power = 0; power < terms; ++power) {
    for (var index = 0; index <= power; ++index) {
      coefficients[power] += poly1[index] * poly2[power - index];
    }
  }
  
  return coefficients;
}

// Returns the expansion of 1/(1-q^magnification).
function rrsdb_expand_geometric(terms, magnification)
{
  var coefficients = new Array(terms).fill(0);
  var index = 0;

  while (index < terms) {
      coefficients[index] = 1;
      index += magnification;
  }
  
  return coefficients;
}

// Returns the expansion of 1/(1-q^magnification)^power.
function rrsdb_expand_geometric_power(terms, power, magnification)
{
  var geometric_series = rrsdb_expand_geometric(terms, magnification);
  var coefficients = geometric_series;

  while (power != 1) {
      power -= 1;
      coefficients = rrsdb_product(terms, coefficients, geometric_series);
  }
  
  return coefficients;
}

// Returns the expansion of (1-q^magnification)^power.
function rrsdb_expand_binomial_power(terms, power, magnification)
{
  var factor = new Array(terms).fill(0);

  factor[0] = 1;

  if (magnification >= terms) {
    return factor;
  } else {
    factor[magnification] = -1;
    
    var coefficients = factor;

    while (power != 1) {
      coefficients = rrsdb_product(terms, coefficients, factor);
      power -= 1;
    }

    return coefficients;
  }
}

// Returns the expansion of (q^offset; q^modulus)^power.
function rrsdb_expand_q_pochhammer(terms, modulus, power, offset)
{
  var coefficients = new Array(terms).fill(0);

  coefficients[0] = 1;

  if (power == 0) return coefficients;

  if (power < 0) {
    var index = offset;

    while (index < terms) {
      coefficients = rrsdb_product(terms, coefficients,
        rrsdb_expand_geometric_power(terms, -power, index));
      index += modulus;
    }
  } else {
    var index = offset;
    
    while (index < terms) {
      coefficients = rrsdb_product(terms, coefficients,
        rrsdb_expand_binomial_power(terms, power, index));
      index += modulus;
    }
  }

  return coefficients;
}

// Returns the expansion of
// (q; q^modulus)^(-power_list[0]) * ... * (q^(modulus - 1); q^modulus)^(-power_list[modulus - 1]).
function rrsdb_expand_q_pochhammer_product(terms, modulus, power_list)
{
  var coefficients = new Array(terms).fill(0);

  coefficients[0] = 1;

  for (var index = 0; index < modulus; ++index) {
    coefficients = rrsdb_product(terms, coefficients,
      rrsdb_expand_q_pochhammer(terms, modulus, -power_list[index], index + 1));
  }

  return coefficients;
}

// Computes the series expansion of a single product signature and writes
// it to the page in a human readable format.
function rrsdb_series_expand_simple(modulus, power_list)
{
  var terms_text_input = document.getElementById("series_expansion_input_box").value.trim();

  // Check that the input is a non-negative integer
  for (var index = 0; index < terms_text_input.length; ++index) {
    if (!("0123456789".includes(terms_text_input[index]))) {
      document.getElementById("series_expansion").innerHTML =
        "<span style='color: red;'>Please enter a positive integer</span>";
      return;
    }
  }

  var terms = parseInt(terms_text_input);
  var coefficients = rrsdb_expand_q_pochhammer_product(terms, modulus, power_list);

  if (terms == 0) {
    document.getElementById("series_expansion").innerHTML = "0";
    return;
  }

  var html = "\\( 1";

  if (terms > 1) {
    for (var index = 1; index < terms; ++index) {
      if (coefficients[index] != 0) {
        html += (coefficients[index] > 0 ? " + " : " - ")
          + (Math.abs(coefficients[index]) == 1 ? "" : Math.abs(coefficients[index]).toString())
          + "q^{" + (index == 1 ? "" : index.toString()) + "}";
      }
    }
  }

  html += "\\)"

  const output = document.getElementById("series_expansion");
  MathJax.typesetClear([output]);
  output.innerHTML = html;
  MathJax.typesetPromise([output])
}
