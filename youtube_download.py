from tkinter import *
import boto3
from pytube import YouTube
import smtplib
import time



#This is a simple program that allows me download the audio from any Youtube video, load it into a S3 and email a
# pre-signed link to my friends

#AWS SERVICES S3 & Parameter Store Used
#While this version can be retrofitted  for anyone an easier more up to date version will be created soon.



#Downloads the link that was put into ""entry_yt"and saves locally
def Link_Download():
    link = entry_yt.get()
    yt = YouTube(link)
    title = yt.title
    object_name=title+".mp4"
    stream = yt.streams.get_by_itag(139)
    stream.download(filename=str(object_name))
    S3_File_Upload(object_name)



#Takes locally saved file and uploads it into the "sonic19659171" bucket (which is not public) and creates a pre_signed_link
def S3_File_Upload(object_name):

    s3 = boto3.client('s3')

    with open(object_name, "rb") as data:
        s3.upload_fileobj(data, bucket_name, object_name)
        pre_signed_link = s3.generate_presigned_url(

            'get_object',

             Params={'Bucket': bucket_name,

            'Key': object_name},

            ExpiresIn=600)
        Mailer(entry_email.get(),pre_signed_link)



#Using "entry_email" as the recipient email and the pre-signed url made in the S3_File_Upload function. This function emails the link
def Mailer(rep,pre_link):
    s3_ssm = boto3.client('ssm')
    parameter = s3_ssm.get_parameter(Name='maileruser', WithDecryption=True)
    email_user = (parameter['Parameter']['Value'])
    parameter = s3_ssm.get_parameter(Name='mailerpass', WithDecryption=True)
    email_pass = (parameter['Parameter']['Value'])
    subjects = ["Your download is ready!"]
    bodys = ["Your link will expire in 10 minutes:\n\n" +" "+pre_link]

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(email_user, email_pass)
        for subject, body in zip(subjects, bodys):
            time.sleep(3)
            msg = f'Subject:{subject}\n\n{body}'
            smtp.sendmail(email_user, rep, msg)
            print("E-mail Sent")






root =Tk()
root.title("Youtube Downloader")
root.geometry("550x80")
label_yt=Label(text="Youtube URL").grid(row=1,column=0)
label_email=Label(text="E-mail").grid(row=0,column=0)
bucket_name="sonic19659171"
entry_yt=Entry(width=80)
entry_email=Entry(width=80)
entry_email.grid(row=0,column=1)
entry_yt.grid(row=1,column=1)
Download_yt=Button(text="E-Mail Download Link",command=Link_Download).grid(row=2,column=1)

mainloop()
