$(document).ready(function(){
    $('.sidenav').sidenav();
  });

$(document).ready(function() {
  $('input#recipe_name, textarea#recipe_intro').characterCounter();
});

$(document).ready(function(){
  $('select').formSelect();
  
  $('#textarea1').val('New Text');
  M.textareaAutoResize($('#textarea1'));
});



  
  $(document).ready(function(){
  validateMaterializeSelect();
  function validateMaterializeSelect() {
	  let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
	  let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
	  if ($("select.validate").prop("required")) {
		  $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
	  }
	  $(".select-wrapper input.select-dropdown").on("focusin", function () {
		  $(this).parent(".select-wrapper").on("change", function () {
			  if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
				  $(this).children("input").css(classValid);
			  }
		  });
	  }).on("click", function () {
		  if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
			  $(this).parent(".select-wrapper").children("input").css(classValid);
		  } else {
			  $(".select-wrapper input.select-dropdown").on("focusout", function () {
				  if ($(this).parent(".select-wrapper").children("select").prop("required")) {
					  if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
						  $(this).parent(".select-wrapper").children("input").css(classInvalid);
					  }
				  }
			  });
		  }
	  });
  }
});





$(document).ready(function () {

	$("#repeatDivBtn").click(function () {

		$newid = $(this).data("increment");
		$repeatDiv = $("#repeatDiv").wrap('<div/>').parent().html();
		$('#repeatDiv').unwrap();
		$($repeatDiv).insertAfter($(".repeatDiv").last());
		$(".repeatDiv").last().attr('id',   "repeatDiv" + '_' + $newid);
		$("#repeatDiv" + '_' + $newid).append('<div class="input-field"><button type="button" class="waves-effect waves-light btn styl removeDivBtn" data-id="repeatDiv'+'_'+ $newid+'">Remove</button></div>');
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
		$("#repDiv" + '_' + $newid).append('<div class="input-field"><button type="button" class="waves-effect waves-light btn styl removeBtn" data-id="repDiv'+'_'+ $newid+'">Remove</button></div>');
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






