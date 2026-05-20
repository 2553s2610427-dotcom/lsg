<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>점심 추천기</title>

  <style>
    body {
      font-family: sans-serif;
      background: #f5f5f5;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .card {
      background: white;
      padding: 40px;
      border-radius: 20px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.1);
      text-align: center;
      width: 320px;
    }

    h1 {
      margin-bottom: 20px;
    }

    #menu {
      font-size: 28px;
      font-weight: bold;
      margin: 30px 0;
      color: #ff5722;
      min-height: 40px;
    }

    button {
      border: none;
      background: #ff5722;
      color: white;
      padding: 14px 24px;
      border-radius: 10px;
      font-size: 16px;
      cursor: pointer;
      transition: 0.2s;
    }

    button:hover {
      background: #e64a19;
      transform: scale(1.05);
    }
  </style>
</head>
<body>

  <div class="card">
    <h1>🍱 오늘 점심 추천</h1>

    <div id="menu">버튼 눌러봐</div>

    <button onclick="pickLunch()">
      추천 받기
    </button>
  </div>

  <script>
    const lunches = [
      "김치찌개",
      "제육볶음",
      "돈까스",
      "국밥",
      "햄버거",
      "초밥",
      "쌀국수",
      "마라탕",
      "비빔밥",
      "치킨"
    ];

    function pickLunch() {
      const random = Math.floor(Math.random() * lunches.length);

      document.getElementById("menu").innerText =
        lunches[random];
    }
  </script>

</body>
</html>
