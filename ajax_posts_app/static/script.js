$('form').submit(function(e){
    e.preventDefault();
    $.ajax({
        url: '/create_post_ajax',
        method: 'post',
        data: $(this).serialize(),
        success: function(response){
            $('#posts').html(response)
        }
    });
    $(this).trigger('reset')
});