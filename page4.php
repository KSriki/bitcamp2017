<!DOCTYPE html>
<html>
<style>

form{
	margin:auto;
}
body{
	background-color: #4DB8FF;
}
</style>
<h1 align = "center"> Congratulations !</h1>
<body>
<?php
	session_start();
	require_once("pivot.php");
	$nameValue = trim($_POST["personName"]);
    echo "<h3 align = center>$nameValue has been terminated." ;
echo "<br> <br> <br>"; 
	    $body = "";
		
	
	// superglobals are not accessible in heredoc
	$scriptName = $_SERVER["PHP_SELF"];
	$topPart = <<<EOBODY
		<form action="page5.php" method="post">
			<!--We need the submit button-->
			<input type="submit"  name="undo" value = "Undo for $5" /><br><br>
		</form>		
EOBODY;
	$body = $topPart.$body;
	
	$page = generatePage($body);
	echo $page;
?>
</body>
</html>