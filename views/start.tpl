<!DOCTYPE html>
<html>
<head>
<style>h1 {
    color: black;
    background: rgb(168, 130, 240);
    border: 3px solid #cccccc;
    box-shadow: 6px 7px rgba(95, 100, 156, 0.904);
}</style>
<meta charset="UTF-8">
<title>マイクラサーバー参加登録</title>
<meta name="description" content="Minecraftサーバー「{{servername}}」に入るのに必要な登録をします。">
<meta property="og:description" content="Minecraftサーバー「{{servername}}」に入るのに必要な登録をします。">
<meta property="og:title" content="マイクラサーバー参加登録">
<meta name="theme-color" content="#800080">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=2">
<script src="{{js}}" async defer></script>
</head>

<body>
<h1>マイクラサーバー参加登録</h1>
<h2>Minecraft サーバー「{{servername}}」への参加登録はこちらから出来ます。</h2>
<h4><font color ="grey">使い方：<u>Java 版で参加するか統合版で参加するかを選択して</u>から、<br>下の MCID 欄に MCID (もしくはゲーマータグ)を入力してください。<br></font></h4>
<center>
<form method="post" action="{{authurl}}">
<label for="r1">Java版:</label>
<input type="radio" id="r1" name="mce" value="java">
<label for="r2">統合版:</label>
<input type="radio" id="r2" name="mce" value="be">

<br>
MCID:<input type="text" name="input_text" placeholder="MCID/ゲーマータグを入力"><br><br>
<div class="{{param}}" data-sitekey="{{rcsite}}"></div>
<p>注意：MCID は一つまでしか登録できませんので誤りが無いか、ご確認ください。</p>

<button type="submit">登録する</button></center>


  

</form><br>
<hr>
<center><a href="https://github.com/Budobudou/MCAuthWebElite/">MCAuthWebElite</a> by Budobudou v1.0</center>
</body>
</html>
