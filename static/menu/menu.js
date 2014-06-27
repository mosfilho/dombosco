$(document).ready(function(){
   $(window).scroll(function () {
      if ($(this).scrollTop() > 150){
         $('.navbar-custom').addClass('navbar-fixed-top');
      } else {
         $('.navbar-custom').removeClass('navbar-fixed-top');
      }
   });
});
