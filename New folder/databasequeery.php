

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


 mysqli_select_db($conn,"ds_db2");
 $result = mysqli_query($conn,"SELECT DATABASE()");
 $row = mysqli_fetch_row($result);
 



$sql_data_display = "SELECT  FirstN, Lastn, HouseNum, Addresss, Address2, City, County, PostCode, ContactNum FROM dateschool";  

     if (mysqli_query($conn, $sql_data_display)){
        $connection_data = mysqli_query($conn, $sql_data_display);
        $data = array(); 
        while ($row_users = mysqli_fetch_assoc($connection_data)){
             array_push($data,$row_users);     
        }
         echo json_encode($data); } 
      
     else {
         echo "error Entering data: " . mysqli_error($conn);
         die('could not enter data. ' );
     }
     mysqli_close($conn);

     
      
      
    ?>
    
    
    

