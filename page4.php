<!DOCTYPE html>
<html>
<style>

form{
	margin:auto;
}
body{
	background-color: #4DB8FF;
}
.center{
	
    margin: auto;
    width: 60%;
    border: 3px double #73AD21;
    padding: 10px;
}

</style>
<h1></h1>
<body>
	<div class="center">
	<h1 align = "center"> Congratulations !</h1>
    
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
</div>
</body>
</html>