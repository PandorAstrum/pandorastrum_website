
//map component starts -------------------------------------------
var forEach = function(array, callback, scope) {
  for (var i = 0; i < array.length; i++) {
    callback.call(scope, i, array[i]); // passes back stuff we need
  }
};

var randomIntFromInterval = function(min,max) {
  return Math.floor(Math.random()*(max-min+1)+min);
}

var $mapPins = document.querySelectorAll('#Map-shape g');

// Setup timelines attached to each map pin
forEach($mapPins, function(index, value) {
  // Group opacity timeline
  value.groupTimeline = new TimelineMax({
    paused: true
  });

  value.groupTimeline
  .to(value, 0.25, {
    opacity: 0
  });

  // Pulse animation
  var pinTimeline = new TimelineMax({
    repeat: -1,
    delay: randomIntFromInterval(1,3),
    repeatDelay: randomIntFromInterval(0, 1)
  });

  pinTimeline.
  to(value.querySelector('.Pin-back'), 3, {
    scale: 50,
    transformOrigin: 'center center',
    opacity: 0
  });
});

forEach(document.querySelectorAll('.js-Location-nav [data-location]'), function(index, value) {

   value.addEventListener('mouseenter', function(e) {
     var location = e.target.getAttribute('data-location');

     // Hide other map pins
     forEach($mapPins, function(index, value) {
       if (value.getAttribute('data-location') !== location) {
         value.groupTimeline.play();
       }
     });
   }, false);

  value.addEventListener('mouseleave', function(e) {
    // Reverse all hidden map pins
    forEach($mapPins, function(index, value) {
       value.groupTimeline.reverse();
    });

  }, false);
});
//map component ends ---------------------------------------------


// contact form component starts ---------------------------------
var formContainer = $('#form-container');

bindFormClick();
//Opening the form
function bindFormClick(){
  $(formContainer).on('click', function(e) {
    e.preventDefault();
    toggleForm();
    //Ensure container doesn't togleForm when open
    $(this).off();
  });
}

//Closing the form
$('#form-close, .form-overlay').click(function(e) {
  e.stopPropagation();
  e.preventDefault();
  toggleForm();
  bindFormClick();
});

function toggleForm(){
  $(formContainer).toggleClass('expand');
  $(formContainer).children().toggleClass('expand');
  $('body').toggleClass('show-form-overlay');
  $('.form-submitted').removeClass('form-submitted');
}

//Form validation
$('form').submit(function() {
  var form = $(this);
  form.find('.form-error').removeClass('form-error');
  var formError = false;

  form.find('.input').each(function() {
    if ($(this).val() == '') {
      $(this).addClass('form-error');
      $(this).select();
      formError = true;
      return false;
    }
    else if ($(this).hasClass('email') && !isValidEmail($(this).val())) {
      $(this).addClass('form-error');
      $(this).select();
      formError = true;
      return false;
    }
  });

  if (!formError) {
    $('body').addClass('form-submitted');
    $('#form-head').addClass('form-submitted');
    setTimeout(function(){
      $(form).trigger("reset");
    }, 1000);
  }
  return false;
});

function isValidEmail(email) {
    var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
    return pattern.test(email);
};
//contact form component ends -------------------------------------
/**
 * Created by Ana Ash on 8/16/2017.
 */
