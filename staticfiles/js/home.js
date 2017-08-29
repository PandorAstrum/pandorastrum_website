//clock timer starts ---------------------
function updateTimer(deadline) {
	var time = deadline - new Date(); //return differens between now and deadline
	return {
		'days': Math.floor(time/(1000*60*60*24)),
		'hours': Math.floor((time/(1000*60*60))%24),
		'minutes': Math.floor((time/1000/60)%60),
		'seconds': Math.floor((time/1000)%60),
		'total': time
	};
}

function animateClock(span) {
	span.className = "turn";
	setTimeout(function(){
		span.className = "";
	}, 700);
}

function startTimer(id, deadline) {
	var timerInterval = setInterval(function(){
		var clock = document.getElementById(id); //store element
		var timer = updateTimer(deadline);

		clock.innerHTML = '<span>' + timer.days + '</span>'  //put in clock element our time
						+ '<span>' + timer.hours + '</span>'
						+ '<span>' + timer.minutes + '</span>'
						+ '<span>' + timer.seconds + '</span>';

		var spans = clock.getElementsByTagName("span");
		animateClock(spans[3]);
		if (timer.seconds == 59) animateClock(spans[2]);
		if (timer.minutes == 59 && timer.seconds == 59) animateClock(spans[1]);
		if (timer.hours == 23 && timer.minutes == 59 && timer.seconds == 59) animateClock(spans[0]);

	if (timer.total < 1) {
		clearInterval(timerInterval);
		clock.innerHTML = '<span>0</span><span>0</span><span>0</span><span>0</span>';
	}

	}, 1000);
}


//clock timer ends -----------------------
/**
 * Created by Ana Ash on 8/28/2017.
 */
//get it btn and side bar -------------------------------------------------------
var $sliderComponent = document.querySelector(".slider-component");
var $container = $(".slider-component__credits");
var $getit1 = $("#getit1");
var $getit2 = $("#getit2");
var $getit3 = $("#getit3");
var $getit4 = $("#getit4");
var $close_btn = $(".slider-component__credits");

[].slice.call(document.querySelectorAll(".pa-slide__action-btn")).forEach(function($btn) {
    $btn.addEventListener("click", function() {
        $sliderComponent.classList.toggle("credits-active");
        var newDiv = $(this).attr("href");
        var divElem = $(''+newDiv).html();
        $container.html(divElem);
    });
});
$close_btn.on("click", function(){
    $sliderComponent.classList.remove("credits-active");
});

$getit1.hide();
$getit2.hide();
$getit3.hide();
$getit4.hide();

// slider -----------------------------------------------------------------------
(function() {
    var $$ = function(selector, context) {
    var context = context || document;
    var elements = context.querySelectorAll(selector);
    return [].slice.call(elements);
  };

  function _fncSliderInit($slider, options) {
    var prefix = ".pa-";
    var $slider = $slider;
    var $slidesCont = $slider.querySelector(prefix + "slider__slides");
    var $slides = $$(prefix + "slide", $slider);
    var $controls = $$(prefix + "nav__control", $slider);
    var $controlsBgs = $$(prefix + "nav__bg", $slider);
    var $progressAS = $$(prefix + "nav__control-progress", $slider);
    var numOfSlides = $slides.length;
    var curSlide = 1;
    var sliding = false;
    var slidingAT = +parseFloat(getComputedStyle($slidesCont)["transition-duration"]) * 1000;
    var slidingDelay = +parseFloat(getComputedStyle($slidesCont)["transition-delay"]) * 1000;
    var autoSlidingActive = false;
    var autoSlidingTO;
    var autoSlidingDelay = 5000; // default autosliding delay value
    var autoSlidingBlocked = false;
    var $activeSlide;
    var $activeControlsBg;
    var $prevControl;

    function setIDs() {
      $slides.forEach(function($slide, index) {
        $slide.classList.add("pa-slide-" + (index + 1));
      });

      $controls.forEach(function($control, index) {
        $control.setAttribute("data-slide", index + 1);
        $control.classList.add("pa-nav__control-" + (index + 1));
      });

      $controlsBgs.forEach(function($bg, index) {
        $bg.classList.add("pa-nav__bg-" + (index + 1));
      });
    };

    setIDs();

    function afterSlidingHandler() {
      $slider.querySelector(".m--previous-slide").classList.remove("m--active-slide", "m--previous-slide");
      $slider.querySelector(".m--previous-nav-bg").classList.remove("m--active-nav-bg", "m--previous-nav-bg");

      $activeSlide.classList.remove("m--before-sliding");
      $activeControlsBg.classList.remove("m--nav-bg-before");
      $prevControl.classList.remove("m--prev-control");
      $prevControl.classList.add("m--reset-progress");
      var triggerLayout = $prevControl.offsetTop;
      $prevControl.classList.remove("m--reset-progress");

      sliding = false;
      var layoutTrigger = $slider.offsetTop;

      if (autoSlidingActive && !autoSlidingBlocked) {
        setAutoslidingTO();
      }
    };

    function performSliding(slideID) {
      if (sliding) return;
      sliding = true;
      window.clearTimeout(autoSlidingTO);
      curSlide = slideID;

      $prevControl = $slider.querySelector(".m--active-control");
      $prevControl.classList.remove("m--active-control");
      $prevControl.classList.add("m--prev-control");
      $slider.querySelector(prefix + "nav__control-" + slideID).classList.add("m--active-control");

      $activeSlide = $slider.querySelector(prefix + "slide-" + slideID);
      $activeControlsBg = $slider.querySelector(prefix + "nav__bg-" + slideID);

      $slider.querySelector(".m--active-slide").classList.add("m--previous-slide");
      $slider.querySelector(".m--active-nav-bg").classList.add("m--previous-nav-bg");

      $activeSlide.classList.add("m--before-sliding");
      $activeControlsBg.classList.add("m--nav-bg-before");

      var layoutTrigger = $activeSlide.offsetTop;

      $activeSlide.classList.add("m--active-slide");
      $activeControlsBg.classList.add("m--active-nav-bg");

      setTimeout(afterSlidingHandler, slidingAT + slidingDelay);
    };

    function controlClickHandler() {
      if (sliding) return;
      if (this.classList.contains("m--active-control")) return;
      if (options.blockASafterClick) {
        autoSlidingBlocked = true;
        $slider.classList.add("m--autosliding-blocked");
      }

      var slideID = +this.getAttribute("data-slide");

      performSliding(slideID);
    };

    $controls.forEach(function($control) {
      $control.addEventListener("click", controlClickHandler);
    });

    function setAutoslidingTO() {
      window.clearTimeout(autoSlidingTO);
      var delay = +options.autoSlidingDelay || autoSlidingDelay;
      curSlide++;
      if (curSlide > numOfSlides) curSlide = 1;

      autoSlidingTO = setTimeout(function() {
        performSliding(curSlide);
      }, delay);
    };

    if (options.autoSliding || +options.autoSlidingDelay > 0) {
      if (options.autoSliding === false) return;

      autoSlidingActive = true;
      setAutoslidingTO();

      $slider.classList.add("m--with-autosliding");
      var triggerLayout = $slider.offsetTop;

      var delay = +options.autoSlidingDelay || autoSlidingDelay;
      delay += slidingDelay + slidingAT;

      $progressAS.forEach(function($progress) {
        $progress.style.transition = "transform " + (delay / 1000) + "s";
      });
    }

    $slider.querySelector(".pa-nav__control:first-child").classList.add("m--active-control");

  };

  var fncSlider = function(sliderSelector, options) {
    var $sliders = $$(sliderSelector);

    $sliders.forEach(function($slider) {
      _fncSliderInit($slider, options);
    });
  };

  window.fncSlider = fncSlider;
}());
fncSlider(".main-slider", {autoSlidingDelay: 4000});

// default open accordion
$("#accordion1").find('.panel-collapse:first').addClass("in");
function close_accordion_section() {
    $('.accordion .accordion-section-title').removeClass('active');
    $('.accordion .accordion-section-content').slideUp(300).removeClass('open');
}
$('.accordion-section-title').click(function(e) {
    // Grab current anchor value
    var currentAttrValue = $(this).attr('href');
    if($(e.target).is('.active')) {
        close_accordion_section();
    }else {
        close_accordion_section();
        // Add active class to section title
        $(this).addClass('active');
        // Open up the hidden content panel
        $('.accordion ' + currentAttrValue).slideDown(300).addClass('open');
    }
    e.preventDefault();
});
