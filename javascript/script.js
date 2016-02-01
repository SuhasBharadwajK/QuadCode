$(document).ready(function() {

  $(".light-button").click(function(event) {
    if ($(this).data('state') == 'off') {
      $(this).css({'background-color': $(this).css('border-left-color')});
      $(this).data('state', 'on');
    } else {
      $(this).css({'background-color': 'white'});
      $(this).data('state', 'off');
    }
    data = '{"type" : "light", "color" : "' + $(this).attr('value') + '", "state" : "' + $(this).data('state') + '"}';
    send(data);
  });

  $(".motor > div").click(function(event) {
    data = '{"type" : "motor", "num" : "' + $(this).parent().attr('id') + '", "operation" : "' + $(this).attr('class') + '"}';
    send(data);
  });

  $(".main-button").click(function(event) {
    if ($(this).attr('value') == 'up') {
      send('{"type" : "throttle", "direction" : "up"}');
    }
    else {
      send('{"type" : "throttle", "direction" : "down"}');
    }
  });

  $(".led-control > div").click(function(event) {
      $(".light-button").css({'background-color': 'white'});
	  data = '{"type" : "led", "action" : "' + $(this).attr('value') + '"}';
	  send(data);
  });

});

function send(dataToSend) {
  $.ajax({
    url:'http://192.168.0.103:8000',
    //url:'piserver.py',
    type: "POST",
    data: dataToSend,
	dataType: 'json',
    success: function(response) {
      console.log("Success! " + response['type']);
    },
    error: function (xhr, ajaxOptions, thrownError) {
      console.log(xhr.status);
      console.log(thrownError);
    }
  });
}
