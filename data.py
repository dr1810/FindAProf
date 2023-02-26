import sqlite3 as sq
import pandas as pd
import streamlit as st
con = sq.connect("Profs.db")
cur = con.cursor()
#cur.execute("create table prof(name varchar(255),friend int,qua int,comm int, pro int,type varchar(255),course varchar(255));")
file1 = pd.read_csv("C:\\Users\\dharu\\PycharmProjects\\Ureackathon\\professors.csv")
print(list(cur.execute("select * from prof where course='Fluid Dynamics';")))
