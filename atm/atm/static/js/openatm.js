const open_Atm_btn=document.querySelector('#checkCardBtn');
const cardFrom=document.getElementById('openAtm');
open_Atm_btn.addEventListener('click',function(){
  console.log("clicked")
   cardFrom.style.display='block';
})

