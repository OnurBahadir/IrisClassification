function validateForm() {
  let x = document.forms["irisForm"]["sLen"].value;
  let y = document.forms["irisForm"]["pLen"].value;
  let z = document.forms["irisForm"]["pWid"].value;
  let k = document.forms["irisForm"]["sWid"].value;
  if (x == "" || y=="" || z=="" || k=="") {
        alert("Data must be filled out correctly");
        return false;
  }
}