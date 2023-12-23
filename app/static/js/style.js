document.body.style.transition = "background-color 190s ease";

counter = 0;
var a = new Date()
console.log(a.getMinutes() + " " + a.getSeconds())
function animate() {
    const colors = ['#f79824','#fdca40', '#ffd166', 'white', '#33a1fd', '#2176ff', '#31393c', 'black'];
    currentColor = colors[counter];
    document.body.style.backgroundColor = currentColor;
    counter+=1;

    if (counter==9) {
        var notif = document.createElement("div")
        notif.classList.add("alert", "alert-danger", "center-alert")


        var text = document.createTextNode("Time's up!")
        notif.appendChild(text)

        var blogs = document.getElementById('blogs')
        document.body.appendChild(notif)

        var b = new Date()
        console.log(b.getMinutes() + " " + b.getSeconds())
    }
}

var intervalID = setInterval(() => {
        if (counter < 9) {
            animate()
        } else {
            clearInterval(intervalID)
        }
    }, 200000)