from flask import Flask

aplicacion = Flask (__name__)

@aplicacion.route("/")
def raiz():
    return '''
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Texto gradiente</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@600;800&display=swap" rel="stylesheet">
  <style>
    :root{ --bg-1: #0b1220; --bg-2: #071026; --stable-color: #E6F0FF; }
    *{box-sizing:border-box}
    html,body{height:100%;}
    body{
      margin:0;
      min-height:100vh;
      display:flex;
      flex-direction:column;
      align-items:center;
      justify-content:flex-start;
      background: linear-gradient(135deg,var(--bg-1),var(--bg-2));
      font-family: 'Inter', system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
      color:var(--stable-color);
      padding:4vh 2rem;
    }

    .hero{
      display:flex;
      align-items:center;
      justify-content:center;
      width:100%;
      margin-bottom:3vh;
    }

    h1{
      margin:0;
      font-weight:800;
      font-size:clamp(2.5rem, 8vw, 6rem);
      line-height:1;
      text-align:center;
      letter-spacing:-0.02em;
      padding:0 1rem;
      background: linear-gradient(90deg,#ff7a18 0%, #ff3cac 40%, #7a00ff 70%, #00d4ff 100%);
      background-size:200% 200%;
      -webkit-background-clip: text;
      background-clip: text;
      color: transparent;
      animation: moveGradient 6s linear infinite;
      text-shadow: 0 8px 30px rgba(0,0,0,0.45);
    }

    @keyframes moveGradient{
      0%{background-position:0% 50%}
      50%{background-position:100% 50%}
      100%{background-position:0% 50%}
    }

    .list-wrapper{
      width:100%;
      max-width:880px;
      background: rgba(255,255,255,0.02);
      border-radius:14px;
      padding:1.25rem 1.5rem;
      box-shadow: 0 10px 30px rgba(0,0,0,0.45);
    }

    table{
      width:100%;
      border-collapse:collapse;
      font-weight:600;
      font-size:clamp(1rem, 2.2vw, 1.25rem);
      line-height:1.6;
      color:var(--stable-color);
    }

    thead th{
      text-align:left;
      padding:0.5rem;
      background:rgba(255,255,255,0.08);
    }

    tbody td{
      padding:0.5rem;
      border-bottom:1px solid rgba(255,255,255,0.08);
    }

    tbody tr:nth-child(even){
      background:rgba(255,255,255,0.03);
    }

    tbody tr:hover{
      background:rgba(255,255,255,0.08);
    }

    @media (min-width:1600px){
      h1{font-size:7rem}
    }
  </style>
</head>
<body>
  <div class="hero">
    <h1>Вероничка у меня:</h1>
  </div>

  <div class="list-wrapper">
    <table>
      <thead>
        <tr>
          <th>Number</th>
          <th>Text</th>
        </tr>
      </thead>
      <tbody>
        <!-- Filas de 1 a 30 con espacio para texto -->
        <tr><td>1</td><td>самая красивая</td></tr>
        <tr><td>2</td><td>самая умная</td></tr>
        <tr><td>3</td><td>самая мудрая</td></tr>
        <tr><td>4</td><td>самая сексуальная</td></tr>
        <tr><td>5</td><td>самая заботливая</td></tr>
        <tr><td>6</td><td>самая добрая</td></tr>
        <tr><td>7</td><td>самая нежная</td></tr>
        <tr><td>8</td><td>самая ласковая</td></tr>
        <tr><td>9</td><td>самая милая</td></tr>
        <tr><td>10</td><td>самая веселая</td></tr>
        <tr><td>11</td><td>самая жизнерадостная</td></tr>
        <tr><td>12</td><td>самая харизматичная</td></tr>
        <tr><td>13</td><td>самая талантливая</td></tr>
        <tr><td>14</td><td>самая сильная</td></tr>
        <tr><td>15</td><td>самая смелая</td></tr>
        <tr><td>16</td><td>самая верная</td></tr>
        <tr><td>17</td><td>самая искренняя</td></tr>
        <tr><td>18</td><td>самая честная</td></tr>
        <tr><td>19</td><td>самая трудолюбивая no ne vsegda ;)</td></tr>
        <tr><td>20</td><td>самая терпеливая</td></tr>
        <tr><td>21</td><td>самая элегантная</td></tr>
        <tr><td>22</td><td>самая стильная</td></tr>
        <tr><td>23</td><td>самая обаятельная</td></tr>
        <tr><td>24</td><td>самая очаровательная</td></tr>
        <tr><td>25</td><td>самая привлекательная</td></tr>
        <tr><td>26</td><td>самая фантастическая</td></tr>
        <tr><td>27</td><td>неповторимая</td></tr>
        <tr><td>28</td><td>самая удивительная</td></tr>
        <tr><td>29</td><td>самая великолепная</td></tr>
        <tr><td>30</td><td>SLAY</td></tr>
      </tbody>
    </table>
  </div>

</body>
</html>
'''

if __name__ == "__main__":
    aplicacion.run(debug=True)