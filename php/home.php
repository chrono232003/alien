<?php
  include 'connection.php';

  $statement = "SELECT * FROM stories LIMIT 4";
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
