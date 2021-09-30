from ftplib import FTP
import ftplib
with ftplib.FTP('127.0.0.1') as ftp:
    print(ftp.getwelcome())
    ftp.login()
    ftp.cwd('test_folder')
    # ftp.delete('test')  

    # filename="test2.xml"
    # block_size = 128
    # myfile = open(filename, "rb")
    # ftp.storbinary("STOR " + 'test.xml', myfile)     # send the file
    # myfile.close()                                    # close file and FTP
    
    try:
        ftp.retrbinary("RETR " + 'test.xml' ,open('test4.xml', 'wb').write)
    except:
        print ("Error")

    ftp.quit()
