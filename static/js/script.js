$(document).ready(function(){
    $('.sidenav').sidenav();
  });

$(document).ready(function() {
  $('input#recipe_name, input#recipe_intro').characterCounter();
});

$(document).ready(function(){
  $('select').formSelect();
});


$(document).ready(function () {

	$("#repeatDivBtn").click(function () {

		$newid = $(this).data("increment");
		$repeatDiv = $("#repeatDiv").wrap('<div/>').parent().html();
		$('#repeatDiv').unwrap();
		$($repeatDiv).insertAfter($(".repeatDiv").last());
		$(".repeatDiv").last().attr('id',   "repeatDiv" + '_' + $newid);
		$("#repeatDiv" + '_' + $newid).append('<div class="input-field"><button type="button" class="waves-effect waves-light btn removeDivBtn" data-id="repeatDiv'+'_'+ $newid+'">Remove</button></div>');
		$newid++;
		$(this).data("increment", $newid);

	});


	$(document).on('click', '.removeDivBtn', function () {

		$divId = $(this).data("id");
		$("#"+$divId).remove();
		$inc = $("#repeatDivBtn").data("increment");
		$("#repeatDivBtn").data("increment", $inc-1);

	});

});


$(document).ready(function () {

	$("#repeatBtn").click(function () {

		$newid = $(this).data("increment");
		$repeatDiv = $("#repDiv").wrap('<div/>').parent().html();
		$('#repDiv').unwrap();
		$($repeatDiv).insertAfter($(".repDiv").last());
		$(".repDiv").last().attr('id',   "repDiv" + '_' + $newid);
		$("#repDiv" + '_' + $newid).append('<div class="input-field"><button type="button" class="waves-effect waves-light btn removeBtn" data-id="repDiv'+'_'+ $newid+'">Remove</button></div>');
		$newid++;
		$(this).data("increment", $newid);

	});


	$(document).on('click', '.removeBtn', function () {

		$divId = $(this).data("id");
		$("#"+$divId).remove();
		$inc = $("#repeatBtn").data("increment");
		$("#repeatBtn").data("increment", $inc-1);

	});

});






