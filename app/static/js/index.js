// event listener for side nav
document.addEventListener('DOMContentLoaded', function() {
  let elem = document.querySelector('.sidenav');
  let options = {};
  let instance = M.Sidenav.init(elem, options);
});


// for submission.html
document.addEventListener('DOMContentLoaded', function() {
  let elems = document.querySelector('.tabs');
  let options = {swipeable: true};
  let instance = M.Tabs.init(elems, options);
})

