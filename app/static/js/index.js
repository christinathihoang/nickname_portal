// // event listener for side nav
// document.addEventListener('DOMContentLoaded', function() {
//   let elem = document.querySelector('.sidenav');
//   let options = {};
//   let instance = M.Sidenav.init(elem, options);
// });


// // for submission.html
// document.addEventListener('DOMContentLoaded', function() {
//   let elems = document.querySelector('.tabs');
//   let options = {swipeable: true};
//   let instance = M.Tabs.init(elems, options);
// })

let flipCardButtons = document.querySelectorAll('.flip-card');
// event listener to flip login/register card
for (let i = 0; i < flipCardButtons.length; i++) {
  flipCardButtons[i].addEventListener("click", function(e) {
    e.preventDefault();
    let card = document.querySelector('.card-body')
    document.querySelector('.card-body').classList.toggle('flipped');
  })
}