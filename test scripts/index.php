<?php
$servername = "localhost";
$username = "root";
$password = "";
$db = "alien";

// Create connection
$conn = new mysqli($servername, $username, $password, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";

$sql = "SELECT article FROM stories";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo $row["article"]. "<br><br><br><br><br>";
    }
} else {
    echo "0 results";
}
$conn->close();
?>
