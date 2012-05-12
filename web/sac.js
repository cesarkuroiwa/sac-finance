function calculate()
{
	var result = document.getElementById("result");
	var interest = document.getElementById("interest").value;
	var value = document.getElementById("value").value;
	var period = document.getElementById("period").value;
	var taxes = document.getElementById("taxes").value;
	interest = interest/100;
	interest = interest/12;
	var output = "";

	var amort = 1.0*value/period;
	var total = 0;
	for (var i = 1; i <= period; i++) {
		var payment = amort + value*interest + taxes*1.0;
		value = value - amort;
		total = total + payment;
		output = output + i + " - R$ " + payment.toFixed(2) + "<br/>";
	}
	output = output + "Total: R$ " + total.toFixed(2) + "<br/>";
	result.innerHTML = output;
}
