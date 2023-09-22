import ftplib
import os
from hijri_convert import convert
import Error_Handling

# Source FTP credentials
source_Host = 'IPAddress_HERE'
source_UNAME = 'UserNAME_HERE'
source_PASS = 'PASSWD_HERE'
source_port = 21

# Destinatoin FTP credentials
Dest_Host = 'IPAddress_HERE'
Dest_UNAME = 'UserNAME_HERE'
Dest_PASS = 'PASSWD_HERE'
Dest_PORT = 21

source_ftp = ftplib.FTP(source_Host, source_UNAME, source_PASS)
Dest_ftp = ftplib.FTP(Dest_Host, Dest_UNAME, Dest_PASS)

"""Local_and_Server_Path's"""
Local_path = "Path_Here"
Server_path = "Path_Here"


def Files_Transfer(source_FTP=source_ftp, Dest_FTP=Dest_ftp, photo_DIR_SOR=Local_path, photo_DIR_DES=Server_path):
    source_FTP.cwd(photo_DIR_SOR)
    source_data = source_FTP.nlst()

    Dest_FTP.cwd(photo_DIR_DES)

    # Enabling utf-8 encoding to use Arabic language
    Dest_FTP.sendcmd('OPTS UTF8 ON')
    source_FTP.sendcmd('OPTS UTF8 ON')

    for folders in source_data:
        source_FTP.cwd(photo_DIR_SOR + f"/{folders}")
        folder_Content = source_FTP.nlst()
        # print(folder_Content)

        # read the file.txt Data and append it to a list var
        lines = []
        source_FTP.retrlines('RETR file.txt', lines.append)
        file_name = str(lines[0])
        date = str(lines[1])
        name_of_lecturer = str(lines[2])
        other_lecturers = str(lines[3])
        event_type = str(lines[4])

        file_name = file_name.strip().split(":")[1]
        file_name = file_name.strip()
        date = date.split(":")[1]
        day = date.strip().split("-")[0]
        month = date.split("-")[1]
        year = date.split("-")[2]
        name_of_lecturer = name_of_lecturer.strip().split(":")[1]
        other_lecturers = other_lecturers.strip().split(":")[1]
        event_type = event_type.strip().split(":")[1]
        event_type = event_type.strip()

        # convert the Eng Date to Arab Date
        hijri_year, hijri_month, hijri_day = convert(int(year), int(month), int(day))
        hijri_year = str(hijri_year)
        year = year + '-' + hijri_year
        month = month + '-' + hijri_month

        # make DIR file system depending on the txt file Data
        if year in Dest_FTP.nlst():
            Dest_FTP.cwd(year)
        elif year not in Dest_FTP.nlst():
            Dest_FTP.mkd(year)
            Dest_FTP.cwd(year)
        if month in Dest_FTP.nlst():
            Dest_FTP.cwd(month)
        elif month not in Dest_FTP.nlst():
            Dest_FTP.mkd(month)
            Dest_FTP.cwd(month)
        if event_type in Dest_FTP.nlst():
            Dest_FTP.cwd(event_type)
        elif event_type not in Dest_FTP.nlst():
            Dest_FTP.mkd(event_type)
            Dest_FTP.cwd(event_type)
        if file_name in Dest_FTP.nlst():
            Dest_FTP.cwd(file_name)
        elif file_name not in Dest_FTP.nlst():
            Dest_FTP.mkd(file_name)
            Dest_FTP.cwd(file_name)

        # Transfer files from the source to the destination server
        for file in folder_Content:
            file_name = os.path.basename(file)
            with open(file_name, 'wb') as f:
                source_FTP.retrbinary('RETR ' + file_name, f.write)
            with open(file_name, 'rb') as f:
                Dest_FTP.storbinary('STOR ' + file_name, f)
            os.remove(file_name)
            print(f"Successed {file}")
        Dest_FTP.cwd(photo_DIR_DES)


try:
    Files_Transfer()
    source_ftp.quit()
    Dest_ftp.quit()
except Exception as error:
    Error_Handling.email_sending(error)
    Error_Handling.whatsapp_alert()
    print("There is Error")
