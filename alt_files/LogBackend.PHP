<?php
session_start();

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  // Get the user's username and password from the form
  $username = $_POST["username"];
  $password = $_POST["password"];

  // TODO: Check the user's credentials against a database or other authentication mechanism
  if ($username == "exampleuser" && $password == "examplepassword") {
    // Login successful - store the user's information in the session and redirect to the dashboard page
    $_SESSION["username"] = $username;
    header("Location: dashboard.php");
    exit;
  } else {
    // Login failed - display an error message
    $error = "Invalid username or password";
  }
}
?>

<!DOCTYPE html>
<html>
  <head>
    <title>Login Page</title>
  </head>
  <body>
    <h2>Login Page</h2>
    <?php if (isset($error)) { echo "<p>$error</p>"; } ?>
    <form method="post" action="LogBackend.php">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username"><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password"><br><br>
      <input type="submit" value="Login">
    </form>
  </body>
</html>