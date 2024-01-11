#Celery 
from celery import Celery
from flask import Flask, request
from flask_cors import CORS
import db_tools


app = Flask(__name__)

simple_app = Celery('simple_worker', broker="redis://redis:6379/0", backend="redis://redis:6379/0")
CORS(app)


@app.route("/API/v1.0/anketa_soiskatel", methods=['POST',])
def send_anketa_soiskatel():

    if request.method == "POST":
      db_tools.update_soiskatel_number()
      anket_number = db_tools.get_soiskatel_number()

      dataFormDict = {
          "surname": request.form["surname"], "name": request.form["name"], "patronymic": request.form["patronymic"],
          "age": request.form["age"], "email": request.form["email"], "mailArea": request.form["mailArea"], 
          "mailRegistration": request.form["mailRegistration"], "mobilePhone": request.form["mobilePhone"],
          "dreamJob": request.form["dreamJob"], "family": request.form["family"], "childrens": request.form["childrens"], 
          "education": request.form["education"], "nameInstitution": request.form["nameInstitution"],
          "possibilityOfRelocation": request.form["possibilityOfRelocation"], "needForHousing": request.form["needForHousing"],
          "desiredSalaryLevel": request.form["desiredSalaryLevel"], "generalExperience": request.form["generalExperience"],
          "positionAtLastJob": request.form["positionAtLastJob"], "additionalInf": request.form["additionalInf"], 
          "anket_number": anket_number, "summary": request.files["summary"].read(), "summaryName": request.files["summary"].filename 
      }

      r = simple_app.send_task('tasks.send_email_soiskatel', kwargs={'dataFormDict': dataFormDict})
      app.logger.info(r.backend)
      return "Status OK", 200
    else: 
      return "Method Not Allowed", 405
    

@app.route("/API/v1.0/anketa_employer", methods=['POST',])
def send_anketa_employer():
    if request.method == "POST":
        db_tools.update_employer_number()
        anket_number = db_tools.get_employer_number()

        dataFormDict = {
            "nameCompany": request.form["nameCompany"], "Address": request.form["Address"], "contact": request.form["contact"],
            "phoneNumber": request.form["phoneNumber"], "email": request.form["email"], "anket_number": anket_number,
            "Vacancies": request.files["Vacancies"].read(), "VacanciesName":request.files["Vacancies"].filename, 
            "CompanyCard": request.files["CompanyCard"].read(), "CompanyCardName": request.files["CompanyCard"].filename
        }

        r = simple_app.send_task('tasks.send_email_employer', kwargs={'dataFormDict': dataFormDict})
        app.logger.info(r.backend)
        return "Status Ok", 200
    else:
        return "Method Not Allowed", 405


if __name__ == "__main__":
    app.run(debug=False)