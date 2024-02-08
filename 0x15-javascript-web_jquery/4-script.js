$('#toggle_header').click(function() {
    var header = $('header');
    if (header.hasClass('green')) {
      header.removeClass('green');
      header.addClass('red');
    } else {
      header.removeClass('red');
      header.addClass('green');
    }
  });
