
function Example(){
    var rating = document.getElementById('first').getAttribute("data-value");
    var x ="", i;
    for (i=1; i<=rating; i++) {
    x = x + "<a>⭐</a>";
    }
    document.getElementById("demo").innerHTML = x;
    }
Example();
