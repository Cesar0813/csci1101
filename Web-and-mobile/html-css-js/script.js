window.addEventListener("load", function ()
{
    //Get click element references.
    let clickCounterElement = document.getElementById("click-counter");
    let clickButtonElement = document.getElementById("click-button");

    // counter value.
    let counter = 0;

    //click button function.
    let clickButtonFunction = function ()
    {
        // Increment counter.
        counter++;

        //update counter value.
        clickCounterElement.innerHTML =counter;
    };

    //attach button function.
    clickButtonElement.addEventListener("click", clickButtonFunction);
});