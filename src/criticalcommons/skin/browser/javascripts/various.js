$(document).ready(function() {
  $(window).keydown(function(event){
    if(event.keyCode == 13 && $(document.activeElement).attr('id') == "form-widgets-Title") {
      event.preventDefault();
      return false;
    }
  });
});
