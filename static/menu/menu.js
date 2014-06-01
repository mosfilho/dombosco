$(document).ready(function(){
   $(window).scroll(function () {
      if ($(this).scrollTop() > 150){
         $('#navbar-site').addClass('navbar-fixed-top');
      } else {
         $('#navbar-site').removeClass('navbar-fixed-top');
      }
   });
});
