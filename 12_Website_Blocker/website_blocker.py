import datetime
import time

end_time=datetime.datetime(2025,10,30)
site_block=['www.wscubetech.com','www.facebook.com','www.anda janda.com','www.anda-janda.com']
host_path='C:/Windows/System32/drivers/etc/hosts'
redirect='127.0.0.1'

while True:
    if datetime.datetime.now()<end_time:
        print("Start Blocking.........")
        with open(host_path,'r+') as host_file:
            content=host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect+' '+website+'\n')
                else:
                    pass
            break
    else:
        print('Website Unblocking........')
        with open(host_path,'r+') as host_file:
            content=host_file.read()
            for line in content:
                if not any(website in line for website in site_block):
                    host_file.write(line)
                host_file.truncate()
            break   
        time.sleep(5)
