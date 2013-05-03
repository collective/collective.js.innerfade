jq(document).ready(function() {

    var thumbWidth = jq('.imgnolink').width()
    if(!thumbWidth > 0){
        thumbWidth = jq('.imglink').width()
    }
    console.log(thumbWidth)

    var width = parseInt(jq("input[name='width']").val())+thumbWidth
    var height= jq("input[name='height']").val()
    var animationtype = jq("input[name='animationtype']").val()
    var speed = jq("input[name='speed']").val()
    var timeout = jq("input[name='timeout']").val()
    var type = jq("input[name='innerfade_type']").val()
    console.log(type)
    var options = {
        speed: speed,
        timeout: timeout,
        containerheight: height,
        animationtype: animationtype,
        type: type
    }

    console.log(options)
    jq("#InnerfadeContainer").css('width',width)
    jq('#Innerfade').innerFade(options);

    jq(".ifnav img").hover(

        // hover
        function() {
            id = jq(this).parent().attr('id').substr(5);
            
            jq('#Innerfade').innerFadeUnbind();
            jq('#Innerfade').innerFadeTo(id);

        }
    );
});