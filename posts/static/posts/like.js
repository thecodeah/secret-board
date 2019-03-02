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
                $(this).prop("value", `Like (${response.like_count})`)
            },
            error: function(response, err) {
                alert("Woopsy daisy!");
            }
        });
    });
});