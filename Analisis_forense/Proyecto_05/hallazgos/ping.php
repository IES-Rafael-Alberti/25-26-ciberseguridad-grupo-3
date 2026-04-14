<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8"/>
        <title>PING</title>
    </head>
    <body>
        <form action="ping.php" method="post" />
            <label for="ping">IP: </label><input type="text" name="ping" value="<?php echo(isset($_POST['ping']) ? $_POST['ping'] : ''); ?>" />
            <br/>
            <input type="submit" value="enviar" />
            <br/>
            <br/>
        <form/>
<?php

if (isset($_POST['ping'])) {
    echo(system('ping -c 1 ' . $_POST['ping']));
}

?>
    </body>
</html>
