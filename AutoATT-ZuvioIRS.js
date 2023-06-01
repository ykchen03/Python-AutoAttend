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

(function() {
	var flag = false;
    if (document.readyState == "complete" || document.readyState == "loaded" || document.readyState == "interactive") 
       var title = document.getElementsByClassName("text")[0];
        title.textContent = "自動點名啟動中";
        title.style.color = "MediumSeaGreen";
        title.style.fontSize = "30px";
        var button = document.getElementById("submit-make-rollcall");
        if(button)
        {
            button.click();
			flag = true;
            return;
        }
    }

	if(!flag)
	{
		const refreshInterval = setInterval(function(){
			location.reload();
		},15000);
	}

    // Your code here...
})();
