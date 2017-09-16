$(document).ready(function() {
    $("#buttonAbout").click(function() {
        //hide welcome stuff
        $("#welcomeContent").css("opacity","0");
                            
        setTimeout(function() {
            $("#welcomeContent").addClass("hidden");
            //show about
            $(".overlay-white").addClass("expanded-medium overlay-whiter");
            $("#aboutContent").removeClass("hidden");
                   
            setTimeout(function() {
                $("#aboutContent").css("opacity","1");
            }, 800);
        }, 500);
    });
                  
    $("#buttonBack").click(function() {
    
    //hide about stuff
    $("#aboutContent").css("opacity","0");

        setTimeout(function() {
            $("#aboutContent").addClass("hidden");
            //show about
            $(".overlay-white").removeClass("expanded-medium overlay-whiter");
            $("#welcomeContent").removeClass("hidden");
                   
            setTimeout(function() {
                $("#welcomeContent").css("opacity","1");
            }, 800);
        }, 500);
    });
                  
    $("#buttonStart").click(function() {
        //show start
    });
});
