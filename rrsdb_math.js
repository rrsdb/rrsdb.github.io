
function rrsdb_product(terms, poly1, poly2)
{
  var coefficients = new Array(terms).fill(0);

  for (power = 0; power < terms; ++power) {
    for (index = 0; index <= power; ++index) {
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
  var html = "1";
  var terms = parseInt(document.getElementById("series_expansion_input_box").value);

  // TODO sanity check terms

  var coefficients = rrsdb_expand_q_pochhammer_product(terms, modulus, power_list);

  if (terms > 1) {
    html += " + " +  (coefficients[1] == 1 ? "" : coefficients[index].toString()) + "q";

    for (var index = 2; index < terms; ++index) {
      html += " + " + (coefficients[index] == 1 ? "" : coefficients[index].toString()) + "q<sup>" + index.toString() + "</sup>";
    }
  }

  document.getElementById("series_expansion").innerHTML = html;
}
