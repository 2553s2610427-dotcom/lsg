<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>점심 추천</title>

  <style>
    body {
      margin: 0;
      height: 100;
      display: flex;
      justify-content: center;
      align-items: center;
      background: #f4f4f4;
      font-family: sans-serif;
    }

    .container {
      background: white;
      padding: 40;
      border-radius: 20px;
      text-align: center;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    h1 {
      margin-bottom: 20px;
    }

    #menu {
      font-size: 30px;
      color: tomato;
      margin: 20px 0;
    }

    button {
      padding: 12px 20px;
      border: none;
      border-radius: 10px;
      background: tomato;
      color: white;
      font-size: 16px;
      cursor: pointer;
    }

    button:hover {
      opacity: 0.8;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>🍱 오늘 점심</h1>

    <div id="menu">추천 받기</div>

    <button onclick="recommendMenu()">
      추천하기
    </button>
  </div>

  <script>
    const menus = [
      "김치찌개",
      "돈까스",
      "햄버거",
      "초밥",
      "제육볶음",
      "마라탕",
      "비빔밥",
      "국밥"
    ];

    function recommendMenu() {
      const random = Math.floor(Math.random() * menus.length);

      document.getElementById("menu").innerText =
        menus[random];
    }
  </script>

</body>
</html>
