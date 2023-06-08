// ==UserScript==
// @name         AutoATT-CHUMoodle
// @namespace    http://tampermonkey.net/
// @version      0.2
// @description  try to take over the world!
// @author       YK
// @match        https://moodle.chu.edu.tw/mod/attendance/view.php?id=*
// @icon         https://moodle.chu.edu.tw/theme/image.php/chu/theme/1685412700/favicon
// @grant        none
// ==/UserScript==

(function() 
{
  setTimeout(function()
  {
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
	 break;
      }
    }
  },1000);
  setTimeout(function(){
	location.reload();
  },15000);
    // Your code here...
})();
