<html>
    <head>
        <title>Hello, World</title>
</head>
<body>

    <?php 
$servername = "10.140.42.235";
$username = "DS";
$password = "password";
$port = "3307";
$database = "ds_db2";

$conn = mysqli_connect($servername,$username,$password,$database,$port);
if(mysqli_connect_errno()) {
    echo"Failed to connect to MSQLl " . mysqli_connect_error();
    exit();
}
else{
    echo "connection succesfull";
}


  $FirstN = $_POST['FirstN']; //Check the input is
 $LastN = $_POST['LastN']; //Check the input is
  $HouseNum = $_POST['HouseNum']; //Check the input is
 $Addresss = $_POST['Addresss']; //Check the input is
  $Address2 = $_POST['Address2']; //Check the input is
 $City = $_POST['City']; //Check the input is
   $County = $_POST['County']; //Check the input is
    $PostCode = $_POST['PostCode']; //Check the input is
   $ContactNum = $_POST['ContactNum']; //Check the input is

      $sql = "INSERT INTO dateschool ( FirstN, Lastn, HouseNum, Addresss, Address2, City, County, PostCode, ContactNum) VALUES
    ('$FirstN','$LastN','$HouseNum','$Addresss','$Address2','$City','$County','$PostCode','$ContactNum')";
     
     if (mysqli_query($conn, $sql)){
         echo "Data obtained Successfully";
        // echo mysqli_affected_rows($conn)."rows added successfull";
     } else {
         echo "error Entering data: " . mysqli_error($conn);
         die('could not enter data. ' );
     }
     mysqli_close($conn);

    
    ?>
    
    
</body>
    </html>
   
