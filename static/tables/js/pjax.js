$(function () {
    if ($.support.pjax) {
        $('#pjax-container').pjax('a[data-pjax]', '#pjax-container', {fragment: ('#pjax-container'), timeout: 8000});

        $(document).on('pjax:start', function () {
            NProgress.start();
        });
        $(document).on('pjax:end', function () {
            NProgress.done();
        });
    }
});