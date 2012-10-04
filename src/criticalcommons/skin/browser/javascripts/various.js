$("#form\\.usertype").live('change', function() {
   if ($("#form\\.usertype").val() == 'Basic User') {
        $("#formfield-form-user_title").hide();
        $("#formfield-form-institution").hide();
        $("#formfield-form-description").hide();
        $("#formfield-form-home_page").hide();
   }
   else {
        $("#formfield-form-user_title").show();
        $("#formfield-form-institution").show();
        $("#formfield-form-description").show();
        $("#formfield-form-home_page").show();
   }
});

$(document).ready(function() {
  $(window).keydown(function(event){
    if(event.keyCode == 13 && $(document.activeElement).attr('id') == "form-widgets-Title") {
      event.preventDefault();
      return false;
    }
  });
});

$(document).ready(function() {
    $("form.edit-form #form\\.usertype").parent().parent().parent().parent().hide()
    $("form.edit-form #form\\.accept").parent().parent().hide()
});
