#Sends E-mail through G-mail to the specified people.
import smtplib


def send_email(from_addr, to_addr_list, cc_addr_list, subject, message, login, password, smtp='smtp.gmail.com:587'):
    #Fills out the header of the e-mail with the information.
    header = 'From: %s\n' % from_addr
    header += 'To %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
#At the moment this information is for GMAIL. Modification would be needed for other clients.
    server = smtplib.SMTP(smtp)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list,message)
    server.quit()
    return problems

#example call off the function

send_email(from_addr    = 'who the e-mail is from (sender)', 
          to_addr_list = ['To List'],
          cc_addr_list = ['Cc List'], 
          subject      = 'subject', 
          message      = 'Message text', 
          login        = 'G-mail name', 
          password     = 'password')











