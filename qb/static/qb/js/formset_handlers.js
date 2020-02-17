(function($) {
    $(document).ready(function() {
      // Your JavaScript
       $('#id_lang').change(function() {
                 var lang_choice = this.value;
                 for(var i=0; i<4; i++){
                    id = '#id_choice_set-'+ i +'-lang';
                    $(id).val(lang_choice).prop('selected', 'selected').change();
                } 
        });
    });
})(django.jQuery);


