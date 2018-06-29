$(document).ready(function() {
  $("body.template-publish_video textarea").attr("maxlength", 249);
  $("body.template-publish_video_scalar textarea").attr("maxlength", 249);
  $(window).keydown(function(event){
    if(event.keyCode == 13 && $(document.activeElement).attr('id') == "form-widgets-Title") {
      event.preventDefault();
      return false;
    }
  });

$('#formfield-form-usertype select').change(function() {
            var type = $(this).find('option:selected').val(), $fields = $('#formfield-form-user_title, #formfield-form-institution, #formfield-form-description, #formfield-form-home_page');
            if (type == 'Basic User') {
                $fields.hide();
            } else {
                $fields.slideDown();
            }
        })
        .change();
});
