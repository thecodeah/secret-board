$(document).ready(function() {
    $(document).on("click", ".js-exposeCollapsable", function(e) {
        var $target = $($(this).attr("data-collapsable"));

        $target.toggleClass("show");
    });
});
