// Default way of doing things
// first display
let Surname_First_nmae = "SAMUEL EFFIONG";

let Height = 18;

let country = "NIGERIA";

// Object way7 of doing things
const myScreenOutput = document.getElementById("Display");
const myScreenOutput2 = document.getElementById("Display");

const Mydata = {
  FirstName: "SAMUEL ",
  MiddleName: "EFFIONG",
  lastName: "JACOB",
  HeightOriginal: 18,
  countryOriginal: "NIGERIA",
};

// SECOND OBJECT DISPLAY

myScreenOutput2.innerHTML =
  "<h2>" +
  "First Name: " +
  Mydata.FirstName +
  "<br> " +
  "Middle Name: " +
  Mydata.MiddleName +
  " <br>" +
  " Last Name: " +
  Mydata.lastName +
  "<br> " +
  "Height: " +
  Mydata.HeightOriginal +
  "<br> " +
  "Country: " +
  Mydata.countryOriginal;
("</h2>");

// FOR ALERT

console.log(Surname_First_nmae);
console.log(Height);
console.log(country);
console.log(Mydata);

alert("welcome to my Data ");
