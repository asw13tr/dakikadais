$(function(){

$('span.moresidemenu').on('click', function(){
	$(this).parent('.sidecontent').find('.sidemenu').addClass('full');
	$(this).remove();
});

// ekran çözünürlüğü değişince kullanılacak kodlar başlangıcı
sidemenu_col_control();
$(window).resize(function(event) {
	sidemenu_col_control();
});
// ekran çözünürlüğü değişince kullanılacak kodlar bitişi

});


function sidemenu_col_control(){
	var w = $('.sidemenu.col2').first().outerWidth();
	if(w < 250){
		$('.sidemenu.col2').addClass('col1');
	}else{
		$('.sidemenu.col2').removeClass('col1');
	}
}