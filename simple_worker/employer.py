from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from dotenv import load_dotenv
import os


load_dotenv()


class DataForm(object):

    FROM_EMAIL = os.getenv("FROM_EMAIL")
    TO_EMAIL = os.getenv("TO_EMAIL")
    APP_PASS_MAIL = os.getenv("APP_PASS_MAIL")
    TO_ZAN_CHECK_MAIL = os.getenv("TO_ZAN_CHECK_MAIL")
    TO_MAIL_CHECK_MAIL = os.getenv("TO_MAIL_CHECK_MAIL")
    TO_MAIL_CHECK_ADMIN = os.getenv("TO_MAIL_CHECK_ADMIN")
    BCC = [TO_ZAN_CHECK_MAIL, TO_MAIL_CHECK_MAIL]
    recipients = [TO_ZAN_CHECK_MAIL, TO_MAIL_CHECK_MAIL, TO_EMAIL]

    def __init__(self, dictForm: dict):
        self.nameCompany = dictForm["nameCompany"]
        self.Address = dictForm["Address"]
        self.contact = dictForm["contact"]
        self.phoneNumber = dictForm["phoneNumber"]
        self.email = dictForm["email"]
        self.anket_number = dictForm["anket_number"]
        self.Vacancies = dictForm["Vacancies"]
        self.VacanciesName = dictForm["VacanciesName"]
        self.CompanyCard = dictForm["CompanyCard"]
        self.CompanyCardName = dictForm["CompanyCardName"]


def send_to_employer(dataForm: DataForm):
    msg_for_sender = MIMEMultipart()
    msg_for_sender['From'] = dataForm.FROM_EMAIL
    msg_for_sender['To'] = dataForm.email
    msg_for_sender['Subject'] = "Спасибо за участие в проекте «Курс на Север»!"
    body = '''<!DOCTYPE html  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"  xmlns:o="urn:schemas-microsoft-com:office:office" lang="ru"><head>  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />  <meta http-equiv="X-UA-Compatible" content="IE=edge" />  <meta name="viewport" content="width=device-width, initial-scale=1.0" />  <!-- <meta name="color-scheme" content="light dark" />  <meta name="supported-color-schemes" content="light dark" /> -->  <title>KursNaSever</title>  <style type="text/css">    /* @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap'); */    @font-face {        font-family: "CorkiRegular";        font-style: normal;        font-weight: 400;        src: url('https://murman-zan-api.site/materials/CorkiRegular.ttf') format('truetype')    }    @font-face {        font-family: "Montserrat-Medium";        font-style: normal;        font-weight: 400;        src: url('https://murman-zan-api.site/materials/Montserrat-Medium.ttf') format('truetype')    }    table {      border-spacing: 0;      mso-cellspacing: 0;      mso-padding-alt: 0;    }    td {      padding: 0;    }    #outlook a {      padding: 0;    }    a {      text-decoration: none;      color: #e8fbfa;      font-size: 16px;    }    @media screen and (max-width: 599.98px) {}    @media screen and (max-width: 399.98px) {      .mobile-padding {        padding-right: 10px !important;        padding-left: 10px !important;      }      .mobile-col-padding {        padding-right: 0 !important;        padding-left: 0 !important;      }      .two-columns .column {        width: 100% !important;        max-width: 100% !important;      }      .two-columns .column img {        width: 100% !important;        max-width: 100% !important;      }      .three-columns .column {        width: 100% !important;        max-width: 100% !important;      }      .three-columns .column img {        width: 100% !important;        max-width: 100% !important;      }    }    /* Custom Dark Mode Colors */    /* :root {      color-scheme: light dark;      supported-color-schemes: light dark;    }    @media (prefers-color-scheme: dark) {      table,      td {        background-color: #06080B !important;      }      h1,      h2,      h3,      p {        color: #ffffff !important;      }    } */  </style>  <!--[if (gte mso 9)|(IE)]>    <style type="text/css">      table {border-collapse: collapse !important;}    </style>  <![endif]-->  <!--[if (gte mso 9)|(IE)]>  <xml>    <o:OfficeDocumentSettings>      <o:AllowPNG/>      <o:PixelsPerInch>96</o:PixelsPerInch>  </o:OfficeDocumentSettings>  </xml>  <![endif]--></head><body style="Margin:0;padding:0;min-width:100%;background-color:#dde0e1;">  <!--[if (gte mso 9)|(IE)]>      <style type="text/css">         body {background-color: #dde0e1!important;}         body, table, td, p, a {font-family: sans-serif, Arial, Helvetica!important;}      </style>   <![endif]-->  <center style="width: 100%;table-layout:fixed;background-color: #dde0e1;padding-top: 40px;padding-bottom: 40px;">    <div style="max-width: 600px;background-color: #fafdfe;box-shadow: 0 0 10px rgba(0, 0, 0, .2);">      <!-- Preheader (remove comment) -->      <div        style="font-size: 0px;color: #fafdfe;line-height: 1px;mso-line-height-rule:exactly;display: none;max-width: 0px;max-height: 0px;opacity: 0;overflow: hidden;mso-hide:all;">        Стартовое описание      </div>      <!-- End Preheader (remove comment) -->      <!--[if (gte mso 9)|(IE)]>        <table width="600" align="center" border="0" cellspacing="0" cellpadding="0" role="presentation"          style="color:#1C1E23;">        <tr>        <td>      <![endif]-->      <table align="center" border="0" cellspacing="0" cellpadding="0" role="presentation"        style="color:#1C1E23; font-family: 'CorkiRegular';background-color: #fafdfe;Margin:0;padding:0;width: 100%;max-width: 600px;"        >            <!-- Logo -->            <tr>                <td>                    <table align="center" border="0" cellspacing="0" cellpadding="0" role="presentation">                        <tr>                            <td style="padding: 19px 0 10px 0; text-align: center;">                                <a href="https://kursnasever51.ru" target="_blank">                                    <img src="https://murman-zan-api.site/materials/logo.png" alt="KursNaSever Logo" border="0" width="200">                                </a>                            </td>                        </tr>                    </table>                </td>            </tr>            <!-- End Logo -->            <!-- Hero -->            <tr>                <td>                    <table align="center" border="0" cellspacing="0" cellpadding="0" role="presentation">                        <tr>                            <td style="padding: 19px 0 19px 0;">                                <p align="center" style="margin: 0; color: #1B4E9B; font-size: 24px;">                                    Спасибо за участие в проекте «Курс на Север» Мурманская область!                                </p>                            </td>                        </tr>                        <tr>                            <td style="padding: 5px 0 2px 0;">                                <p align="center" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                                    Ваша заявка на участие в проекте «Курс на Север»                                 </p>                            </td>                        </tr>                        <tr>                            <td style="padding: 2px 0 5px 0;">                                <p align="center" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                                    зарегистрирована под номером <strong>''' +f'{dataForm.anket_number}' + '''</strong>                                </p>                            </td>                        </tr>                        <tr>                            <td style="padding: 10px 0 19px 0;">                                <p align="center" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 14px; color: #696969">                                    С Вами свяжется специалист службы сопровождения в течении 5 рабочих дней.                                </p>                             </td>                        </tr>                        <tr>                            <td align="center">                                <img src="https://murman-zan-api.site/materials/town_with_road.png" alt="Murman Photo" border="0" style="width: 100%; max-width: 552px;">                            </td>                        </tr>                        <tr>                            <td style="padding: 19px 0 5px 0;">                                <p align="center" style="margin: 0; color: #1B4E9B; font-family: 'CorkiRegular'; font-size: 24px;">                                    Вы также можете ознакомиться с новостями проекта «Курс на Север»!                                </p>                            </td>                        </tr>                        <tr>                            <td align="center" style="padding: 5px 0 19px 0;">                                <a href="https://kursnasever51.ru/news" target="_blank">                                    <img src="https://murman-zan-api.site/materials/button_news.png" alt="See News" border="0" style="width: 100%; max-width: 350px;">                                </a>                            </td>                        </tr>                        <tr>                            <td style="padding: 10px 0 19px 0;">                                <p align="center" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 14px; color: #696969">                                    Это автоматическая рассылка. Пожалуйста, не надо отвечать на это письмо.                                </p>                            </td>                        </tr>                    </table>                </td>            </tr>            <!-- End Hero -->      </table>      <!--[if (gte mso 9)|(IE)]>        </td>        </tr>        </table>      <![endif]-->    </div>  </center></body></html>'''

    msg_for_sender.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)

    server.login(dataForm.FROM_EMAIL, dataForm.APP_PASS_MAIL)

    text = msg_for_sender.as_string()
    server.sendmail(dataForm.FROM_EMAIL, dataForm.email, text)
    server.quit()


def send_to_KursNaSever(dataForm: DataForm):
    msg = MIMEMultipart()
    msg['From'] = dataForm.FROM_EMAIL
    msg['To'] = dataForm.TO_EMAIL
    msg['Subject'] = f"Заявка работодателя №{dataForm.anket_number}"
    msg['BCC'] = ", ".join(dataForm.BCC) 
    body = '''<!DOCTYPE html  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml"  xmlns:o="urn:schemas-microsoft-com:office:office" lang="ru"><head>  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />  <meta http-equiv="X-UA-Compatible" content="IE=edge" />  <meta name="viewport" content="width=device-width, initial-scale=1.0" />  <!-- <meta name="color-scheme" content="light dark" />  <meta name="supported-color-schemes" content="light dark" /> -->  <title>KursNaSever</title>  <style type="text/css">    /* @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap'); */    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');    @font-face {        font-family: "CorkiRegular";        font-style: normal;        font-weight: 400;        src: url('https://murman-zan-api.site/materials/CorkiRegular.ttf') format('truetype')    }    @font-face {        font-family: "Montserrat-Medium";        font-style: normal;        font-weight: 400;        src: url('https://murman-zan-api.site/materials/Montserrat-Medium.ttf') format('truetype')    }    table {      border-spacing: 0;      mso-cellspacing: 0;      mso-padding-alt: 0;    }    td {      padding: 0;    }    #outlook a {      padding: 0;    }    a {      text-decoration: none;      color: #e8fbfa;      font-size: 16px;    }    @media screen and (max-width: 599.98px) {}    @media screen and (max-width: 399.98px) {      .mobile-padding {        padding-right: 10px !important;        padding-left: 10px !important;      }      .mobile-col-padding {        padding-right: 0 !important;        padding-left: 0 !important;      }      .two-columns .column {        width: 100% !important;        max-width: 100% !important;      }      .two-columns .column img {        width: 100% !important;        max-width: 100% !important;      }      .three-columns .column {        width: 100% !important;        max-width: 100% !important;      }      .three-columns .column img {        width: 100% !important;        max-width: 100% !important;      }    }    /* Custom Dark Mode Colors */    /* :root {      color-scheme: light dark;      supported-color-schemes: light dark;    }    @media (prefers-color-scheme: dark) {      table,      td {        background-color: #06080B !important;      }      h1,      h2,      h3,      p {        color: #ffffff !important;      }    } */  </style>  <!--[if (gte mso 9)|(IE)]>    <style type="text/css">      table {border-collapse: collapse !important;}    </style>  <![endif]-->  <!--[if (gte mso 9)|(IE)]>  <xml>    <o:OfficeDocumentSettings>      <o:AllowPNG/>      <o:PixelsPerInch>96</o:PixelsPerInch>  </o:OfficeDocumentSettings>  </xml>  <![endif]--></head><body style="Margin:0;padding:0;min-width:100%;background-color:#dde0e1;">  <!--[if (gte mso 9)|(IE)]>      <style type="text/css">         body {background-color: #dde0e1!important;}         body, table, td, p, a {font-family: sans-serif, Arial, Helvetica!important;}      </style>   <![endif]-->  <center style="width: 100%;table-layout:fixed;background-color: #dde0e1;padding-top: 40px;padding-bottom: 40px;">    <div style="max-width: 600px;background-color: #fafdfe;box-shadow: 0 0 10px rgba(0, 0, 0, .2);">      <!-- Preheader (remove comment) -->      <div        style="font-size: 0px;color: #fafdfe;line-height: 1px;mso-line-height-rule:exactly;display: none;max-width: 0px;max-height: 0px;opacity: 0;overflow: hidden;mso-hide:all;">        Стартовое описание      </div>      <!-- End Preheader (remove comment) -->      <!--[if (gte mso 9)|(IE)]>        <table width="600" align="center" border="0" cellspacing="0" cellpadding="0" role="presentation"          style="color:#1C1E23;">        <tr>        <td>      <![endif]-->      <table align="center" border="0" cellspacing="0" cellpadding="0" role="presentation"        style="color:#1C1E23; font-family: 'Montserrat', sans-serif, ;background-color: #fafdfe;Margin:0;padding:0;width: 100%;max-width: 600px;"        >            <!-- Logo -->            <tr>                <td>                    <table align="center" border="0" cellspacing="0" cellpadding="0" role="presentation">                        <tr>                            <td style="padding: 19px 0 10px 0; text-align: center;">                                <a href="https://kursnasever51.ru" target="_blank">                                    <img src="https://murman-zan-api.site/materials/logo.png" alt="KursNaSever Logo" border="0" width="200">                                </a>                            </td>                        </tr>                    </table>                </td>            </tr>            <!-- End Logo -->            <!-- Hero -->            <tr>                <td>                    <table align="center" border="0" cellspacing="0" cellpadding="0" role="presentation">                        <tr>                            <td style="padding: 19px 0 19px 0;">                                <p align="center" style="margin: 0; color: #1B4E9B; font-size: 24px; font-family: 'CorkiRegular'">                                  Зарегистрирована заявка работодателя на участие в проекте «Курс на Север» Мурманская область                                </p>                            </td>                        </tr>                        <tr>                            <td style="padding: 5px 0 5px 0;">                                <p align="center" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                                  ''' + f'<strong>№{dataForm.anket_number}</strong>' + '''                                </p>                            </td>                        </tr>                        <tr>                            <td style="padding: 5px 0 5px 20px;">                                <p align="left" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                                  ''' +f'Полное наименование: <strong>{dataForm.nameCompany}</strong>' + '''                                </p>                            </td>                        </tr>                        <tr>                          <td style="padding: 5px 0 5px 20px;">                            <p  align="left" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                              ''' + f'Юридеский адрес: <strong>{dataForm.Address}</strong>' + '''                            </p>                          </td>                        </tr>                        <tr>                          <td style="padding: 5px 0 5px 20px;">                            <p  align="left" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                              ''' + f'ФИО контактного лица: <strong>{dataForm.contact}</strong>' + '''                            </p>                          </td>                        </tr>                        <tr>                          <td style="padding: 5px 0 5px 20px;">                            <p  align="left" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                              ''' + f'Номер телефона: <strong>{dataForm.phoneNumber}</strong>' + '''                            </p>                          </td>                        </tr>                        <tr>                          <td style="padding: 5px 0 5px 20px;">                            <p  align="left" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                              ''' + f'Электронный адрес: <strong>{dataForm.email}</strong>' + '''                            </p>                          </td>                        </tr>                                              <tr>                          <td style="padding: 5px 0 5px 20px;">                            <p  align="left" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 15px;">                              Документы приложеннные к обращению во вложении.                            </p>                          </td>                        </tr>                        <tr>                            <td style="padding: 10px 0 19px 0;">                                <p align="center" style="margin: 0; font-family: 'Montserrat-Medium'; font-size: 14px; color: #696969">                                    Это автоматическая рассылка. Пожалуйста, не надо отвечать на это письмо.                                </p>                            </td>                        </tr>                    </table>                </td>            </tr>            <!-- End Hero -->      </table>      <!--[if (gte mso 9)|(IE)]>        </td>        </tr>        </table>      <![endif]-->    </div>  </center></body></html>'''
    
    msg.attach(MIMEText(body, 'html'))

    if dataForm.Vacancies != "":
        part = MIMEBase('application', 'octet-stream')

        part.set_payload(dataForm.Vacancies)
        encoders.encode_base64(part)

        part.add_header('Content-Disposition', 'attachment', filename=dataForm.VacanciesName)

        msg.attach(part)

    if dataForm.CompanyCard != "":
        part = MIMEBase('application', 'octet-stream')

        part.set_payload(dataForm.CompanyCard)
        encoders.encode_base64(part)

        part.add_header('Content-Disposition', 'attachment', filename=dataForm.CompanyCardName)

        msg.attach(part)


    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(dataForm.FROM_EMAIL, dataForm.APP_PASS_MAIL)

    text = msg.as_string()
    server.sendmail(dataForm.FROM_EMAIL, dataForm.recipients, text)
    server.quit()