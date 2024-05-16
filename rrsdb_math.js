
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
      
  }
  
  return coefficients;
}

function rrsdb_expand_q_pochhammer_product(terms, modulus, power_list)
{
  var coefficients = new Array(terms).fill(0);

  coefficients[0] = 1;

  for (var index = 0; index < modulus; ++index) {
    coefficients = rrsdb_product(terms, coefficients,
      rrsdb_expand_q_pochhammer(terms, modulus, power_list[index], index + 1));
  }

  return coefficients;
}

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

  var html = "1";

  if (terms > 1) {
    html += " + " +  (coefficients[1] == 1 ? "" : coefficients[1].toString()) + "q";

    for (var index = 2; index < terms; ++index) {
      html += " + " + (coefficients[index] == 1 ? "" : coefficients[index].toString()) + "q<sup>" + index.toString() + "</sup>";
    }
  }

  document.getElementById("series_expansion").innerHTML = html;
}
