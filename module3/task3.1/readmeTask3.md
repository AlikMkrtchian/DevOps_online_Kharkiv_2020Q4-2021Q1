# Task 3.1
 ## Base scheme
![Image_](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module3/task3.1/plan.png)

## Adding and creating a user
> GRANT [SELECT] ON [BikeMaster]. [*] TO ‘alik@'127.0.0.1’;

![Image_](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module3/task3.1/createtable.png)
![Image_](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module3/task3.1/userdatabase.png)
![Image_](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module3/task3.1/mytableend.png)
 ## Connection to AWS
![Image_](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module3/task3.1/connectamazondate.png)
 ## Transferring the local base to rds
![Image_](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module3/task3.1/migrationdatabase.png)
## DynamoDb
![Image_](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module3/task3.1/DynamoDB.png ) 
  ## An example of queries to databases that I write at work
  >SELECT data::json->>'pcl' from archived_order;(postgres)
![Image_](https://github.com/AlikMkrtchian/DevOps_online_Kharkiv_2020Q4-2021Q1/blob/master/module3/task3.1/example%20knowledge%20in%20queries.png)
