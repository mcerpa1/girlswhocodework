<script>
$('body').on({
    mousemove: function(e){
        // Calculate number of stars
        var currentMousePosition = e.pageX - $(this).offset().left;
        var width = $(this).width();
        var rounded = Math.round((currentMousePosition/width)*10);

        var starNumber = rounded/2;

        // Remove + add Classes
        $(this).removeClass();
        $(this).addClass('stars s-' + starNumber);

        // Store current rating
        $(this).attr('data-rating', starNumber);
    },
    mouseleave:function(){
        $(this).removeClass();
        $(this).addClass('stars s-' + $(this).attr('data-default'));
    },
    click: function(){
        //Hide the current rating selector
        $(this).replaceWith($('<div>', {
            'class': 'loading'
        }));

        // Send the request
        $.ajax('rating.php',{
            rating: $(this).attr('data-rating')
        }, function(d){
            // Handle response
            if(d.result == 'error'){
                alert(d.msg);
            } else {
                $(this).removeClass();
                $(this).addClass('stars s-' + d.rating);
                $(this).attr('data-default', d.rating);
                $temp = $(this);
                $('.loading').replaceWith($temp);
            }
        }, 'json');
    }
}, '.stars');
</script>
