import streamlit as st
import sqlite3 as sql
from tab1 import home_tab
from about import about_us
from app import app_work
from recommend import recomm
con = sql.connect("reviews.db")
curs = con.cursor()
st.title("FindAProf")
def reviews(tab4):
    tab4.title("Feedback")
    tab4.write("Your feedback is valuable to us. Give us your feedback and inputs on how we can improvise our application")
    name = tab4.text_input("Enter your name ")
    email = tab4.text_input("Enter your email id ")
    review = tab4.text_input("What do you think about our app and feedback")
    submit = tab4.button("Submit")
    if submit:
        curs.execute('insert into reviews values("{}","{}","{}")'.format(name,email,str(review)))
        con.commit()
        tab4.write("Thank You for your valuable feedback...")
home,recommend,work,abt,review = st.tabs(["Home","Our Recommender","How Does Our App Work","About Us","Reviews"])
home_tab(home)
reviews(review)
about_us(abt)
app_work(work)
recomm(recommend)
