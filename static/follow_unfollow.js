$(document).ready(function() {
    $('.follow-unfollow-form').submit(function(e) {
        e.preventDefault();

        const profile_pk = $(this).attr('id');
        const btn_text = $(`.btn${ profile_pk }`).text();
        const trim = $.trim(btn_text);
        const url = $(this).attr('action');

        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'profile_pk': profile_pk
            },

            success: function(response) {
                if (trim === 'Follow') $(`.btn${ profile_pk }`).text('Unfollow');
                else $(`.btn${ profile_pk }`).text('Follow');
            },
            error: function(response) {
                console.log('error', response);
            }
        });
    });
});
