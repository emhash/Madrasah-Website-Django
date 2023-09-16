'use strict';
(function ($) {
	jQuery(window).load(function(){
		jQuery(window).trigger('resize');
	});

	jQuery(window).on('elementor/frontend/init', function(){
		elementorFrontend.hooks.addAction('frontend/element_ready/wb-news-ticker.default', function ($scope, $) {
			$scope.find('.wb-breaking-news-ticker').breakingNews();
		});
	});
})(jQuery);
/*This file was exported by "Export WP Page to Static HTML" plugin which created by ReCorp (https://myrecorp.com) */