let button = document.querySelector("#button");
button.addEventListener("click", myFunction)

function myFunction(){
    hyper = document.createElement("div");
    let parent = document.getElementsByClassName("hypers")
    hyper.className =  "hyper";
    hyper.style.backgroundColor = "red";
    hyper.className = "rounded-end hypers";
    hyper.style.width = "150px";
    hyper.style.height = "250px";
    hyper.style.margin = "20px";
    hyper.style.boxShadow = "0 0 1rem 0 rgba(0, 0, 0, 0.5)";
    document.body.appendChild(hyper);
        }