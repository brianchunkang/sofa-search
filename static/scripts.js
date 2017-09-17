$(document).ready(function() {
                  
    var transitionDelay1 = 500;
    var transitionDelay2 = 500;
	
	$.post("/init",function(data){
		update(data);
	});
                  
    $("#buttonAbout").click(function() {
        
        $("#welcomeContent").css("opacity","0");
                            
        setTimeout(function() {
            $("#welcomeContent").addClass("hidden");
            $(".overlay-white").addClass("expanded-medium overlay-whiter");
            $("#aboutContent").removeClass("hidden");
                   
            setTimeout(function() {
                $("#aboutContent").css("opacity","1");
            }, transitionDelay1);
        }, transitionDelay2);
    });
                  
    $("#buttonStart").click(function() {
                            
        $("#welcomeContent").css("opacity","0");
        
        setTimeout(function() {
            $("#welcomeContent").addClass("hidden");
            $(".overlay-white").addClass("expanded-full");
            $("#sofaContent").removeClass("hidden");
                   
            setTimeout(function() {
                $("#sofaContent").css("opacity","1");
            }, transitionDelay1);
        }, transitionDelay2);
    });
                  
    $(".btn-back").click(function() {
       
        $("#aboutContent").css("opacity","0");
        $("#sofaContent").css("opacity","0");

        setTimeout(function() {
        $("#aboutContent").addClass("hidden");
        $("#sofaContent").addClass("hidden");
        $(".overlay-white").removeClass("expanded-medium expanded-full overlay-whiter");
        $("#welcomeContent").removeClass("hidden");

        setTimeout(function() {
            $("#welcomeContent").css("opacity","1");
            }, transitionDelay1);
        }, transitionDelay2);
    });
	
	$(".btn-small").click(function() {
		$(this).parent().submit(function(data){
			update(data);
		});
	});
	
	function update(data) {
		console.log(data);
		console.log(data.link);
		$("#sofaImage").attr("src",data.img-link);
		$("#viewProd").attr("href",data.link);
	}
});
