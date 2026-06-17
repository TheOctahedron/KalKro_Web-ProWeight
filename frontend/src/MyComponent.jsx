html = """ 
    <!DOCTYPE html>  <!-- CREATE HTML5 -->
    <html> <!-- START HTML-DOCUMENT -->
    <head>
        <title>Kalkro Web</title>
    </head>
    <body>
        <div style="text-align: center;">
            <img src="static/kalkro_icone1.png" alt="KalKro logo" width="300">
        </div>
        <h1 style="text-align: center;">Welcome to KalKro 2.1</h1>   <!-- [style="text-align: center;"]  SEND TEXT TO THE CENTER -->
        <p style="text-align: center;">Text-Based OS simulator</p>
        <p><br>'!Go' - Let's register!<br></p>
        <button id="GoButton">Go></button>
        <input type="text" id="userInput">
        <div id="output"></div>
        <script>
            const box = document.getElementById('output');
            const button = document.getElementById('GoButton');
            const us_input = document.getElementById('userInput')
            
            box.innerHTML = "<br><br>Enter Your Name: "
            button.onclick = function() {
                const us_answer = us_input.value;
            }

        </script>
        <div id="input"></div>

    </body>  
    </html> <!-- END HTML-DOCUMENT -->
""" 
