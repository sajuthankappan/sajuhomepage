$(document).ready(function(){
    $.history.init(loadContent);
    
    $(".tm").click(function(){
        var url = $(this).attr('href');
        url = url.replace(/^.*#/, '');
        $.history.load(url);
    });
    
});

function loadContent(hash) {
    if (hash == "") {
        hash = "home";
    }
    $(".active").removeClass("active");
    $("#" +hash).addClass("active");
    $("#contentarea").load(hash + ".html");
}