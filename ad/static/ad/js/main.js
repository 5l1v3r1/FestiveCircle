$(".dropdown-menu li").click(function(){
    $(this).parents(".dropdown").find('.btn').html($(this).text() + ' <span class="pull-left"><i class="fas fa-caret-down"></i></span>');
    $(this).parents(".dropdown").find('.btn').val($(this).data('value'));
  });

  