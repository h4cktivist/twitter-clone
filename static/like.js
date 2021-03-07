$(document).ready(function() {
    $('.like-form').submit(function(e) {
        e.preventDefault();
        
        const post_id = $(this).attr('id');
        const like_text = $(`.like-btn${ post_id }`).text();
        const trim = $.trim(like_text);

        const likes = $(`.like-count${ post_id }`).text();
        const count_trim = parseInt(likes);

        const url = $(this).attr('action');
        let result;
        
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'post_id': post_id
            },

            success: function(response) {
                if (trim === 'Unlike') {
                    $(`.like-btn${ post_id }`).text('Like');
                    result = count_trim - 1;
                }
                else {
                    $(`.like-btn${ post_id }`).text('Unlike');
                    result = count_trim + 1;
                }
                $(`.like-count${ post_id }`).text(result);
            },
            error: function(response) {
                console.log('error', response);
            }
        });
    });
});
