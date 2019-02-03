$(document).ready(function(){
    $('.collapsible').collapsible();
    Materialize.updateTextFields();
    $('select').material_select();
    $('#dataTable').DataTable();
  });

 $(".button-collapse").sideNav({
  closeOnClick: true // Close the sidebar on <a> click
 });

 $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 5, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false, // Close upon selecting a date,
    format: 'yyyy-mm-dd',
    // formatSubmit: undefined,
  });