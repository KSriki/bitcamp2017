<!DOCTYPE html>
<html>
<style>

button {
    background-color: #3b5998;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 30%;
}

body{
	background-color: #8CE8BA;
    width: 10px
    height: 10px;
    margin: auto;
}

.twitter{
	background-color: CYAN;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    cursor: pointer;
    width: 30%;

}

.center{
	
    margin: auto;
    width: 60%;
    border: 3px ridge #73AD21;
    padding: 10px;
}

</style>
<h1></h1>
<body>
	<div class = "center"> 
		<h1 align = "center"><u> <i>Welcome</i></u> </h1>

<?php
	session_start();
	require_once("pivot.php");
	unset($_SESSION['personName']);
	$body = "";
	// superglobals are not accessible in heredoc
	$scriptName = $_SERVER["PHP_SELF"];
	$topPart = <<<EOBODY
		<form action="page4.php" method="post">
		<h3 align = center> <strong>Select Person: </strong><input type="text" name="personName" required/></h3>
		<h4 align = center> <button type="button" name = "fb" class="Log in with facebook">Sign in to Facebook</button>
        <h4 align = center> <input type="button"  class = "twitter" value="Sign in to twitter"></button>
   
			
			<!--We need the submit button-->
		<h4 align = center>	<input type="submit" name="exterminate" /></h4><br><br>
		
		</form>		
EOBODY;
	$body = $topPart.$body;
	
	$page = generatePage($body);
	echo $page;

?>
</div>
</body>
</html>