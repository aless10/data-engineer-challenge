$(document).on('submit','#run-task', function(e){
      e.preventDefault();
      console.log({
              'events': $("#events").val();
              'start_date': $("#start_date").val(),
              'end_date': $("#end_date").val(),
              'scheduler': "celery"
          });
      $.ajax({
          type:'POST',
          url: "/",
          data: {
              'events': $("#events").val();
              'start_date': $("#start_date").val(),
              'end_date': $("#end_date").val(),
              'scheduler': $("#scheduler").val()
          },

      success:function(jsondata){
        $(".response").display();
        $("#task-result").html(jsondata);
    };

    })
    });