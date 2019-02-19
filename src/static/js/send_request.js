$(document).on('submit', '#run-task', function(e){
      e.preventDefault();
      console.log({
              'events': $("#events").val(),
              'start-date': $("#start-date").val(),
              'end-date': $("#end-date").val(),
              'scheduler': $("#scheduler").val()
          });
      $.ajax({
          type:'POST',
          url: "/",
          data: {
              'events': $("#events").val(),
              'start_date': $("#start-date").val(),
              'end_date': $("#end-date").val(),
              'scheduler': $("#scheduler").val()
          },
        success:function(jsondata){
        $(".response").display();
        $("#animated").html('<button class="btn waves-effect waves-light animate-button" type="submit">RUN\
                                <i class="material-icons right">send</i>');
        $("#task-result").html(jsondata);
      }
    })

    });