Youtube_Downloader


This is a simple program that allows me download the audio from any Youtube video, load it into a S3 and email a
pre-signed link to my friends
















This is a Python script that uses the tkinter, boto3, pytube, and smtplib modules to create a simple program that allows the user to download the audio from a YouTube video, upload it to an S3 bucket, and email a pre-signed link to a recipient.

The program consists of several functions that are responsible for different tasks:

Link_Download(): This function takes the URL of a YouTube video entered into an Entry widget (entry_yt), downloads the video using the pytube module, saves it locally as an .mp4 file, and calls the S3_File_Upload() function to upload the file to an S3 bucket.

S3_File_Upload(): This function takes the name of the locally saved file, uploads it to an S3 bucket using the boto3 module, and generates a pre-signed URL for the file that expires in 10 minutes. It then calls the Mailer() function to email the pre-signed URL to a recipient.

Mailer(): This function takes the recipient's email address entered into an Entry widget (entry_email) and the pre-signed URL generated in the S3_File_Upload() function. It uses the smtplib module to send an email containing the pre-signed URL to the recipient's email address.

The root object is an instance of the Tk class from the tkinter module, which creates a GUI window with a title and dimensions set by the title() and geometry() methods. The Label and Entry widgets are used to display and input the YouTube video URL and recipient's email address. The Button widget is used to initiate the download and email process when clicked, using the Link_Download() function as the command.

The bucket_name variable is set to the name of the S3 bucket to which the file will be uploaded.




https://user-images.githubusercontent.com/52922101/224924330-a7f58d93-7a13-405e-a019-64dc28004d3c.mov






![image](https://user-images.githubusercontent.com/52922101/217215324-c6092ee6-6f3f-4bb4-beec-ac35f5b4304b.png)




![image](https://user-images.githubusercontent.com/52922101/217215567-7ae5d761-d343-488e-8b9f-03f0c2e015d4.png)









Things to do:

Make it easier for others to use 
 -	Remove Personal env variables

Fix Title Bug 
 - If a youtube title have a “|” or maybe a “(“ the application won't finish


Exception Handling
 - There are no errors if/when actions don’t work    
