$(document).ready(function() {
	
	if ($('div.info h1').html() == " UNC CS Student Portal ") {
		$('a.home').addClass('current');
	}
	if ($('div.info h1').html() == " Get Hired ") {
		$('a.hired').addClass('current');
	}
	if ($('div.info h1').html() == " Project Marketplace ") {
		$('a.market').addClass('current');
	}
	if ($('div.info h1').html() == " Job Board ") {
		$('a.jobs').addClass('current');
	}

    
	var offset = 420;
	var offsetbottom = $('div.footer').offset().top - 900;
	var duration = 200;
	jQuery(window).scroll(function() {
		if (jQuery(this).scrollTop() > offsetbottom) {
			jQuery('.back-to-top').fadeOut(duration);
		} else if (jQuery(this).scrollTop() > offset) {
			jQuery('.back-to-top').fadeIn(duration);
		} else {
			jQuery('.back-to-top').fadeOut(duration);
		}

	});

	jQuery('.back-to-top').click(function(event) {
		event.preventDefault();
		jQuery('html, body').animate({
			scrollTop : 0
		}, duration);
		return false;
	})
	
	$('div.newform').find('input').addClass('form-control input-sm');
	$('div.newform').find('input').css('width', '100%');
	$('div.newform').find('select').addClass('form-control input-sm');
	$('div.newform').find('select').css('width', '100%');
	$('div.newform').find('textarea').addClass('form-control');
	$('div.newform').find('textarea').css('width', '100%');
	//Do all except the checkbox
	$('div.newform').find('input[type="checkbox"]').css('width', '0');

    $('#offer_job_type select').change(function() {
        
        var val = $('#offer_job_type select option:selected').val();
        if (val === "UI" || val === "VW") {
            $('div.newform select[name="pay_type"] option').prop("disabled",true);
            $('div.newform select[name="pay_type"] option[value="OT"]').removeAttr("disabled");
            $('div.newform input[name="salary"]').val('0');
            $('div.newform input[name="signing_bonus"]').val('');
            $('div.newform input[name="relocation_bonus"]').val('');
            $('div.newform input[name="salary"]').prop("readonly",true);
            $('div.newform input[name="signing_bonus"]').prop("disabled",true);
            $('div.newform input[name="relocation_bonus"]').prop("disabled",true);
        }

        else {
            $('div.newform select[name="pay_type"] option').removeAttr('disabled');
            $('div.newform input[name="salary"]').removeAttr('readonly');
            $('div.newform input[name="signing_bonus"]').removeAttr('disabled');
            $('div.newform input[name="relocation_bonus"]').removeAttr('disabled');
        }
    });
	
	/* Event for disabling state selection when an international
       country is selected when creating a new post */

    $('div.newform select[name="country"]').change(function() {


    	if ($('div.newform select[name="country"] option:selected').val() !== "US") {
    		$('div.newform select[name="state"] option').prop("disabled", true);
    		$('div.newform select[name="state"]').val('IT');
    		$('div.newform select[name="state"] option[value="IT"]').removeAttr('disabled');
    		$('div.newform input[name="city"]').prop("readonly", true);
    		$('div.newform input[name="city"]').val('International');
    	}
    	else {
    		$('div.newform select[name="state"] option').removeAttr('disabled');
    		$('div.newform select[name="state"] option[value="IT"]').removeAttr('disabled');
    		$('div.newform select[name="state"]').val('AL');
    		$('div.newform input[name="city"]').removeAttr('readonly');
    		if ($('div.newform input[name="city"]').val() === 'International') {
    			$('div.newform input[name="city"]').val('');
    		}
    	}
    });
    $('button.form_with_password').click(function(e) {
        if ($('#confirm_password').length == 0) {
            console.log('worked');
            $('form').submit();
        }

        else {
            console.log('didnt');
        }
        var password = $('input[name="password"]').val();
        var confirmation = $('#confirm_password').val();

        if (password === confirmation) {
            $('form').submit();
        }

        else {
            e.preventDefault();
            $('#password_error').empty();
            $('#password_error').append('<li>Passwords do not match</li>');
        }
    });
    /* Confirm before deletion */
    $('#submit_link').click(function() {
        if (confirm('Do you really want to delete this post?')) {
            $('form#delete').submit();
        }
    });

    /* Parse number with commas on submit */
    $('div.new-offer-form form').submit(function() {
    	$(this).find('.money_field input').each(function() {
    		$(this).val($(this).val().replace(/,/g,''));
    	});
    });

    /* datepicker widget */
    $(function() {
    	$('div.date input').datepicker({ dateFormat: "yy-mm-dd"});
  	});
	
    $(function () {
        $("select#id_technologies").chosen();
    });

    $(function () {
        $("[data-rel='tooltip']").tooltip();
    });
	
    if ($(document).height() == $(window).height()) {
    	$('div.footer').css('position','absolute');
    	$('div.footer').css('bottom','0');
    }
    
    /*URI implementation to grab URL search parameters and track user searches. We then select the
     * appropriate selectors/input values in the filterdiv
     */
    var uri = new URI(document.URL);
    if(uri.hasSearch("location")){
    	var search = uri.search(true);
    	for(key in search){
    		if(key == 'post_type'){
    			if(search[key] == 'interview,offer'){
    				$('div.filterdiv input[value="offer"]').prop("checked", true);
    				$('div.filterdiv input[value="interview"]').prop("checked", true);
    			} else
    			$('div.filterdiv input[value='+search[key]+']').prop("checked", true);
    		} else{
    			$('div.filterdiv select[name="'+key+'"] option[value="'+search[key]+'"]').prop('selected', true);
    		}
    	}
    } else{
    		if(uri.segment(1) == "company"){
    			var name = uri.segment(2).replace("-"," ");
    			$('div.filterdiv select[name="company"] option[value="'+name.toProperCase()+'"]').prop('selected', true);
    		}
    }
    
    if(uri.hasSearch("technology")){
    	var search = uri.search(true);
    	for(key in search){
    		console.log(key);
    		if(key == 'technology'){
    			$('div.filterdiv select[name="'+key+'"] option[value="'+search[key]+'"]').prop('selected', true);
    			}
    	
    		}
    	}
    
    
    
    $('div.hover-test').each(function(index, value){
    	var number = $(value).attr('data-num');
        $(value).remove();
        $('body').append('<div class="hover-div hover-'+number+'" style="display: none; position:absolute;">'+$(value).html()+'</div>');
        var hover_div = $('div.hover-'+number);
        var action_div = $('div.related-post[data-num="'+number+'"]');
        var width = action_div.offset().left + hover_div.width();
        var width2 = action_div.offset().left + action_div.width();
        	action_div.mouseenter(function(){
        	hover_div.show();
        	hover_div.css('top', action_div.offset().top+'px');
        	
        	if(width > width2){
        		hover_div.css('left', (width) +'px');
        	} else{
        		hover_div.css('left', (width2) +'px');
        	}
        	
        	}).mouseleave(function(){
        	hover_div.hide();
        	});
    });
    
});

String.prototype.toProperCase = function () {
    return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
};