$(document).ready(function(){
    $("#Features").on('click', function(){
      var yr = $(this).val();
      $("table tbody tr").each(function(index){
        var val = $(":nth-child(2)", this).html();
        console.log(val);
        if(val === yr) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    })
  ;
  
    $("#year").trigger('click');
  });