$(document).ready(function(){
    const list = $('#add_item');
    list.click(function(){
      const item = $('<li>Item</li>');
      $('ul.my_list').append(item);
    });
  });
