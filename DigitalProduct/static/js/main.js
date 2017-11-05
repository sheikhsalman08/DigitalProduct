$(document).ready(function(){

  $("#side-menu-singup").click(function(){
    $("#side-menu").animate({
  height: "toggle",
  opacity: "toggle",
});
    $("#side-menu-singup").hide();
    $("#side-menu-singup1").css({"display": "initial", });
  });

  $("#side-menu-singup1").click(function(){
         $("#side-menu").animate({
       height: "toggle",
       opacity: "toggle"
     });
         $("#side-menu-singup1").hide();
         $("#side-menu-singup").css({"display": "initial", });
       })

   $("#box-roww").hover(function(){
     $(".middle").css({"display": "initial", });
     $("i.fa.fa-cloud-download.fa-5x").css({"display": "initial"});
     $("#box-row").css({"position": "absolute", })
     console.log("hello");
   }, function(){
     $(".middle").css({"display": "none", });
      $("i.fa.fa-cloud-download.fa-5x").css({"display": "none"})
});


    $("#button-last").click(function(){
      $(".four-row").css({"display": "initial"})
    })

});
