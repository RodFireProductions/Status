
displayDay = function(id) {
    let now = new Date();
    let day; let time;
    if (now.getDay() == 0 ) { day = "Sunday" };
    if (now.getDay() == 1 ) { day = "Monday" };
    if (now.getDay() == 2 ) { day = "Tuesday" };
    if (now.getDay() == 3 ) { day = "Wednesday" };
    if (now.getDay() == 4 ) { day = "Thursday" };
    if (now.getDay() == 5 ) { day = "Friday" };
    if (now.getDay() == 6 ) { day = "Saturday" };

    if ( now.getHours() <= 11 && now.getHours() >= 0 ) { time = "morning"; }
    else if ( now.getHours() <= 19 && now.getHours() >= 12 ) { time = "afternoon"; }
    else { time = "night"; }

    document.getElementById(id).innerHTML = `${day} ${time}`;
}
