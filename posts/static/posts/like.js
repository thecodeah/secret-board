$(document).ready(function() {
    $(".js-actionLike").click(function(){
        $.ajax({
            context: this,
            type: "POST",
            url: post_url,
            data: {
                "csrfmiddlewaretoken": csrf_token,
                "post_id": $(this).attr("name").slice(5)
            },
            dataType: "json",
            success: function(response) {
                if(response.liked) {
                    $(this).prop("value", `Unlike`);
                } else {
                    $(this).prop("value", `Like`);
                }

                $(this).siblings(".js-likeCount").text(response.like_count);
            },
            error: function(response, err) {
                alert("Whoopsy daisy! Something went wrong! Try again later...");
            }
        });
    });
});