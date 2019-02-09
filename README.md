# Web_map

Module generates .html file, that can create map with population and films' filming locations.
<h2>Installation<br></h>

You need to install everything from <b>requirements.txt</b> file via command
~~~~
sudo pip install -r  requirements.txt
~~~~
<h2>Usage<br></h>

Start the application<br>
~~~~
python3 web_map.py
~~~~
You will need to enter year to generate map with films for that year.

In case of<br><i>__geopy.exc.GeocoderQuotaExceeded: HTTP Error 429: Too Many Requests__</i><br>
try to change your WI-Fi network or use VPN service

Then you will get <b>Map_{year}.html</b>

<h2> HTML file description<br></h2>

first tag `<!DOCTYPE HTML>` directly define that file type is html5<br>
`<head>` contains all technique information of the document<br>
`<meta>` contains an <i>meta</i> tags, which contain information for browsers and search systems<br> 
`<script>` contains references to program or its text<br>
`<link>`  sets connection with external documents<br>
`<style>` defines styles of elements of the page<br>
`<body>` contains all maintain of web-page. In this case is short because all is performed in script<br>
After this file contains code to generate the map itself.

<h2> Conclusion<br></h2>
We can use Python based frameworks like <b>folium</b> to generate .html files for our web applications. It is simple and fast to use, so it can be effective instrument in development.
