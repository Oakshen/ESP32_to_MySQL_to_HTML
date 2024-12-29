<?php

$servername = "localhost";
$username = "xxxx";
$password = "xxxxxxx";
$dbname = "Load_status";
 
// 创建连接
$conn = mysqli_connect($servername, $username, $password,$dbname);
 
// 检测连接
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT sta FROM load2 WHERE id=1";//选取保存在MySQL里用电器1的状态
$result = mysqli_query($conn, $sql);//用mysqli_query获取你想要的数据

while($row = mysqli_fetch_row($result)) {//将获取到数据用数组保存起来
    if($row[0]==1)
    {
        $jus='open';
        echo $jus;//如果用电器开着的话就输出open字符串（主要是配合我改CSS的className）
    }else{
        $jus='close';
        echo $jus;//关闭就输出close字符串
    }
}
mysqli_close($conn);
?>
