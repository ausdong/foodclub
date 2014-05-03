$(document).ready(function(){
				$('#lightbox_trigger_{{post.id}}').click(function() {
					$('#lightbox').show();
					$('#gallery-container_{{post.id}}').show();
				});
				$('#lightbox').click(function() {
					$('#lightbox').hide();
					$('#gallery-container_{{post.id}}').hide();
				});
				$('#right_{{post.id}}').click(function() {
					var post_id = {{post.id}} - 1;
					if($('#gallery-container_' + post_id).length == 0) {
						alert("No more photos right!");
					} else {
						$('#gallery-container_{{post.id}}').hide();
						$('#gallery-container_' + post_id).show();
					}
				});
				$('#left_{{post.id}}').click(function() {
					var post_id = {{post.id}} + 1;
					if($('#gallery-container_' + post_id).length == 0) {
						alert("No more photos left!");
					} else {
						$('#gallery-container_{{post.id}}').hide();
						$('#gallery-container_' + post_id).show();
					}
				});
				$('#lightbox_trigger_{{post.id}}').hover(function() {
					$('#box_inside_{{post.id}}').show();
				}, function() {
					$('#box_inside_{{post.id}}').hide();
				});
			

				
				
			});