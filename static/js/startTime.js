function startTime()
{
var tm=new Date();
var h=tm.getHours();
var m=tm.getMinutes();
m=checkTime(m);
document.getElementById('txt').innerHTML=h+":"+m;
t=setTimeout('startTime()',500);
}
function checkTime(i)
{
if (i<10)
{
i="0" + i;
}
return i;
}
