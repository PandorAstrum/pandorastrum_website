
var topBorderWidth = $('.topBorder').outerWidth();
var topBorderHeight = $('.topBorder').outerHeight();

/* Plugin from Joshua Poehls and originally Jim Palmer, to give support clip in jquery .animate function */

/*
* jquery.animate.clip.js
*
* jQuery css clip animation support -- Joshua Poehls
* version 0.1.4

* forked from Jim Palmer's plugin http://www.overset.com/2008/08/07/jquery-css-clip-animation-plugin/
* idea spawned from jquery.color.js by John Resig
* Released under the MIT license.
*/
(function (jQuery) {

    function getStyle(elem, name) {
        return (elem.currentStyle && elem.currentStyle[name]) || elem.style[name];
    }

    function getClip(elem) {
        var cssClip = jQuery(elem).css('clip') || '';

        if (!cssClip) {
            // Try to get the clip rect another way for IE8.
            // This is a workaround for jQuery's css('clip') returning undefined
            // when the clip is defined in an external stylesheet in IE8. -JPOEHLS
            var pieces = {
                top: getStyle(elem, 'clipTop'),
                right: getStyle(elem, 'clipRight'),
                bottom: getStyle(elem, 'clipBottom'),
                left: getStyle(elem, 'clipLeft')
            };

            if (pieces.top && pieces.right && pieces.bottom && pieces.left) {
                cssClip = 'rect(' + pieces.top + ' ' + pieces.right + ' ' + pieces.bottom + ' ' + pieces.left + ')';
            }
        }

        // Strip commas and return.
        return cssClip.replace(/,/g, ' ');
    }

    jQuery.fx.step.clip = function (fx) {
        if (fx.pos === 0) {
            var cRE = /rect\(([0-9\.]{1,})(px|em)[,]?\s+([0-9\.]{1,})(px|em)[,]?\s+([0-9\.]{1,})(px|em)[,]?\s+([0-9\.]{1,})(px|em)\)/;

            fx.start = cRE.exec(getClip(fx.elem));
            if (typeof fx.end === 'string') {
                fx.end = cRE.exec(fx.end.replace(/,/g, ' '));
            }
        }
        if (fx.start && fx.end) {
            var sarr = new Array(), earr = new Array(), spos = fx.start.length, epos = fx.end.length,
                emOffset = fx.start[ss + 1] == 'em' ? (parseInt($(fx.elem).css('fontSize')) * 1.333 * parseInt(fx.start[ss])) : 1;
            for (var ss = 1; ss < spos; ss += 2) { sarr.push(parseInt(emOffset * fx.start[ss])); }
            for (var es = 1; es < epos; es += 2) { earr.push(parseInt(emOffset * fx.end[es])); }
            fx.elem.style.clip = 'rect(' +
                parseInt((fx.pos * (earr[0] - sarr[0])) + sarr[0]) + 'px ' +
                parseInt((fx.pos * (earr[1] - sarr[1])) + sarr[1]) + 'px ' +
                parseInt((fx.pos * (earr[2] - sarr[2])) + sarr[2]) + 'px ' +
                parseInt((fx.pos * (earr[3] - sarr[3])) + sarr[3]) + 'px)';
        }
    }
})(jQuery);

/* Code to actually animate the borders */

var IntervalTimer = 1;
varAnmiSpeed = 1000;
setInterval(function(){
  $( window ).resize(function() {
    var topBorderWidth = $('.topBorder').outerWidth();
    var topBorderHeight = $('.topBorder').outerHeight();
  });
  $('.topBorder').animate({'clip':'rect(0px '+topBorderWidth+'px '+(topBorderHeight-topBorderHeight+5)+'px 0px)'}, varAnmiSpeed);
  $('.topBorder').animate({'clip':'rect(0px '+topBorderWidth+'px '+(topBorderHeight)+'px '+(topBorderWidth-5)+'px)'}, varAnmiSpeed);
  $('.topBorder').animate({'clip':'rect('+(topBorderHeight-5)+'px '+topBorderWidth+'px '+(topBorderHeight)+'px 0px)'}, varAnmiSpeed);
  $('.topBorder').animate({'clip':'rect(0px '+(topBorderWidth-topBorderWidth+5)+'px '+(topBorderHeight)+'px 0px)'}, varAnmiSpeed)

  $('.bottomBorder').animate({'clip':'rect('+(topBorderHeight-5)+'px '+topBorderWidth+'px '+(topBorderHeight)+'px 0px)'}, varAnmiSpeed);
  $('.bottomBorder').animate({'clip':'rect(0px '+(topBorderWidth-topBorderWidth+5)+'px '+(topBorderHeight)+'px 0px)'}, varAnmiSpeed)
  $('.bottomBorder').animate({'clip':'rect(0px '+topBorderWidth+'px '+(topBorderHeight-topBorderHeight+5)+'px 0px)'}, varAnmiSpeed);
  $('.bottomBorder').animate({'clip':'rect(0px '+topBorderWidth+'px '+(topBorderHeight)+'px '+(topBorderWidth-5)+'px)'}, varAnmiSpeed);

  IntervalTimer = varAnmiSpeed * 4;
}, IntervalTimer);


//text
var animationType = function(myTarget, myClass) {
  var delay = 3;
  var colors = ['#ffffff', '#ffffff', '#ffffff', '#ffffff', '#ffffff'];
  var myTextToSplit = document.getElementsByClassName(myTarget);
  for (var i = 0; i < myTextToSplit.length; i++) {
    /* Val for the win  */
    var myTag = myTextToSplit[i].innerHTML.split(/(<[^>]+>)/g);
    var html = '';

    //console.log(myTag);
    for (var j = 0; j < myTag.length; j++) {

      html += (!myTag[j].includes('<') && !myTag[j].includes('\n') ? myTag[j].split('').join('</span><span class=\'' + myClass + ' \' >') : myTag[j]);

    }
    myTextToSplit[i].innerHTML = "<span class=\'" + myClass + " \'>" + html + "</span>";

  }
  var elemDelay = document.getElementsByClassName(myClass);
  for (i = 0; i < elemDelay.length; i++) {
    elemDelay[i].style.animationDelay = delay - (delay / (i + delay)) + "s";
    elemDelay[i].style.color = colors[i % colors.length];

  }
  console.log(elemDelay.length);

}
animationType('textAnim', 'textAnim1');
