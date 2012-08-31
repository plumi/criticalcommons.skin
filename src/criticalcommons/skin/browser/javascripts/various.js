$("#form\\.usertype").live('change', function() {
   if ($("#form\\.usertype").val() == 'Basic User') {
        $("#formfield-form-title").hide();
        $("#formfield-form-institution").hide();
        $("#formfield-form-biography").hide();
        $("#formfield-form-homePage").hide();
   }
   else {
        $("#formfield-form-title").show();
        $("#formfield-form-institution").show();
        $("#formfield-form-biography").show();
        $("#formfield-form-homePage").show();
   }
});
