<!DOCTYPE html>
<html>
<style>

body{
	background-color: #8CE8BA;
}
</style>
<h1 align = "center"> Welcome </h1>
<body>
<?php
	session_start();
	require_once("pivot.php");
	unset($_SESSION['personName']);
	$body = "";
	// superglobals are not accessible in heredoc
	$scriptName = $_SERVER["PHP_SELF"];
	$topPart = <<<EOBODY
		<form action="page4.php" method="post">
		<h3 align = center> <strong>Choose Person: </strong><input type="text" name="personName" /></h2>
			
			<!--We need the submit button-->
		<h4 align = center>	<input type="submit" name="exterminate" /></h4><br><br>
		</form>		
EOBODY;
	$body = $topPart.$body;
	
	$page = generatePage($body);
	echo $page;

?>
</body>
</html>