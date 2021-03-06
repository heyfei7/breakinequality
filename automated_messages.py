from twilio.rest import TwilioRestClient
from twilio import twiml
import datetime

account_sid = "AC0bdf8036e6590c7833e0766423192f3f"
auth_token = "4f9a0e84bbee241ea73ad380f9255925"
n = "6476949837"
client = TwilioRestClient(account_sid, auth_token)

phone_book ={"Fei":"6472333048",
            "Anupya":"6479940655",
            "He Yue":"5195888188",
            "Fizaa":"",
            "Ankita":"5197814838",
            "Shreya":""}

weekly_symptoms={1:{"Physical":"Vomiting, nausea, Gas, Constipation, Mood-swings",
                    "Tips":"Cut out alcohol, cigarettes, any illegal or recreational drug"},
                 2:{"Physical":"A missed period, tender breasts, feeling nauseous, increased vaginal discharge",
                    "Tips":"Be sure to visit the doctor, Cut out alcohol, cigarettes, any illegal or recreational drug"},
                 3:{"Physical":"Vaginal bleeding (not to be mistaken for a period)",
                    "Tips":"Be sure to visit the doctor, Cut out alcohol, cigarettes, any illegal or recreational drug"},
                 4:{"Physical":"mood swings, intense food cravings, morning sickness",
                    "Tips":"Be sure to visit the doctor, Cut out alcohol, cigarettes, any illegal or recreational drug"},
                 5:{"Physical":"Missed menstrual period. Tender breasts, cramping, nausea and fatigue",
                    "Tips":"Be sure to visit the doctor, Cut out alcohol, cigarettes, any illegal or recreational drug"},
                 6:{"Physical":"mood swings, intense food cravings, morning sickness, weight gain, fatigue, sickness",
                    "Tips":"Be sure to visit the doctor, Cut out alcohol, cigarettes, any illegal or recreational drug"},
                 7:{"Physical":"aches, pains, headache, fatigue, morning sickness",
                    "Tips":"Be sure to visit the doctor, Cut out alcohol, cigarettes, any illegal or recreational drug"},
                 8:{"Physical":"morning sickness, rising hormone levels, fatigue, difficulty sleeping, heartburn, frequently urinating",
                    "Tips":"have your first panetral checkup with a midwife, check urine sample"},
                 9:{"Physical":"nausea or vomiting ,frequent urination,tender or tingly breasts, fatigue,dizziness,irritability or unexpected emotions,heartburn or constipation,food aversions or cravings,increased hunger",
                    "Tips":"Drink plenty of water and eat high fiber foods to combat constipation. Stand up slowly, don't skip meals, avoid standing in place for too long"},
                 10:{"Physical":"version, indigestion, fatigue , heartburn , vomiting",
                     "Tips":"go check with the doctor, if the vaginal discharge has foul order, green or yellow colour, mixed with blood, redness of itching of the vulva"},
                 11:{"Physical":"eartburn, soring of enlarged breasts",
                     "Tips":"Call the doctor, if you experience vaginal bleeding as well as fever, blurred vision, heachache and abdominal pain"},
                 12:{"Physical":"constant urge to urinate ends,super tender breasts and nipples, food aversions, fatigue, breast aereolas become darker",
                     "Tips":"Ice packs, cool cabbage leaves, or bags of frozen peas on your chest while you lie down may also offer some relief. Look for small, silicone-filled breast soothing products that you can keep in the refrigerator and wear inside your bra"},
                 13:{"Physical":"constiplation",
                     "Tips":"c"},
                 14:{"Physical":"Decreasing Fatigue, Continued Breast Growth, less tenderness, an end to nausea and vomiting, increasing appetite, stuffy nose, Varicose Veins",
                     "Tips":"If new moles appear, get them evaluated by the doctor. Stay away from from sick people, wash hands regualrly, dont share drinks, toothbrushes etc."},
                 15:{"Physical":"Body aches, tingling in the hands and feet. Darkening of the skin around the nipples",
                     "Tips":"Consume extra calories : lean meats ,low-fat dairy,fruits,vegetables,whole grains"},
                 16:{"Physical":"Weight gain, Nasal Congestion, Increased Vaginal Discharge, Conspitation, Bleeding Gums, Backaches",
                     "Tips":"Drink saline water, add a humidifier in your room. Dont stand in one position for long streches"},
                 17:{"Physical":"Growing Appetite, Nasal Congestion",
                     "Tips":"Get the anatomical scan, take lean meat and low-fat dairy"},
                 18:{"Physical":"Growing Appetite, Snoring, Periodic pain in legs, loose teeth",
                     "Tips":"check up with a periodonitis. Use heating pad or back streches to ease the pain"},
                 19:{"Physical":"Round ligament pain, Hair loss",
                     "Tips":"Take ginger and peppermint, if round ligament pains last even after resting, contact your doctor"},
                 20:{"Physical":"Food cravings, Braxton-Hicks contractions",
                     "Tips":"Make sure to take the anatomical scan. Any strong, painful , or regular contractions could be signs of preterm birth"},
                 21:{"Physical":"week 21 physical symptoms",
                     "Tips":"week 21 Tips"},
                 22:{"Physical":"week 22 physical symptoms",
                     "Tips":"week 22 Tips"},
                 23:{"Physical":"week 23 physical symptoms",
                     "Tips":"week 23 Tips"},
                 24:{"Physical":"week 24 physical symptoms",
                     "Tips":"week 24 Tips"},
                 25:{"Physical":"week 25 physical symptoms",
                     "Tips":"week 25 Tips"},
                 26:{"Physical":"week 26 physical symptoms",
                     "Tips":"week 26 Tips"},
                 27:{"Physical":"week 27 physical symptoms",
                     "Tips":"week 27 Tips"},
                 28:{"Physical":"week 28 physical symptoms",
                     "Tips":"week 28 Tips"},
                 29:{"Physical":"week 29 physical symptoms",
                     "Tips":"week 29 Tips"},
                 30:{"Physical":"week 30 physical symptoms",
                     "Tips":"week 30 Tips"},
                 31:{"Physical":"week 31 physical symptoms",
                     "Tips":"week 31 Tips"},
                 32:{"Physical":"week 32 physical symptoms",
                     "Tips":"week 32 Tips"},
                 33:{"Physical":"week 33 physical symptoms",
                     "Tips":"week 33 Tips"},
                 34:{"Physical":"week 34 physical symptoms",
                     "Tips":"week 34 Tips"},
                 35:{"Physical":"week 35 physical symptoms",
                     "Tips":"week 35 Tips"},
                 36:{"Physical":"week 36 physical symptoms",
                     "Tips":"week 36 Tips"},
                 37:{"Physical":"week 37 physical symptoms",
                     "Tips":"week 37 Tips"},
                 38:{"Physical":"week 38 physical symptoms",
                     "Tips":"week 38 Tips"},
                 39:{"Physical":"week 39 physical symptoms",
                     "Tips":"week 39 Tips"},
                 40:{"Physical":"week 40 physical symptoms",
                     "Tips":"week 40 Tips"}}

def send_sms(number,msgs):
    for msg in msgs:
        if msg=="": continue
        elif "www" in msg:
            client.messages.create(
                to = number,
                from_ = n,
                body = "This is what your baby looks like:",
                media_url = msg,
                )
        else:
            client.messages.create(
                to = number,
                from_ = n,
                body = msg,
                )

def find_week_from_string(d):
    due_day = int(d[0:2])
    due_month = int(d[3:5])
    due_year = int(d[6:])
    
    duedate=datetime.date(due_year,due_month,due_day)
    today = datetime.date.today()
    
    difference = duedate-today
    days_elapsed = 280-difference.days
    week = (days_elapsed//7)+1

    return week

def find_week_info(duedate):
    today = datetime.date.today()
    difference = duedate-today
    days_elapsed = 280-difference.days
    week = (days_elapsed//7)+1

    welcome = "You are in week " + str(week) + " of your pregnancy!"
    symptoms = "Symptoms:\n"+weekly_symptoms[week]["Physical"]
    tips = "Tips:\n"+weekly_symptoms[week]["Tips"]
    if week==1:
        url="http://www.pregnancycorner.com/wp-content/uploads/1-week-pregnant.jpg"
    else:
        url="http://www.pregnancycorner.com/wp-content/uploads/"+str(week)+"-weeks-pregnant.jpg"
    return [welcome,symptoms,tips,url]

def send_weekly_message(duedate,number):
    week_info = find_week_info(duedate)
    send_sms(number,week_info)

def main(due_year,due_month,due_day,number):
    duedate=datetime.date(due_year,due_month,due_day)
    send_weekly_message(duedate,number)

def respond(sentence):
  words = sentence.split()
  if (("baby" in words) and (("move" in words) or ("moving" in words))):
      return "You can start to feel the baby's movement anytime from 16-22 weeks, " + \
            "and the baby may not move very frequently until 24 weeks. " + \
    "Though do contact us if the baby doesn't move everyday after 24 weeks. " \
    + "See more at " + \
    "http://blogs.webmd.com/womens-health/2015/10/babys-movement-during-pregnancy-whats-normal.html"
  if ("exercise" in words):
      return "You should definitely exercise during your pregnancy. " + \
             "At least 20 minutes of exercise with moderate intensity per day " + \
             "is recommend. " + "See more at " + \
             "http://www.babycenter.com/0_the-best-kinds-of-exercise-for-pregnancy_7880.bc"
  if (("nausea" in words) or ("nauseous" in words) or ("vomit" in words) or ("vomiting" in words)):
      return "Nausea and vomiting is common during pregnancy. " + \
             "It will not affect the health of your baby whether you have it or not. " + \
             "Just remember to stay hydrated. " + "See more at " + \
             "http://www.babycenter.com/morning-sickness?page=1"
  return "Sorry, no answer to your question is found, we are trying our best"  + \
         "to complete the database. " + \
         "In the meantime, please text # to talk to a doctor."

def question_response(number,sentence):
      msg=respond(sentence)
      send_sms(number,msg,"")
      
