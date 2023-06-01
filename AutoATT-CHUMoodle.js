// ==UserScript==
// @name         AutoATT-CHUMoodle
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       YK
// @match        https://moodle.chu.edu.tw/mod/attendance/view.php?id=*
// @icon         https://moodle.chu.edu.tw/theme/image.php/chu/theme/1685412700/favicon
// @grant        none
// ==/UserScript==

(function() {
    var flag = false;
    if (document.readyState == "complete" || document.readyState == "loaded" || document.readyState == "interactive") {
        console.log("1");
        var title = document.createElement('h1');
        title.textContent = "自動點名啟動中";
        title.style.color='green';
        document.getElementsByClassName("page-header-headings")[0].appendChild(title);
        var button = document.getElementsByClassName("btn btn-primary");
        for(var i of button)
        {
            if(i.hasAttribute("href"))
            {
                console.log(i);
                window.location.href=i.href;
                flag = true;
                //alert("點名完成");
                break;
            }
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
