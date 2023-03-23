$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.tabs').tabs();
    $('.modal').modal();

  });


// From Task Manager Tutorial
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



// Modifying from Cookle cookbook
 // Adding and editing ingredients for a recipe
let ingredients;
let maxIngredients = 20;

if ($("#number-ingredients").text()) {
    ingredients = parseInt($("#number-ingredients").text()); 
} else {
    ingredients = 1;
}

$("#add-ing-btn").click(function (e) {
    if (ingredients < maxIngredients) {
        e.preventDefault();
        $("#ingredients-wrapper").append(
        `<div class="d-flex flex-row">
            <input type="text" class="form-control flex-grow new-field" minlength="5" maxlength="200" name="ingredients" required>
            <button class="btn btn-styl btn-remove" type="button"><i class="fa-solid fa-x"></i></button>
        </div>`);
        ingredients++;
    } else {
        $("#add-ing-btn").text("You have reached the max input.");
        e.preventDefault();
    }
});

$("#ingredients-wrapper").on("click", ".btn-remove", function(e){
    e.preventDefault();
    $(this).parent('div').remove();
    $("#add-ing-btn").html('<i class="fas fa-plus"></i> Add more');
    ingredients--;
});


// Adding and editing method/directions for a recipe

let directions;
let maxDirections = 20; 

if ($("#number-directions").text()) {
    directions = parseInt($("#number-directions").text()); 
} else {
    directions = 1;
}

$("#add-dir-btn").click(function (e) {
    if (directions < maxDirections) {
        e.preventDefault();
        $("#directions-wrapper").append(
        `<div class="d-flex flex-row">
            <input type="text" class="form-control new-field" minlength="5" maxlength="750" name="method" required>
            <button class="btn btn-styl btn-remove" type="button"><i class="fa-solid fa-x"></i></i></button>
        </div>`);
        directions++;
    } else {
        $("#add-dir-btn").text("You have reached the max input.");
        e.preventDefault();
    }
});

$("#directions-wrapper").on("click", ".btn-remove", function(e){
    e.preventDefault();
    $(this).parent('div').remove();
    $("#add-dir-btn").html('<i class="fas fa-plus"></i> Add more');
    directions--;
});





