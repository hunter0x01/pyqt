from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리
import schedule
import time
import smtplib
import datetime
from email.mime.text import MIMEText
import daemon




def job_checkTheSite():
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('window-size=1920x1080')
	options.add_argument("disable-gpu")
	options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
	options.add_argument("lang=ko_KR") # 한국어!
	driver = webdriver.Chrome(executable_path=r'/Users/steve/Downloads/chromedriver', options=options)
	#driver = webdriver.Chrome(executable_path=r'c:\util\chromedriver.exe', chrome_options=options)
	driver.implicitly_wait(1)

	 
	try:    # 정상 처리

		now = datetime.datetime.now()
		nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
		print(nowDatetime)
		with open('/tmp/echo.txt', 'a') as fh:
			fh.write("{}\n".format(nowDatetime))

		driver.get('https://learn.hoseo.edu')
		# 아이디/비밀번호를 입력해준다.
		driver.find_element_by_name('user_id').send_keys('1111')
		driver.find_element_by_name('password').send_keys('1111')
		driver.find_element_by_xpath('//*[@id="entry-login"]').click()
		# driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')
		# driver.get('http://google.com/')

	 
	# except TimeoutException:    # 예외 처리
	except Exception as e:

		recipients = ['ramiah@nate.com','hunter0x01@gmail.com']
		smtp = smtplib.SMTP('smtp.gmail.com', 587)
		smtp.ehlo()      # say Hello
		smtp.starttls()  # TLS 사용시 필요
		smtp.login('hunter0x01@gmail.com', '1111')

		msg = MIMEText('블랙보드 접속 및 예외사항이 발생했습니다.')
		msg['Subject'] = '블랙보드 예외가 발생하였습니다.'
		msg['To'] = ", ".join(recipients)
		smtp.sendmail('hunter0x01@gmail.com', 'hunter0x01@gmail.com', msg.as_string())
	 
		smtp.quit()
	 
	finally:    # 정상, 예외 둘 중 하나여도 반드시 실행
	    driver.quit()

# 5분마다 웹사이트를 점검합니다.
schedule.every(10).seconds.do(job_checkTheSite)


def main():
	try:

		while True: 
			schedule.run_pending() 
			time.sleep(1)

	except KeyboardInterrupt:
	    print('종료합니다!!')


with daemon.DaemonContext():
	main()


