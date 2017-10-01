$(document).ready(function () {
    new WOW({mobile: false}).init();

    var url = window.location.href, idx = url.indexOf("#")
    var hash = idx != -1 ? url.substring(idx + 1) : "";
    if (hash == "success") {
        $('.popup-overlay').fadeIn();
        $('.success-popup').fadeIn();
    }


    var fixed_header = $('.header');

    $(window).on("scroll", function (e) {
        if ($(document).scrollTop() > 0) {
            fixed_header.addClass("scrolled-header");
        } else {
            fixed_header.removeClass("scrolled-header");
        }

    });

    $('.homepage-header').find('.scroll-down-landpage img').click(function () {
        var header = $('.homepage-header').height();
        $('html, body').animate({
            scrollTop: header
        }, 900);
    });

    $('.static-header').find('.scroll-down-arrow img').click(function () {
        var header = $('.static-header').height();
        $('html, body').animate({
            scrollTop: header
        }, 900);
    });

    $('.book-a-meeting-button').click(function () {
        $('#popup1').fadeIn();
    });

    $('.close').click(function () {
        $('#popup1').fadeOut();
        $('#success').fadeOut();
    });

    $(document).keydown(function (e) {
        //ESC button pressed
        if (e.keyCode == 27) {
            $('#popup1').fadeOut();
            $('#success').fadeOut();
        }
    });

    $('.video-play').click(function () {
        $(this).hide();
        $('.video-pause').show();
        $(".cover-video").get(0).play();
    })

    $('.video-pause').click(function () {
        $(this).hide();
        $('.video-play').show();
        $(".cover-video").get(0).pause();
    });

    $('.client-box').click(function () {
        var clinetNumber = $(this).data('client-number');
        $('html, body').animate({
            scrollTop: $("#clinet-number-" + clinetNumber).offset().top - 60
        }, 1000);
    })

    $('a[href^="http"]').attr('target', '_blank');
});
