(function(document) {
  var i = 0;
  // snip empty header rows since markdown can't
  var rows = document.querySelectorAll('tr');
  for(i=0; i<rows.length; i++) {
    var ths = rows[i].querySelectorAll('th');
    var rowlen = rows[i].children.length;
    if (ths.length > 0 && ths.length === rowlen) { rows[i].remove(); }
  }
})(document);
/* Lanyon & Poole are Copyright (c) 2014 Mark Otto. Adapted to Pelican 20141223 and extended a bit by @thomaswilley */
(function(document) {
  var toggle = document.querySelector('.sidebar-toggle');
  var sidebar = document.querySelector('#sidebar');
  var checkbox = document.querySelector('#sidebar-checkbox');
  document.addEventListener('click', function(e) {
    var target = e.target;
    if(!checkbox.checked
      || sidebar.contains(target)
      || (target === checkbox || target === toggle)) return;
    checkbox.checked = false;
  }, false);
})(document);
