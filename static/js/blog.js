'use strict';

$(function () {

  var scrollFixing = function () {
    var offset = 50,
        init = function init() {
      _events();
    };

    var checkFixation = function checkFixation(targets) {
      var $targets = targets || $('.js-pushpin-target');

      $targets.each(function () {
        var rect = this.getBoundingClientRect(),
            fixingParent = $(this).closest('.js-pushpin-parent'),
            fixingParentRect = fixingParent[0].getBoundingClientRect(),
            parentRect = $(this).parent()[0].getBoundingClientRect(),
            top = 100;

        if (rect.height >= fixingParentRect.height) return;

        if (fixingParentRect.top <= 100 && fixingParentRect.bottom > 100 + rect.height) {
          this.style.width = rect.width + 'px';
          this.style.top = top + 'px';
          this.style.position = 'fixed';
        } else if (fixingParentRect.top > 100) {
          this.style.position = 'static';
        } else if (fixingParentRect.bottom <= 100 + rect.height) {
          top = fixingParentRect.height - rect.height;
          this.style.top = top + 'px';
          this.style.position = 'absolute';
        }
      });
    };

    var resetTargetsWidth = function resetTargetsWidth() {
      var $targets = $('.js-pushpin-target');

      $targets.each(function () {
        var width = $(this).parent().width();
        this.style.width = width + 'px';
      });
    };

    var _events = function _events() {
      $(document).off('scroll.pushpin').off('DOMContentLoaded.pushpin');

      $(document).on('scroll.pushpin', function () {
        checkFixation();
      });

      $(window).on('resize.pushpin', resetTargetsWidth);

      $(document).on('DOMContentLoaded.pushpin', function () {
        checkFixation();
      });
    };

    init();

    return {
      checkFixation: checkFixation
    };
  }();
});/**
 * Created by Ana Ash on 8/17/2017.
 */
