// ==UserScript==
// @name         AutoATT-CHUMoodle
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       YK
// @match        https://moodle.chu.edu.tw/mod/attendance/view.php?id=*
// @icon         https://moodle.chu.edu.tw/theme/image.php/chu/theme/1685412700/favicon
// @require      https://code.jquery.com/jquery-3.7.1.min.js
// @grant        none
// ==/UserScript==
/*global $*/
$().ready(function() {
    console.log("ready");
    $("#page-header .page-header-headings h1").text("自動點名啟動中").css({
        "color": "green",
        "font-weight": "bold"
    });
    if ($("#region-main .btn.btn-primary").length > 0) {
        window.location.href = $("#region-main .btn.btn-primary").attr("href");
    }
    setTimeout(function() {
        window.location.reload();
    }, 12000);
});
