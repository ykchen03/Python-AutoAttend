// ==UserScript==
// @name         AutoATT-ZuvioIRS
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       YK
// @match        https://irs.zuvio.com.tw/student5/irs/rollcall/*
// @icon         https://s3.hicloud.net.tw/zuvio.public/public/system/images/irs_v4/favicon/student5.ico
// @grant        none
// ==/UserScript==
document.querySelector("#content .irs-rollcall .text").textContent = "自動點名啟動中";
setTimeout(function() {
    console.log(rollcall_id);
    if (rollcall_id != '') {
        makeRollcall(rollcall_id);
    }
}, 3000);
setTimeout(function() {
    window.location.reload();
}, 12000);
