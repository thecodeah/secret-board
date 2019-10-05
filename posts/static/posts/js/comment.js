$(document).ready(function() {
    $(document).on("submit", ".js-formComment", function(e){
        e.preventDefault(); // Prevent form to refresh page

        var post_id = $(this).attr("name").slice(12);
        var commentstring = $(this).find(".comment-input").val();

        $.ajax({
            context: this,
            type: "POST",
            url: comment_post_url,
            data: {
                "csrfmiddlewaretoken": csrf_token,
                "post_id": post_id,
                "content": commentstring
            },
            dataType: "json",
            success: function(response) {

                // Update comment count
                $(`button[name ="comment-${post_id}"]`).children(".js-commentCount").text(response.comment_count);

                // Create new comment
                var comment_template = $("#single-comment").html();
                var $comment = $(comment_template);
                
                $comment.find("b").text(`${username}:`);
                $comment.find("span").text(commentstring);

                $comment.insertBefore($(this));

                // Empty the comment input box
                $(this).find(".comment-input").val("");

                //$(this).children(".js-likeCount").text(response.like_count);
            },
            error: function(response, err) {
                alert("Whoopsy daisy! Something went wrong! Try again later...");
            }
        });
    });
});
