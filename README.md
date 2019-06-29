# Jump Ranking
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/57831edb0d864a0abf001ca94b97df14)](https://app.codacy.com/app/RDCH106/JumpRanking?utm_source=github.com&utm_medium=referral&utm_content=RDCH106/JumpRanking&utm_campaign=Badge_Grade_Dashboard)
[![License](https://img.shields.io/github/license/RDCH106/JumpRanking.svg)](https://github.com/RDCH106/JumpRanking/blob/master/LICENSE)

Simple Jump Ranking created using a REST service developed in Python and Web viewer developed in HTML and Javascript.

### What can I do with Jump Ranking?

* Run decoupled project with REST service and Web viewer
  + Run service in a server or cloud
  + Run Web viewer from repository or host the web in Apache server
* Use it as base project for bigger projects

<br>

### 🛠️ Installation
<hr>

#### 🤖 REST Service

Install service requirements using [requirements.txt](https://github.com/RDCH106/JumpRanking/blob/master/service/requirements.txt):

`pip install -r requirements.txt`

Run with and follow [linkero](https://github.com/ingran/linkero) instructions:

`python jumprankingAPI_main.py`

⚠️ REST service runs with Python2 and Python3

#### 👀 Web Viewer

Host Web viewer directly from GitHub with [raw.githack.com](https://github.com/neoascetic/rawgithack):

https://raw.githack.com/RDCH106/JumpRanking/master/web/jumpranking-viewer.html

Use [`http_server_with_cors.py`](https://github.com/RDCH106/JumpRanking/blob/master/web/http_server_with_cors.py) server included in the project behing a reverse proxy with SSl certificate. The server include CORS support.

Host in a traditional Apache server, Nginx... or that you want.

<br>

### REST Service 🔌 API
<hr>

Resgiters list access:

Verb (GET) - 🔓 No-Auth - Response (JSON)

https://your_host:port/jumpranking/api/v1/registers

💡 You can open it from the browser by entering the URL

<br><br>

Add register:

Verb (POST) - 🔐Auth - Response (JSON + HTTP 201 --> added)

https://your_host:port/jumpranking/api/v1/registers/\<username\>/\<height\>
  
💡 Replace `<username>` and `<height>` by desired values

⚠️ Requiered HTTP Basic Auth using User:Password or using [Token](https://github.com/ingran/linkero/wiki/usage)

<br><br>

Delete registers list:

Verb (DELETE) - 🔐Auth - Response (JSON + HTTP 204 --> deleted)

https://your_host:port/jumpranking/api/v1/registers 

⚠️ Requiered HTTP Basic Auth using User:Password or using [Token](https://github.com/ingran/linkero/wiki/usage)
