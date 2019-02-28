var but = document.getElementById('btn');
but.addEventListener('mouseover',changeOnMouseOver);
but.addEventListener('mouseout',changeOnMouseOut);
function changeOnMouseOver() {
    this.style.background='red';
}
function changeOnMouseOut() {
    this.style.background='blue';
}
/*document.getElementById('btn').onmouseover=function() {
    this.style.background='red';
}
document.getElementById('btn').onmouseout=function() {
    this.style.background='blue';
}*/