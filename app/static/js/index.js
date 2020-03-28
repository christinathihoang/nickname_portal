// event listener for side nav
document.addEventListener('DOMContentLoaded', function() {
  let elem = document.querySelector('.sidenav');
  let instance = M.Sidenav.init(elem, {
  });
  // document.getElementById('menu-icon').addEventListener('click', function() {
  //   if (instance.isOpen) {
  //     instance.close();
  //   }
  //   else {
  //     instance.open()
  //   }
  // });
});

