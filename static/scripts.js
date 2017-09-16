$(document).ready(function() {
    $("#buttonAbout").click(function() {
        //hide welcome stuff
        $("#welcomeContent").css("opacity","0");
                            
        setTimeout(function() {
            $("#welcomeContent").addClass("hidden");
            //show about
            $(".overlay-white").addClass("expanded overlay-whiter");
                
            $("#aboutContent").removeClass("hidden");
            $("#aboutContent").css("opacity","1");
        }, 500);
    });
                  
    $("#buttonBack").click(function() {
    
    //hide about stuff
    $("#aboutContent").css("opacity","0");

        setTimeout(function() {
             $("#aboutContent").addClass("hidden");
             //show about
             $(".overlay-white").removeClass("expanded overlay-whiter");
             $("#welcomeContent").removeClass("hidden");
             $("#welcomeContent").css("opacity","1");
        }, 500);
    });
                  
    $("#buttonStart").click(function() {
        //show start
    });
});
