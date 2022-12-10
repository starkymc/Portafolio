let a=document.getElementById('enlace');
a.addEventListener('click',function (event) {
  event.preventDefault(); //esto cancela el comportamiento del click
  setTimeout(()=> location.href="http://127.0.0.1:8000/profile/",5000);
});