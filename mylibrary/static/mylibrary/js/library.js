/**
 * Created by shamsad on 5/29/17.
 */

var BooksListPage = {
	init: function() {
		this.$container = $('.books-container');
		this.render();
		this.bindEvents();
	},

	render: function() {

	},

	bindEvents: function() {
		$('.btn-favorite', this.$container).on('click', function(e) {
			e.preventDefault();

			var self = $(this);
			var url = $(this).attr('href');
			$.getJSON(url, function(result) {
				if (result.success) {
					$('.glyphicon-star', self).toggleClass('active');
				}
			});

			return false;
		});
	}
};



$(document).ready(function() {
	BooksListPage.init();
	//SongsListPage.init();
});