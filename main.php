<!DOCTYPE html>
<html>
<style>


input[type=text], input[type=password] {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px double #ccc;
    box-sizing: border-box;
}

body{
    background-color: #87CEFA ;
    width: 800px
    margin: auto;
}
button {
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 30%;
}

button:hover {
    opacity: 0.8;
}

.center{
    
    margin: auto;
    width: 60%;
    border: 3px double #73AD21;
    padding: 10px;
}

.cancelbtn {
    width: auto;
    padding: 10px 18px;
    background-color: #f44336;
}

.imgcontainer {
    text-align: center;
    margin: 1px 0 1px 0;
}

img.avatar {
    width: 10%;
    border-radius: 50%;
}

.container {
    padding: 0px;
}

span.psw {
    float: right;
    padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
    span.psw {
       display: block;
       float: none;
    }
    .cancelbtn {
       width: 100%;
    }
}
</style>
<h1></h1>
<body>
<div class = "center">
<h2 style="font-family:italic;" align = "center"><u><strong>EX-Terminator</u></strong></h2>

<form action="page2.php" method = "post">
  <div class="imgcontainer">
    <img src="imageBR.jpg" alt="Avatar" class="avatar">
  </div>

  <div class="container">
    <label><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>
    <input type="checkbox" checked="checked"> Remember me <br>
  <p align = "right"> <button type="submit" >Login</button></p>
</form>
Don't have an account yet?<a href = "page3.php"> Register Now</a><br>
    <strong><a href="#">Forgot password?</strong>
  </div>
</div>
  </body>
</html>
