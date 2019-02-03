$(document).on('submit','#myFilterPermission', function(e){
      e.preventDefault();
      var masterid_inputs = $(".masterid_input:checked");
      var agentid_inputs = $(".agentid_input:checked");
      var extension_inputs = $(".extension_input:checked");

      var masterid_filter = [];
      var agentid_filter = [];
      var extension_filter = [];

      for (i=0; i<masterid_inputs.length; i++ ) {
        masterid_filter.push(masterid_inputs[i].name);
      }
      for (i=0; i<agentid_inputs.length; i++ ) {
        agentid_filter.push(agentid_inputs[i].name);
      }
      for (i=0; i<extension_inputs.length; i++ ) {
        extension_filter.push(extension_inputs[i].name);
      }
      myUrl = url;
      $.ajax({
          beforeSend: function(){
            if ( masterid_filter.length == 0 || agentid_filter.length == 0 || extension_filter.length == 0) {
              $("#permission-span").html('Il filtro non può essere vuoto');
              $("#modalPermissionError").modal("open");
              return false;
            }
          },
          type:'POST',
          url: myUrl,
          data: {
              'masterid_list':masterid_filter,
              'agentid_list':agentid_filter,
              'extension_list':extension_filter
          },

      success:function(jsondata){
        result = jsondata[0];
        label = jsondata[2];
        if (label) {
          $('#date-filter')[0].innerHTML = getInfoMessages('Filtro: ' + label);
          }
        // $('#permission-filter')[0].innerHTML = "";
        // if ({{ session['master_id_list']|length }} > 1) {
        //   $('#permission-filter')[0].innerHTML = getInfoMessages('Filtro per Masterid: ' + jsondata[1]['master_id_filter']);
        // }
        // if ({{ session['agent_id_list']|length }} > 1) {
        //   $('#permission-filter')[0].innerHTML += getInfoMessages('Filtro per AgentId: ' + jsondata[1]['agent_id_filter']);
        //   }
        // if ({{ session['extension_list']|length }} > 1) {
        //   $('#permission-filter')[0].innerHTML += getInfoMessages('Filtro per Extension: ' + jsondata[1]['extension_filter']);
        // }
        $("#chart-div").hide();
        if (chart !=null){
            chart.destroy();
          }
        if (typeof num_data_visualized !== 'undefined') {
          createChart(result, num_data_visualized);
        }
        else {
          createChart(result);
        }
        if (typeof t != "undefined") {
          t.clear().draw();
          createTable(result);
          }

        }
    });

    });