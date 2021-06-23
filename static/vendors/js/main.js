(function ($) {
"use strict";


// smooth scrolling
$('body').scrollspy({target: ".navbar", offset: 50});
//animation scroll js
var html_body = $('html, body');
$('nav a').on('click', function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        if (target.length) {
            html_body.animate({
                scrollTop: target.offset().top - 50
            }, 1500);
            return false;
        }
    }
});


//navbr collpse function clicking <a> tag and "x" icon and 3 bars icon for menu
$(".js-scroll-trigger").click(function(){
  $(".navbar-collapse").collapse('hide');
});

// resposive navbar "x" icon
$('.navbar-toggler').click(function() {
	$('.navbar-toggler-icon').toggleClass('hidden');
	$('#navbar-close').toggleClass('hidden');
});


// slick-slider
$('.new-arrival-slick').slick({
	dots: true,
	infinite: true,
	speed: 300,
	slidesToShow: 4,
	//prevArrow: '.slider_right',
	//nextArrow: '.slider_left',
	arrows:true,
	slidesToScroll: 1,
	responsive: [
		{
				breakpoint: 1025,
				settings: {
						slidesToShow: 4,
						slidesToScroll: 1,
						infinite: true,
						dots: true
				}
		},
		{
				breakpoint: 992,
				settings: {
						slidesToShow: 3,
						slidesToScroll: 1,
						infinite: true,
						dots: true,
				}
		},
		{
				breakpoint: 768,
				settings: {
						slidesToShow: 2,
						slidesToScroll: 1,
						infinite: true,
						dots: true,
				}
		},{
			breakpoint: 577,
			settings: {
					slidesToShow: 1,
					slidesToScroll: 1,infinite: true,
					dots: true,
			}
	}
		// You can unslick at a given breakpoint now by adding:
		// settings: "unslick"
		// instead of a settings object
]
});

 new WOW().init();


})(jQuery);

