$(document).ready(function() {

      var setFields = function(that) {

        if (that.val() == -1) {
          $('.group-name').show();
        };

        if (that.val() == 1) {
          $('.aim-form .row').show();          
          $('.new-series-name').hide();
          $('.lesson-aim').hide();
          $('label[for=tip1]').text('Reinforcement idea 1');
          $('label[for=tip2]').text('Reinforcement idea 2');
        };

        if ((that.val() == 2) || (that.val() == 3)) {
          $('.aim-form .row').show();
          $('.new-series-name').hide();
          $('.lesson-aim').show();
          $('label[for=tip1]').text('Suggested question to ask child #1');
          $('label[for=tip2]').text('Suggested question to ask child #2');
        };
      }
     
      setFields($('select[name=groupName]'));


      if($('select[name=seriesName]').val() == 0) {
        $('.new-series-name').show();
      }; 

      $('select[name=groupName]').change(function() {
        setFields($(this));
      });


      /*

      var thisFunction = function(that) {
        console.log(this)
        $('.row').hide();
      }

      thisFunction($(this));

      */

      
      
      

       $('select[name=seriesName]').change(function() {
        if($(this).val() == 0) {
          $('.new-series-name').show();
        } else {
          $('.new-series-name').hide();
        }
      }); 

});