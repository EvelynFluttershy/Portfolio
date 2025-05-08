var cart_count = 0;
var cart_price = 0;
var sale_ready = false;

$(document).ready(function(){
	$.each(products,function(i,obj){
		let p = `<div class ="product">
<img src="${obj.img}">
<div class="name">${obj.name}</div>
<div class="buy">
<div>${price(obj.price)}</div>
<button type="button" onclick="addToCart(${i})">lägg till i varukorg</button>
</div>
</div>`; /* *** *** */
		$("#products").append(p);
	})

	filter();
});

function addToCart(i) { /* *** *** */
	cart_count += 1;
	cart_price += products[i].price;
	products[i].count += 1;
	$("#counter").css({"display":"block"});
	$("#counter").text(cart_count);
	updateCart();
}
function updateCart() {
	var list = [];
	//var cart_list = [];
	//var sale_list = [];
	var total = 0;
	$.each(products,function(i,obj){
		if (obj.count > 0) {
			list.push({"name": obj.name, "img": obj.img, "count": obj.count, "sum": obj.count * obj.price});
			//cart_list.push(`${obj.count} × ${obj.name}, ${price(obj.count * obj.price)}`);
			total += obj.count * obj.price;
		}
	});
	var cart_output = ``;
	var sale_output = ``;
	$.each(list,function(i,obj){
		cart_output += `<div>${obj.count} × ${obj.name}, ${price(obj.sum)}</div>`;
		sale_output += `<div class="sale_row"><div class="sale_image"><img class="sale_image" src="${obj.img}"></div><div class="sale_name">${obj.name}</div><div class="sale_count">${obj.count} st</div><div class="sale_price">${price(obj.sum)}</div></div>`;
	});
	if (list.length === 0) {
		$("#cart_content").html("Varukorgen är tom");
		$("#cart_content").addClass("cart_error");
		$("#cart_buy").prop("disabled", true);
	} else {
		$("#cart_content").html(cart_output);
		$("#cart_content").removeClass("cart_error");
		$("#cart_buy").prop("disabled", false);
		$("#sale_content").html(sale_output);
		$("#sale_sum_order").html(price(total));
		let shipping = (Math.floor(cart_count/5)+1) * 29;
		$("#sale_sum_ship").html(price(shipping));
		$("#sale_sum_total").html(price(total + shipping));
		$("#sale_sum_vat").html(price((total + shipping)/5));
	}
	$("#cart_sum").text(`Summa: ${price(total)}`);
}
function openCart() { /* *** *** */
	if ($("#cart").css("display") == "none") {
		updateCart();
		$("#cart").css({"display":"block"});
	} else {
		$("#cart").css({"display":"none"});
	}
}
function closeCart() { /* *** *** */
	$("#cart").css({"display":"none"});
}
function openSale() { /* *** *** */
	if (cart_count > 0) {
		$("#sale").css({"display":"block"});
	}
}
function closeSale() { /* *** *** */
	$("#sale").css({"display":"none"});
}
function completeSale() {
	sale_ready = true;
	check_input("#addr_name",true);
	check_input("#addr_street",true);
	check_input("#addr_postno",true);
	check_input("#addr_city",true);
	check_input("#card_name",true);
	check_input("#card_number",true);
	check_input("#card_valid",true);
	check_input("#card_cvv",true);
}
function check_input(which,strict) {
	let error_id = which+"_error";
	if (which === "#addr_name" || which === "#addr_street" || which === "#addr_city" || which === "#card_name" || which === "#card_cvv") {
		format_input(which,strict);
		clear_error_input(error_id)
		if (strict) {
			if ($(which).val() == "") {
				error_input(error_id,"Fältet kan inte lämnas tomt");
			}
		}
	} else if (which === "#addr_postno") {
		format_input(which,strict);
		clear_error_input(error_id)
		if (strict) {
			if ($(which).val() == "") {
				error_input(error_id,"Fältet kan inte lämnas tomt");
			} else if ($(which).val().length < 5) {
				error_input(error_id,"Postnummret måste vara 5 siffror");
			}
		}
	} else if (which === "#card_number") {
		format_input(which,strict);
		clear_error_input(error_id)
		if (strict) {
			if ($(which).val() == "") {
				error_input(error_id,"Fältet kan inte lämnas tomt");
			} else if ($(which).val().length < 16) {
				error_input(error_id,"Kortnummret måste vara 16 siffror");
			} else if (!$(which).val().match(/^(222[1-9]|22[3-9]|2[3-6]|27[01][0-9]|2720|4[0-8]|49[24-9]|490[0-246-9]|491[02-9]|493[0-57-9]|5[1-5])/)) {
				error_input(error_id,"Endast Visa och Mastercard accepteras");
			}
		} else {
			if (!$(which).val().match(/^((222|22|2|27|272|4|49|490|491|493|5|)$|222[1-9]|22[3-9]|2[3-6]|27[01][0-9]|2720|4[0-8]|49[24-9]|490[0-246-9]|491[02-9]|493[0-57-9]|5[1-5])/)) {
				error_input(error_id,"Endast Visa och Mastercard accepteras");
			}
		}
	} else if (which === "#card_valid") {
		format_input(which,strict);
		clear_error_input(error_id)
		if (strict) {
			if ($(which).val() == "") {
				error_input(error_id,"Fältet kan inte lämnas tomt");
			} else if ($(which).val().length < 4) {
				error_input(error_id,"Giltighetstiden måste vara 4 siffror");
			} else if (!$(which).val().match(/^(0[1-9]|1[0-2])\/[0-9]{2}/)) {
				error_input(error_id,"Måste vara i formatet MM/ÅÅ");
			}
		} else {
			if ($(which).val().match(/^([2-9]|1[3-9]|00)/)) {
				error_input(error_id,"Måste vara i formatet MM/ÅÅ");
			}
		}
	}
}
function format_input(which,strict) {
	if (which === "#addr_name") {
		let fix = $(which).val().replace(/(^\s+|[^A-Za-z \-ÅåÄäÖöÀàÁáÂâÃãÆæÇçÈèÉéÊêËëÌìÍíÎîÏïÐðÑñÒòÓóÔôÕõØøÙùÚúÛûÜüÝýÞÞÿ])/g,"");
		if (strict) {
			fix = fix.replace(/\s+$/,"");
		}
		$(which).val(fix);
	} else if (which === "#addr_city") {
		let fix = $(which).val().replace(/(^\s+|[^A-Za-z \-ÅåÄäÖöÀàÁáÉé])/g,"");
		if (strict) {
			fix = fix.replace(/\s+$/,"");
		}
		$(which).val(fix);
	} else if (which === "#addr_street") {
		let fix = $(which).val().replace(/(^\s+|[^0-9A-Za-z \-ÅåÄäÖöÀàÁáÉé])/g,"");
		if (strict) {
			fix = fix.replace(/\s+$/,"");
		}
		$(which).val(fix);
	} else if (which === "#addr_postno") {
		let fix = $(which).val().replace(/(^0|[^0-9]\/?)/g,"");
		if (fix.length > 5) {
			fix = fix.substr(0,5);
		}
		if (fix.length > 3) {
			fix = fix.substr(0,3)+" "+fix.substr(3,2);
		}
		$(which).val(fix);
	} else if (which === "#card_name") {
		let fix = $(which).val().replace(/^\s+/g,"");
		if (strict) {
			fix = fix.replace(/\s+$/,"");
		}
		$(which).val(fix);
	} else if (which === "#card_number") {
		let fix = $(which).val().replace(/[^0-9]/g,"");
		if (fix.length > 16) {
			fix = fix.substr(0,16);
		}
		if (fix.length > 12) {
			fix = fix.substr(0,4)+" "+fix.substr(4,4)+" "+fix.substr(8,4)+" "+fix.substr(12,4);
		} else if (fix.length > 8) {
			fix = fix.substr(0,4)+" "+fix.substr(4,4)+" "+fix.substr(8,4);
		} else if (fix.length > 4) {
			fix = fix.substr(0,4)+" "+fix.substr(4,4);
		}
		$(which).val(fix);
	} else if (which === "#card_valid") {
		let fix = $(which).val().replace(/[^0-9]/g,"");
		if (fix.length > 4) {
			fix = fix.substr(0,4);
		}
		if (fix.length > 2) {
			fix = fix.substr(0,2)+"/"+fix.substr(2,2);
		}
		$(which).val(fix);
	} else if (which === "#card_cvv") {
		let fix = $(which).val().replace(/[^0-9]/g,"");
		if (fix.length > 4) {
			fix = fix.substr(0,4);
		}
		$(which).val(fix);
	}
}
function error_input(which,message) {
	$(which).text(message);
	$(which).css("display","block");
}
function clear_error_input(which) {
	$(which).text("");
	$(which).css("display","none");
}

function filter() { /* *** *** */
	const filters = [$("#hud").prop("checked"),
		$("#ögon").prop("checked"),
		$("#läppar").prop("checked"),
		$("#naglar").prop("checked")
	];
	const types = ["hud","ögon","läppar","naglar"];
	const product_divs = $(".product");
	const noFilters = filters.every(f => !f);
	var count = 0;
	$.each(product_divs,function(i,obj){
		let show = noFilters;
		if (!show) {
			$.each(filters,function(j,filt){
				if (filt && products[i].type.includes(types[j])) {
					show = true;
				}
			});
		}
		if (show) {
			$(obj).css({"display":"inline-block"});
			count += 1;
		} else {
			$(obj).css({"display":"none"});
		}
	})
	$("#product_stats").text(`${number(count,0,0)} produkt` + (count != 1 ? `er` : ``));
}

function number(val,min,max) { /* *** *** */
	return Number(val).toLocaleString("sv-SE", {minimumFractionDigits: min, maximumFractionDigits: max}).replace(" ","\xa0");
}
function price(val) { /* *** *** */
	return number(val,2,2)+"\xa0kr";
}