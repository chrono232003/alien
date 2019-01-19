<?php
include 'connection.php';

$postData = file_get_contents("php://input");
$request = json_decode($postData);

$id = $request->storyId;
$statement = "SELECT * FROM stories WHERE id=$id";
$result = mysqli_query($con, $statement);

if ($result) {
header('Content-Type: application/json');
$rows = array();
while ($row = mysqli_fetch_assoc($result)) {
  $row['article'] = utf8_encode($row['article']);
  $row['article'] = str_replace("==","<br /><br />",$row['article']);
  $rows[] = $row;
}
echo json_encode($rows);
} else {
echo "No records Found";
}
?>
