window.addEventListener("load",init)

function init(){
    document.querySelector("input").addEventListener("change", send)
}

function send(){
    remAnim()
    addAnim()
    movie = document.querySelector("input").value
    if(movie.trim().length == 0){
        document.querySelector("#error").innerHTML = ""
        remAnim(); 
        return;
    }
    console.log("movie")
    request = {"name": ""+movie.trim()}
    document.querySelector("#error").innerHTML = ""
    document.querySelector("ul").innerHTML = ""
    $.ajax({
        crossOrigin: true,
        url: 'http://localhost:5000/server',
        contentType: 'application/json',
        data: JSON.stringify(request),
        type: 'POST',
        success: function (res){
            printResponse(res)
            remAnim()
        },
        error: function(err) {
            console.log(err);
            var p = document.querySelector("#error")
            p.innerHTML = JSON.parse(err.responseText).message
            remAnim()
        }
      });
}

function printResponse(movies){
    // document.querySelector("#error").className = "hide"
    movies = JSON.parse(movies)
    console.log(movies)
    var ul = document.querySelector("ul")
    // ul.innerHTML = ""
    var names = Object.keys(movies)
    // console.log(names[0])
    var i =0
    names.forEach((name)=>{
        var li = document.createElement("li")
        var img = document.createElement("img")
        var p1 = document.createElement("p")
        var p2 = document.createElement("p")
        img.src = movies[name]
        p1.innerHTML = name.slice(0, name.length-7)
        p1.className = "title"
        p2.innerHTML = name.slice(length-6)
        p2.className = "year"
        li.appendChild(img)
        li.appendChild(p1)
        li.appendChild(p2)
        ul.appendChild(li)
        li.setAttribute("name", p1.innerHTML)
        li.addEventListener("click", sendHandler)
        li.style.animation = "slideRight 0.5s  "+i/5+"s 1 forwards";
        li.addEventListener("mouseover",hoverli)
        li.addEventListener("mouseleave",outli)
        i++;
        console.log("done")
    })
}

function hoverli(){
    var li = event.srcElement
    // console.log(li)
    li.style.animation = "";
    li.style.opacity = 1
    li.style.transform = "translateY(-30px)";
}

function outli(){
    var li = event.srcElement
    li.style.transform = "translateY(0px)";
}

function sendHandler(){
    var li = event.srcElement
    // console.log(li);
    try{
    document.querySelector("input").value = li.getAttribute("name")
    send()
    }
    catch(err){
        console.log(err)
    }
}

function addAnim(){
    var logo = document.querySelector("#logo")
    logo.style.animation = "bounce 0.7s ease-in-out 0s infinite forwards";
}

function remAnim(){
    var logo = document.querySelector("#logo")
    logo.style.animation = "";
}