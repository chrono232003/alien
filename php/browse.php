<?php
  include 'connection.php';

  $statement = "SELECT id, title, image FROM stories ORDER BY title";
  $result = mysqli_query($con, $statement);

if ($result) {
  header('Content-Type: application/json');
  $rows = array();
  while ($row = mysqli_fetch_assoc($result)) {
    $row['title'] = utf8_encode($row['title']);
    $rows[] = $row;
  }
  echo json_encode($rows);
} else {
  echo "No records Found";
}
?>
