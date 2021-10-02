// JavaScript source code




function clock() {//my efforts in trying to display a clock on the right hand side of the page
    var now = new Date();
    var hour = now.getHours();
    var min = now.getMinutes();
    var sec = now.getSeconds();
    hour = updateTime(hour);
    min = updateTime(min);
    sec = updateTime(sec);
    document.getElementById("time").innerText = hour + ":" + min + ":" + sec;
    var time = setTimeout(function () { clock() }, 1000);
}

function updateTime(k) {
    if (k < 10) {
        return "0" + k;
    }
    else {
        return k;
    }
}

clock();