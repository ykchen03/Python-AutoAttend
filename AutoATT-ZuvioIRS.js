// ==UserScript==
// @name         AutoATT-ZuvioIRS
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       YK
// @match        https://irs.zuvio.com.tw/student5/irs/rollcall/*
// @icon         https://s3.hicloud.net.tw/zuvio.public/public/system/images/irs_v4/favicon/student5.ico
// @require      https://code.jquery.com/jquery-3.7.1.min.js
// @grant        none
// ==/UserScript==
/*global $*/
$().ready(function() {
	console.log("ready");
	$("#content .irs-rollcall .text").text("自動點名啟動中").css({
		"color": "green",
		"font-weight": "bold",
		"font-size": "40px"
	});
	if ($("#submit-make-rollcall").length > 1) {
		new Function($("#submit-make-rollcall").attr("onclick"))();
	}
	setTimeout(function() {
		window.location.reload();
	}, 12000);
});
