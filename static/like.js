$(document).ready(() => {
    $('.like-form').submit(function(e) {
        e.preventDefault();

        const post_id = $(this).attr('id');
        const like_btn = $(`.like-btn${ post_id }`);
        const trim = $.trim(like_btn.text());

        const likes = $(`.like-count${ post_id }`);
        const likes_count = parseInt(likes.text());
        let result;

        const like_color = '#0075FF';
        const unlike_color = '#FF9C00';

        const request_type = 'POST';
        const url = $(this).attr('action');
        const csrf_token = $('input[name=csrfmiddlewaretoken]').val();


        $.ajax({
            type: request_type,
            url: url,
            data: {
                'csrfmiddlewaretoken': csrf_token,
                'post_id': post_id
            },

            success: () => {
                if (trim === 'Unlike') {
                    like_btn.text('Like');
                    like_btn.css('background-color', like_color);
                    result = likes_count - 1;
                }
                else {
                    like_btn.text('Unlike');
                    like_btn.css('background-color', unlike_color);
                    result = likes_count + 1;
                }
                likes.text(result);
            },
            error: (response) => {
                console.log('error', response);
            }
        });
    });
});
