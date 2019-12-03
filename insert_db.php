<?php
$args = $argv;
unset($args[0]);
$input = implode(' ', $args);

$db = new PDO('mysql:host=localhost;dbname=sayai', 'root', '');

$smt = $db->prepare("INSERT INTO sayings(text, `date`) VALUES(:saying, NOW())");

$smt->execute([
    'saying' => $input,
]);
