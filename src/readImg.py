import selenium


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome("chromedriver")




'''
<div class="performance_2d_sparkline graph ng-isolate-scope ng-scope" x-data-percent-change-day="ticker.pct_chge_1D" x-sparkline="watchlistData.sparklineData[ticker.ticker]">
  <span class="inlinesparkline ng-binding">
    <canvas width="100" height="40" style="display: inline-block; width: 100px; height: 40px; vertical-align: top;">
    </canvas>
  </span>
</div>



<body>
        <div style="position: absolute; left: 0; right: 0; top: 0; bottom: 0; background-color: black">
            <label style="color: #444444; font: bold 42px sans-serif; position: absolute; top: 84px; left: 84px ">Bloomberg</label>
            <label style="color: white; font: bold 42px sans-serif; position: absolute; top: 80px; left: 80px ">Bloomberg</label>

            <label id="hackLogo" style="color: red; font: 36px Segoe Script; position: absolute; top: 76px; left: 80px; transform: rotate(-45deg) ">Hack</label>
            <label id="atLogo" style="color: red; font: 36px Segoe Script; position: absolute; top: 50px; left: 170px;">@</label>
            <label id="timestamp" style="color: white; font: 24px monospace; position: absolute; top: 140px; left: 130px;">00:09:42</label>

            <div id="leaderboard" style="position: absolute; left: 10px; bottom: 10px; width: 376px; top: 200px ;border: 3px solid darkgray; overflow-y: auto"><table style="width: 100%"><tbody><tr><th colspan="3" style="color: white; text-align: left">Player</th><th style="color: white; text-align: right">Score</th></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship14.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">06</label></td><td style="text-align: left"><label style="color:orange; font: monospace">Name</label></td><td style="text-align: right"><label style="color:orange; font: monospace">100923</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship19.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">12</label></td><td style="text-align: left"><label style="color:orange; font: monospace">KingKong</label></td><td style="text-align: right"><label style="color:orange; font: monospace">66222</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship13.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">05</label></td><td style="text-align: left"><label style="color:orange; font: monospace">taqueria</label></td><td style="text-align: right"><label style="color:orange; font: monospace">30117</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship0.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">01</label></td><td style="text-align: left"><label style="color:orange; font: monospace">a</label></td><td style="text-align: right"><label style="color:orange; font: monospace">6239</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship16.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">02</label></td><td style="text-align: left"><label style="color:orange; font: monospace">BSOD</label></td><td style="text-align: right"><label style="color:orange; font: monospace">5837</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship4.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">ElectricBoogalo</label></td><td style="text-align: right"><label style="color:orange; font: monospace">3935</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship15.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">DJ-W</label></td><td style="text-align: right"><label style="color:orange; font: monospace">600</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship7.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">g</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship8.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">Dan.And.Jon</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship9.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">h</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship1.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">b</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship11.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">MemeTeam</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship5.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">e</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship3.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">d</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship2.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">c</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship10.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">SunnbrElla</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship6.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">f</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship17.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">sustorm</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width: 100%; background-color: rgb(32, 32, 32);"><td style="text-align: left; width: 12px"><img src="ship18.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">SuperZhengBrothers</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr><tr style="width:100%"><td style="text-align: left; width: 12px"><img src="ship12.png" style="width: 12px; height: 12px"></td><td style="text-align: center" ;="" width:="" 14px=""><label style="color:orange; font: monospace">00</label></td><td style="text-align: left"><label style="color:orange; font: monospace">gordon</label></td><td style="text-align: right"><label style="color:orange; font: monospace">0</label></td></tr></tbody></table></div>

            <div style="position: absolute; right: 10px; top: 10px; bottom: 10px; left: 400px; border: 3px solid darkgray">
                <canvas id="gameCanvas" style="position: absolute; width: 100%; height: 100%" width="1024" height="1024"></canvas>
            </div>
        </div>
    

</body>




<div style="position: absolute; right: 10px; top: 10px; bottom: 10px; left: 400px; border: 3px solid darkgray">
    <canvas id="gameCanvas" style="position: absolute; width: 100%; height: 100%" width="1024" height="1024"></canvas>
</div>

'''


driver.get("http://codebb.cloudapp.net/BaseInvaders.html")

images = driver.find_elements_by_tag_name('gameCanvas')

# get the base64 representation of the canvas image (the part substring(21) is for removing the padding "data:image/png;base64")
base64_image = driver.execute_script("return document.querySelector('.gameCanvas canvas');")

# decode the base64 image
output_image = base64.b64decode(base64_image)

# save to the output image
with open("image.png", 'wb') as f:
   f.write(output_image)

