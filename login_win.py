#coding=utf-8
import re
import time
import subprocess
import smtplib


def current_date():
    local_date = time.localtime()
    local_date=str(local_date[0])+str(local_date[1])+str(local_date[2])+str(local_date[3])\
                +str(local_date[4])
    return local_date


def failed():
    command = 'Get-EventLog -LogName Security -Source Microsoft-Windows-security-auditing \
    -EntryType FailureAudit -After (Get-Date).AddMinutes(-30)| fl'
    event=subprocess.Popen(['powershell',command],shell=True,stdout=subprocess.PIPE,\
                           stderr=subprocess.STDOUT)
    event = event.communicate()[0]
    return event


def success():
    command = 'Get-EventLog -LogName Security -Source Microsoft-Windows-security-auditing \
    -EntryType SuccessAudit -After (Get-Date).AddMinutes(-30)| fl'
    event=subprocess.Popen(['powershell',command],shell=True,stdout=subprocess.PIPE,\
                           stderr=subprocess.STDOUT)
    event = event.communicate()[0]
    return event


def get_account(event):
    rex = r'\t*Account Name:\s*(.*?)\r\n'
    account = re.findall(rex, event)
    set_account = set(account)
    account_count = {}
    for i in set_account:
        account_count[i] = 0
    for i in account:
        if i in account_count:
            account_count[i] += 1
    return account, account_count


def get_logon_time(event):
    rex = r'TimeWritten\s*:\s(.*?)\r\n'
    logon_time = re.findall(rex, event)
    return logon_time


def get_ip(event):
    rex = r'\t*Client Address:\s*(.*?)\r\n'
    ip = re.findall(rex, event)
    return ip


def write_csv(account, account_count, logon_time, ip, local_date):
    #account,account_count=get_account(event)
    #logon_time=get_logon_time(event)
    #ip=get_ip(event)

    if len(account) == len(logon_time) == len(ip):
        log_path = 'D:\\' + local_date + 'logon_detailed.csv'
        #log_detailed
        log_detailed = open(log_path, 'w+')
        for i in range(len(account)):
            content = account[i] + ',' + ip[i] + ',' + logon_time[i] + '\n'
            log_detailed.write(content)
        log_detailed.close()
    else:
        print "Error"
    log_path = 'D:\\' + local_date + 'logon_conut.csv'
    #logon_count
    log_count = open(log_path, 'w+')
    count = account_count.items()
    for i in count:
        #print i
        content = i[0] + ',' + str(i[1]) + '\n'
        log_count.write(content)
    log_count.close()


def send_mail(content):
    host = 'ip'
    user = 'xxx'
    passd = r'xx'
    sender = 'xx'
    receiver = 'xx'
    header = 'To:' + receiver + '\n' + 'From:' + sender + '\n' + 'Subject:Logon Monitor' + '\n'
    #content='test'
    message = header + '\n' + content + '\n'
    try:
        smtp_server = smtplib.SMTP()
        smtp_server.connect(host, 25)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(user, passd)
        smtp_server.sendmail(sender, receiver, message)
        smtp_server.close()
        print 'doen'
    except:
        pass


def notice(account_count):
    for m, n in account_count.items():
        if n >= 5:
            content = 'Alias: ' + m + ' ' * 3 + 'Failed(s): ' + str(n) + '\n'
            send_mail(content)
        else:
            pass


def test():
    event = failed()
    #print event
    account, account_count = get_account(event)
    logon_time = get_logon_time(event)
    ip = get_ip(event)
    local_date = current_date()
    write_csv(account, account_count, logon_time, ip, local_date)
    #notice(account_count)


if __name__ == '__main__':
    count = 0
    while 1:
        test()
        count += 1
        print count
        time.sleep(1200)