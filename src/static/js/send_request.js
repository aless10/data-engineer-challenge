$(document).on('submit', '#run-task', function(e){
      e.preventDefault();
      console.log({
              'events': $("#events").val(),
              'start-date': $("#start-date").val(),
              'end-date': $("#end-date").val(),
              'scheduler': $("#scheduler").val()
          });
      var url = "{{ url_for('task-view') }}";
      console.log(url);
      $.ajax({
          type:'POST',
          url: "/",
          data: {
              'events': $("#events").val(),
              'start_date': $("#start-date").val(),
              'end_date': $("#end-date").val(),
              'scheduler': $("#scheduler").val()
          },
          afterSend: function(){
            $(".animate-button").html('<button class="btn waves-effect waves-light animate-button" type="submit">RUN\
                                <i class="material-icons right">send</i>');
            },
      success:function(jsondata){
        $(".response").display();
        $("#task-result").html(jsondata);
    }

    });
    });