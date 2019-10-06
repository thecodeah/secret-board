$(document).ready(function() {
    $(document).on("click", ".js-likeButton", function(){
        $.ajax({
            context: this,
            type: "POST",
            url: like_post_url,
            data: {
                "csrfmiddlewaretoken": csrf_token,
                "post_id": $(this).attr("name").slice(5)
            },
            dataType: "json",
            success: function(response) {
                heart = $(this).children(".fa-heart")
                
                // Toggle heart solid and light state
                if(heart.hasClass("far")) {
                    heart.addClass('fas').removeClass('far');
                } else {
                    heart.addClass('far').removeClass('fas');
                }

                // Toggle heart color
                if(heart.hasClass("text-primary")) {
                    heart.addClass('text-muted').removeClass('text-primary');
                } else {
                    heart.addClass('text-primary').removeClass('text-muted');
                }

                $(this).children(".js-likeCount").text(response.like_count);
            },
            error: function(response, err) {
                alert("Whoopsy daisy! Something went wrong! Try again later...");
            }
        });
    });
});