<!DOCTYPE html>
<html>
    <head>
        <title>PHP!</title>
    </head>

<body>

<?php
function test(){
    $colors = array("red", "green", "blue", "yellow"); 

    foreach ($colors as $value) {
    echo "$value <br>";
    }
}

test()
?>

</body>
</html>