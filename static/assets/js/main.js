(function($) {
    'use strict';

    jQuery(document).ready(function($){
    

        var nav = document.querySelector('nav');
            window.addEventListener('scroll', function(){
                if(window.pageYOffset > 100){
                    nav.classList.add('bg-light', 'shadow','text-white');
                    
                }else{
                    nav.classList.remove('bg-light', 'shadow','text-white');
                }
            });

        // VIDEO CAROUSEL 
        $("#videocarousel").owlCarousel({
            loop:true,
            center:true,            
            margin:10,            
            autoplay:true,
            dots:true,
            responsiveClass:true,
            autoplayTimeout: 8500,
            smartSpeed: 450,        
            responsive:{
                0:{
                    items:1
                },
                700:{
                    items:1
                },
                900:{
                    items:1
                },
                1000:{
                    items:1
                }
            }
        });


         // SERVICES CAROUSEL 
        $("#services-carousel").owlCarousel({
            loop:true,
            center:false,                 
            autoplay:true,
            dots:true,
            responsiveBaseElement:'body',
            responsiveClass:true,
            autoplayTimeout: 8500,
            smartSpeed: 450,        
            responsive:{
                0:{
                    items:1
                },

                400:{
                    items:1,
                    
                },
                700:{
                    items:2
                },
                1000:{
                    items:3
                },
               
               
            }
        });

         // TESTIMONIAL CAROUSEL 
        $("#testimonial-carousel").owlCarousel({
            loop:true,
            center:false,            
            margin:50,            
            autoplay:true,
            dots:true,
            // responsiveBaseElement:'body',
            responsiveClass:true,
            autoplayTimeout: 8500,
            smartSpeed: 450,        
            responsive:{
                0:{
                    items:1
                },

                400:{
                    items:1,
                    
                },
                680:{
                    items:2
                },
                1000:{
                    items:3
                }
               
               
            }
        });


          //************ Magnific Popup

        $('.video-play').magnificPopup({
            type: 'video',
        });

        $('.zoom1').magnificPopup({
            type: 'iframe',
            gallery: {
                enabled: true
            },
            zoom: {
                enabled: true,
                duration: 300,
                opener: function(element) {
                    return element.find('img');
                }
            }
        });


        //*************** Isotope filter

        var $Container = $('#img-filter');
        if( $Container.length>0 ) {
            $Container.isotope({
                itemSelector: '.single-port',
                transitionDuration: '0.8s'
            });
            $(".img-filter").on("click", function (e){
                $(".img-filter.active").removeClass("active");
                $(this).addClass("active");
                var selector = $(this).attr('data-filter');
                $Container.isotope({
                    filter: selector
                });
                return false;
            });

            $(window).resize(function(){
                setTimeout(function(){
                    $Container.isotope();
                },1000);
            }).trigger('resize');
        }
    
        
        





        
    });


})(jQuery);
  
