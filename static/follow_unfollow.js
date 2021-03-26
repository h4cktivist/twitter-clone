$(document).ready(() => {
    $('.follow-unfollow-form').submit(function(e) {
        e.preventDefault();

        const profile_pk = $(this).attr('id');
        const btn = $(`.btn${ profile_pk }`);
        const btn_text = $.trim(btn.text());

        const url = $(this).attr('action');
        const request_type = 'POST';
        const csrf_token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            type: request_type,
            url: url,
            data: {
                'csrfmiddlewaretoken': csrf_token,
                'profile_pk': profile_pk
            },

            success: () => {
                (btn_text === 'Follow') ? btn.text('Unfollow') : btn.text('Follow');
            },
            error: (response) => {
                console.log('error', response);
            }
        });
    });
});
