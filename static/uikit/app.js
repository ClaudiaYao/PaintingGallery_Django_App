
"use strict"

// Invoke Functions Call on Document Loaded
// document.addEventListener('DOMContentLoaded', function () {
//   hljs.highlightAll();
// });

console.log("start the js");
let alertWrapper = document.querySelector(".alert");
let alertClose = document.querySelector(".alert__close");

if (alertWrapper) {
console.log("Alert wrapper clicked!");
addEventListener("click", () => {
console.log("enter into");
  alertWrapper.style.display = 'none';
}
)
};

