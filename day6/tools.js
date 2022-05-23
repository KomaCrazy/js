
function cb1(){
    var con = document.getElementById("cb1").checked;
    console.log(con)
    if (con == true){
        document.getElementById("body").style.background = "#FFDB88"
        document.getElementById("body").style.color = "#25272A"
        console.log("White")
    }
    else if (con == false)
    {
        document.getElementById("body").style.background = "#25272A"
        document.getElementById("body").style.color = "#FFDB88"
        console.log("black")

    }
    }