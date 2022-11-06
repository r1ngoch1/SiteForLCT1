$(document).ready(function(){
	$('.slider').slick({
		arrows:true,
		dots:true,
		slidesToShow:3,
		autoplay:true,
		speed:1000,
		autoplaySpeed:5000,
		responsive:[
			{
				breakpoint: 768,
				settings: {
					slidesToShow:2
				}
			},
			{
				breakpoint: 550,
				settings: {
					slidesToShow:1
				}
			}
		]
	});
$("a.MB1").on("click", function () {
    let href = $(this).attr("href");

    $("html, body").animate({
        scrollTop: $(href).offset().top
    });

    return false;
});
 $(window).scroll(function() {
 
if($(this).scrollTop() != 0) {
 
$('#toTop').fadeIn();
 
} else {
 
$('#toTop').fadeOut();
 
}
 
});
 
$('#toTop').click(function() {
 
$('body,html').animate({scrollTop:0},800);
 
});
  $('.popup-open').click(function() {
        $('.popup-black').fadeIn();
        $('html').addClass('no-scroll');
        return false;
    });
     
    $('.popup-close').click(function() {
        $(this).parents('.popup-black').fadeOut();
        $('html').removeClass('no-scroll');
        return false;
    });    
  
    $(document).keydown(function(e) {
        if (e.keyCode === 27) {
            e.stopPropagation();
            $('.popup-black').fadeOut();
            $('html').removeClass('no-scroll');
        }
    });
     
    $('.popup-black').click(function(e) {
        if ($(e.target).closest('.popup').length == 0) {
            $(this).fadeOut(); 
            $('html').removeClass('no-scroll');                
        }
    });
    $('.popup-open1').click(function() {
        $('.popup-black1').fadeIn();
        $('html').addClass('no-scroll');
        return false;
    });
     
    $('.popup-close1').click(function() {
        $(this).parents('.popup-black1').fadeOut();
        $('html').removeClass('no-scroll');
        return false;
    });    
  
    $(document).keydown(function(e) {
        if (e.keyCode === 27) {
            e.stopPropagation();
            $('.popup-black1').fadeOut();
            $('html').removeClass('no-scroll');
        }
    });
     
    $('.popup-black1').click(function(e) {
        if ($(e.target).closest('.popup1').length == 0) {
            $(this).fadeOut(); 
            $('html').removeClass('no-scroll');                
        }
    });
});
  

