import os
import ssl
import sys
from datetime import date, datetime
from email.base64mime import body_encode
from socket import *

from PyQt5 import QtWidgets

from mail import Ui_Form


def get_week_day(date):
    week_day = {
        0: '星期一',
        1: '星期二',
        2: '星期三',
        3: '星期四',
        4: '星期五',
        5: '星期六',
        6: '星期天',
    }
    day = date.weekday()  # weekday()可以获得是星期几
    return week_day[day]


s = "各位收信取信网友大家好，今天是" + str(str(date.today().strftime("%Y年%m月%d日")) + ' ' + get_week_day(date.today()))


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.resize(400, 300)
        self.setupUi(self)
        self.label_6.setText(s)
        self.lineEdit_2.setEchoMode(2)  # 设置为密码表示形式

    def buttonsend(self):
        try:
            fromAddress = self.lineEdit.text()
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            toAddress = [addr.strip() for addr in self.lineEdit_3.text().split(';')]
            subject = self.lineEdit_4.text()
            text = self.textEdit.toPlainText()

            mailServer = "smtp.qq.com"

            serverPort = 465  # SMTP使用465号端口

            CA_FILE = 'key/ca.crt'
            KEY_FILE = "key/client.key"
            CERT_FILE = "key/client.crt"

            context = ssl.SSLContext(purpose=ssl.PROTOCOL_TLS_CLIENT)  # 实现加密功能
            context.check_hostname = False
            context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
            context.load_verify_locations(CA_FILE)

            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect((mailServer, serverPort))  # connect只能接收一个参数

            clientSocket = context.wrap_socket(sock, server_hostname=mailServer)

            # 从客户套接字中接收信息
            recv = clientSocket.recv(1024).decode()
            print(recv)
            if '220' != recv[:3]:
                print('220 reply not received from server.')
                raise Exception('服务器连接失败')

            heloCommand = 'HELO MyName\r\n'
            clientSocket.send(heloCommand.encode())  # 随时注意对信息编码和解码
            recv1 = clientSocket.recv(1024).decode()
            print(recv1)
            if '250' != recv1[:3]:
                print('250 reply not received from server.')
                raise Exception('服务器连接失败')

            # 发送"AUTH PLAIN"命令，验证身份.服务器将返回状态码334（服务器等待用户输入验证信息）
            user_pass_encode64 = body_encode(f"\0{username}\0{password}".encode('ascii'), eol='')
            clientSocket.sendall(f'AUTH PLAIN {user_pass_encode64}\r\n'.encode())
            recv2 = clientSocket.recv(1024).decode()
            print(recv2)
            if '235' != recv2[:3]:
                print('235 reply not received from server.')
                raise Exception('请输入正确的用户名的密码！')

            clientSocket.sendall(('MAIL FROM: <' + fromAddress + '>\r\n').encode())
            recv3 = clientSocket.recv(1024).decode()
            print(recv3)
            if '250' != recv3[:3]:
                print('250 reply not received from server.')
                raise Exception('发件地址配置失败')

            for addr in toAddress:
                clientSocket.sendall(('RCPT TO: <' + addr + '>\r\n').encode())
                recv4 = clientSocket.recv(1024).decode()
                self.label_8.setText(recv4)
                if '250' != recv4[:3]:
                    print('250 reply not received from server.')
                    raise Exception('收件地址配置失败')

            clientSocket.send('DATA\r\n'.encode())
            recv5 = clientSocket.recv(1024).decode()
            print(recv5)
            if '354' != recv5[:3]:
                print('354 reply not received from server.')
                raise Exception('消息传输失败')

            message = 'from:' + fromAddress + '\r\n'
            for addr in toAddress:
                message += 'to:' + addr + '\r\n'
            message += 'subject:' + subject + '\r\n'
            message += '\r\n' + text
            endMsg = "\r\n.\r\n"

            clientSocket.sendall(message.encode())
            clientSocket.sendall(endMsg.encode())
            recv6 = clientSocket.recv(1024).decode()
            print(recv6)
            if '250' != recv6[:3]:
                print('250 reply not received from server.')
                raise Exception('邮件内容发送失败')

            clientSocket.sendall('QUIT\r\n'.encode())
            recv7 = clientSocket.recv(1024).decode()
            print(recv7)
            self.label_8.setText(recv7)
            if '221' != recv7[:3]:
                print('221 reply not received from server.')
                raise Exception('未正确退出')

            clientSocket.close()

            self.label_8.setText('邮件发送成功！')

            f = open('sent.txt', 'a+')
            f.write('\n')
            f.write(str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')) + '\n')
            f.write('from:<' + fromAddress + '>\n')
            for addr in toAddress:
                f.write('to:  <' + addr + '>\n')
            f.write('subject:' + subject + '\n')
            f.write(text)
            f.write('\n\n')
            f.write('------------------------')
            f.close()

        except Exception as e:
            print(e)
            self.label_8.setText(str(e))

    def savepass(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if len(username) == 0:
            print(1)
            self.label_8.setText("请输入用户名")
        elif len(password) == 0:
            print(2)
            self.label_8.setText("请输入密码")
        else:
            print(3)
            f = open('user-pass.txt', 'w')
            f.write(username)
            f.write('\n')
            f.write(password)
            self.label_8.setText("保存密码成功")
            f.close()

    def loadpass(self):
        if os.path.getsize('user-pass.txt') == 0:
            self.label_8.setText("未保存用户密码")
        else:
            f = open('user-pass.txt', 'r')
            username = f.readline()
            password = f.readline()
            username = username[0:len(username) - 1]
            self.lineEdit.setText(username)
            self.lineEdit_2.setText(password)
            self.label_8.setText("载入用户名密码成功")
            f.close()

    def savedraft(self):
        f = open('draft.txt', "w")
        f.write(self.lineEdit_4.text())
        f.write('\n\n')
        f.write(self.textEdit.toPlainText())
        self.label_8.setText("草稿保存成功")
        f.close()

    def loaddraft(self):
        if os.path.getsize('user-pass.txt') == 0:
            self.label_8.setText("草稿箱为空")
        else:
            f = open('draft.txt', "r")
            subject = f.readline()
            subject=subject[0:len(subject)-1]
            self.lineEdit_4.setText(subject)
            content = f.read()
            content = content[1:len(content)]
            self.textEdit.setText(content)
            self.label_8.setText("草稿载入成功")
            f.close()

    def clear(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.textEdit.setText('')
        self.label_8.setText('撤销邮件成功')

    def addcontacts(self):
        if self.lineEdit_3.text() == '':
            self.label_8.setText('请输入联系人')
        else:
            toAddress = [addr.strip() for addr in self.lineEdit_3.text().split(';')]
            count = 0
            rep = 0
            for newcont in toAddress:
                f = open('contacts.txt', 'r')
                contacts = f.readlines()
                flag = False
                for item in contacts:
                    if newcont == item[0:len(item) - 1]:
                        flag = True
                        rep += 1
                        break
                if not flag:
                    f = open('contacts.txt', 'a+')
                    f.write(newcont)
                    f.write('\n')
                    count += 1
                    f.close()
                f.close()
            if rep == 0 and count != 0:
                self.label_8.setText('成功添加' + str(count) + '个联系人')
            elif count != 0:
                self.label_8.setText('成功添加' + str(count) + '个联系人,其中' + str(rep) + '个联系人已经存在')
            else:
                self.label_8.setText('所有联系人都已经存在！')

    def sent(self):
        os.startfile('sent.txt')

    def contacts(self):
        os.startfile('contacts.txt')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
