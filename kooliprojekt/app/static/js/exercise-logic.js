
        
        
        setTimeout(() => {
            // For correctly rendering MathJax
            MathJax.Hub.Typeset();
            
            let checker = (arr, target) => target.every(v => arr.includes(v)) && target.length > 0;
            let someChecker = (arr, target) => target.some(v => arr.includes(v)) && target.length > 0;


            $(".question-submit-btn").click(function (){
                var questionId = $(this).attr("question-id");

                

                var choices = $(".question-choices[question-id="+questionId.toString() + "]");

                var answers = [];
                var correctAnswers = [];

                choices.children().each(function (){
                    if($(this).attr("isCorrect") == "true"){
                        correctAnswers.push($(this).attr("choiceId").toString().toLowerCase());
                    }
                    var isChecked = $(this).children().is(":checked");
                    if(isChecked){
                        answers.push($(this).attr("choiceId"));
                    }

                    $(this).children().prop("checked", false);
                });


                var result;


                if($(".question-write[question-id=" + questionId.toString() + "]").length){
                    // Write answer
                    if(correctAnswers.includes($(".question-write[question-id=" + questionId.toString() + "]").val().toLowerCase())){
                        result = "🎉 Õige vastus!";
                        $(".question-load-div[question-id=" + questionId.toString() + "]").removeClass("question-undone");
                        $(".question-load-div[question-id=" + questionId.toString() + "] .error-text").hide();
                    }else{
                        result = "👎 Vale vastus!";
                    }
                }else if($("input[type='range'][question-id=" + questionId.toString() + "]").length){
                    var correctMin = parseInt($("input[type='range'][question-id=" + questionId.toString() + "]").attr("correct-min"));
                    var correctMax = parseInt($("input[type='range'][question-id=" + questionId.toString() + "]").attr("correct-max"));

                    var answer = parseInt($("input[type='range'][question-id=" + questionId.toString() + "]").val());

                    if(correctMin <= answer && answer <= correctMax){
                        result = "🎉 Õige vastus!";
                        $(".question-load-div[question-id=" + questionId.toString() + "]").removeClass("question-undone");
                        $(".question-load-div[question-id=" + questionId.toString() + "] .error-text").hide();
                    }else{
                        result = "👎 Vale vastus!";
                    }

                }else{

                    //Not write answer
                    if(checker(correctAnswers, answers)){
                        result = "🎉 Õige vastus!";
                        $(".question-load-div[question-id=" + questionId.toString() + "]").removeClass("question-undone");
                        $(".question-load-div[question-id=" + questionId.toString() + "] .error-text").hide();
                        
                    }else if(someChecker(answers, correctAnswers)){
                        result = "😐 Pooleldi õige!";
                    }else{
                        result = "👎 Vale vastus!";
                    }
                }

                

                $(".question-card-back > .question-result[question-id=" + questionId.toString() + "]").text(result);

                $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-front").css("opacity", "0");

                

                setTimeout(() => {
                    $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-front").css("display", "none");
                    $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-back").css("opacity", "0");

                    $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-back").css("display", "block");

                    $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-back").css("opacity", "1");
                }, 200);



            });

            $(".explanation-btn").click(function (){
                var questionId = $(this).attr("question-id");
                $(".explanation[question-id=" + questionId.toString() + "]").toggle();
                if($(".explanation[question-id=" + questionId.toString() + "]").is(":visible")){
                    $(this).text("Peida selgitus")
                }else{
                    $(this).text("Vaata selgitust")
                }
            });

            $(".try-again-btn").click(function (){
                var questionId = $(this).attr("question-id");
                $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-back").css("opacity", "0");
                setTimeout(() => {
                    $(".explanation-btn[question-id="+questionId+"]").text("Vaata selgitust!");

                    $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-back").css("display", "none");
                    $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-front").css("display", "block");
                    $(".explanation[question-id=" + questionId.toString() + "]").hide();

                    $(".question-load-div[question-id=" + questionId.toString() + "] .question > .question-card-front").css("opacity", "1");
                }, 200);
            });

            
            $("input[type='range']").on("change mousemove", function (){
                $(".range-value[question-id="+ $(this).attr("question-id") +"]").text($(this).val().toString());
            });
        }, 1000);