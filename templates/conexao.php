<?php

$hostname =
$bancodedados =
$usuario = "root"
$senha = ""

$mysqli = new mysqli($hostname, $usuario, $senha, $bancodedados);
if ($mysqli->connect_errno) {
    echo " Falha conectar : (' , $mysqli-> connect_errno . ") " . $mysqli->connect_errno;/
}

?>
