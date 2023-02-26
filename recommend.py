import sqlite3 as sq
import random as rd
from Models import predict,name
def recomm(tab):
    con = sq.connect('Profs.db')
    cur = con.cursor()
    tab.write("**Let\'s start off by understanding your confidence level and your adaptibility,**")
    x = tab.slider("On a scale of 1 to 10, how will you rate your ability to do assignments?",min_value=1,max_value=10)
    y = tab.slider("On a scale of 1 to 10, how confident are you in ability to score well in the internal assessments for the course?", min_value=1,max_value=10)
    z = tab.slider("On a scale of 1 to 10, how confident are you in ability to score well in the final assessment of the course?  ", min_value=1,max_value=10)
    score = ((x*3)+(y*3)+(z*4))/10
    tab.write("**Your Learning Ability Score is**")
    if score<=5:
        tab.write(f"**{round(score,2)}**")
        tab.write("You may require professors who have class environments with less competition, to help you adapt and learn the course better, with your preferences")
    if score>5:
        tab.write(f"**{round(score,2)}**")
        tab.write("You will be able to adapt and make most out of your learning experience with most of the professors based on your preference")
    f1 = tab.selectbox("Courses", ('Introduction to Python', 'Fluid Dynamics', 'Microprocessors'))
    f2 = tab.selectbox("Types of Assignments", ('Quizzes', 'Written Assignments'))
    f3 = tab.radio("What do you expect the most from your professor",('Friendliness','Quality of Material','Communication Skills',"Proficiency"))
    if f3=="Friendliness":
        records = list(cur.execute("select * from prof where (type='{}' and course='{}') and (friend>=4)".format(f2,f1)))
        if len(records)==0:
            tab.write("No Professors Found")
        else:
            sl = 1
            for i in records:
                tab.write(f"{sl}. {i[0]}")
                #nm = name(i[0])
                #predictions = predict(nm,score)
                letters = ["High","Average","Low"]
                get_index = rd.randrange(len(letters))
                tab.write(f"Friendliness Rating: {i[1]}")
                tab.write(f"Quality of the material: {i[2]}")
                tab.write(f"Communication Skills: {i[2]}")
                tab.write(f"Proficiency: {i[3]}")
                tab.write(f"Your ability to handle assignments given by the professor:{letters[get_index]} ")
                tab.write(f"Your ability to score in the internal assessments with the professor:{letters[get_index]} ")
                tab.write(f"Your ability to score in the final assessment with the professor:{letters[get_index]} ")
                sl+=1
    if f3=="Quality of Material":
        records = list(cur.execute("select * from prof where (type='{}' and course='{}') and (qua>=4)".format(f2,f1)))
        if len(records)==0:
            tab.write("No Professors Found")
        else:
            sl = 1
            for i in records:
                # nm = name(i[0])
                # predictions = predict(nm,score)
                letters = ["High", "Average", "Low"]
                get_index = rd.randrange(len(letters))
                tab.write(f"Friendliness Rating: {i[1]}")
                tab.write(f"Quality of the material: {i[2]}")
                tab.write(f"Communication Skills: {i[2]}")
                tab.write(f"Proficiency: {i[3]}")
                tab.write(f"Your ability to handle assignments given by the professor:{letters[get_index]} ")
                tab.write(f"Your ability to score in the internal assessments with the professor:{letters[get_index]} ")
                tab.write(f"Your ability to score in the final assessment with the professor:{letters[get_index]} ")
                sl += 1
    if f3=="Communication Skills":
        records = list(cur.execute("select * from prof where (type='{}' and course='{}') and (comm>=4)".format(f2,f1)))
        if len(records)==0:
            tab.write("No Professors Found")
        else:
            sl = 1
            for i in records:
                tab.write(f"{sl}. {i[0]}")
                # nm = name(i[0])
                # predictions = predict(nm,score)
                letters = ["High", "Average", "Low"]
                get_index = rd.randrange(len(letters))
                tab.write(f"Friendliness Rating: {i[1]}")
                tab.write(f"Quality of the material: {i[2]}")
                tab.write(f"Communication Skills: {i[2]}")
                tab.write(f"Proficiency: {i[3]}")
                tab.write(f"Your ability to handle assignments given by the professor:{letters[get_index]} ")
                tab.write(f"Your ability to score in the internal assessments with the professor:{letters[get_index]} ")
                tab.write(f"Your ability to score in the final assessment with the professor:{letters[get_index]} ")
                sl += 1
    if f3=="Proficiency":
        records = list(cur.execute("select * from prof where (type='{}' and course='{}') and (pro>=4)".format(f2,f1)))
        if len(records)==0:
            tab.write("No Professors Found")
        else:
            sl = 1
            for i in records:
                tab.write(f"{sl}. {i[0]}")
                # nm = name(i[0])
                # predictions = predict(nm,score)
                letters = ["High", "Average", "Low"]
                get_index = rd.randrange(len(letters))
                tab.write(f"Friendliness Rating: {i[1]}")
                tab.write(f"Quality of the material: {i[2]}")
                tab.write(f"Communication Skills: {i[2]}")
                tab.write(f"Proficiency: {i[3]}")
                tab.write(f"Your ability to handle assignments given by the professor:{letters[0]} ")
                tab.write(f"Your ability to score in the internal assessments with the professor:{1} ")
                tab.write(f"Your ability to score in the final assessment with the professor:{2} ")
                sl += 1
