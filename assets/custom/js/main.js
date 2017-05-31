$(document).ready(function () {
    var numberOne = 1 + Math.floor(Math.random()*9);
    var numberTwo = 1 + Math.floor(Math.random()*9);
    var numSum = numberOne + numberTwo;
    
    $("#add-topic-sum-label").text("What is the sum of " + numberOne + " and " + numberTwo + "?");
    
    var addTopicButton = $("#add-topic-button");
    var addTopicSum = $("#add-topic-sum");
    
    addTopicButton.click(function (e) {
        if (addTopicSum.val() === numSum.toString()) {
            addTopicButton.hide();
        } else {
            alert("You have entered a wrong sum! Try again.");
            e.preventDefault();
        }
    });
});
