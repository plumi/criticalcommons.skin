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
