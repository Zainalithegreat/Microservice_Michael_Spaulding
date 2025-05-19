How to programmatically receive data from this microservice?
Use ZeroMQ socket to send JSON string
-  Address ("london, England)
-  Start Day (1)
-  Start Month (1)
-  Start Year (2019)
-  End Day (1)
-  End Month (1)
-  End Year (2023)

For Example here we are going to request data
 ![image](https://github.com/user-attachments/assets/af541d0e-7a40-480b-8f51-cb8a48433725)

Here we provide address(London, England), Start Day(1), Start Month(1), Start Year(2019), End Day(1), End Month (1), and End Year(2023). 

After sending this JSON string, the server responds with the average temperature between the start date and the end date.

![image](https://github.com/user-attachments/assets/a24636ba-1d28-4265-9f8e-bbd661ed91ca)

Receiving Data
After providing the address(London, England), Start Day(1), Start Month(1), Start Year(2019), End Day(1), End Month (1), and End Year(2023).
-  If the microservice succeeds, then it will print success with the location and average temperature in Celsius
-  If the microservice fails, then it will print an error, location not found.

Success Example

![image](https://github.com/user-attachments/assets/04a91fa5-a7cc-427a-8f40-140f001d61c8)


Fail Example

![image](https://github.com/user-attachments/assets/d0d2c6a6-46a8-48bc-baf2-e5905e941523)

Example Call
![image](https://github.com/user-attachments/assets/59c4ab89-d16d-4c3f-a598-6711cc524605)
