def app_work(tab):
    tab.subheader("How does it work?")
    tab.write("Our app starts by collecting the preferences from the user and filtering out the professors in the college available for the course")
    tab.write("After filtering out the data, our app uses datasets for each professor in the format of the following parameters: ")
    tab.write("1. Assignments - how well the student was able to cope up with the assignments given by the professors ")
    tab.write("2. Internal Assessments - this parameter talks about how well the student performed in the internal assessments")
    tab.write("3. Final Assessments - this parameter talks about well the students perform on the final assessments")
    tab.write("4. Learning Adaptabilty Score - this parameter talks about the learning ability of the student who studied under the professor")
    tab.write("Using the parameters and the trained machine learning models, we\'ve used we come up with the predictions with which we can infer the following:")
    tab.write("1. Expected Assignment Adaptability - this predicted value talks about how well the student would be able to do the assignments assigned by the professor")
    tab.write("2. Expected Internal Assessment Ability Score- this predicted value talks about how well the student would be able to perform in the internal assessments")
    tab.write("3. Expected Final Assessment Ability Score- this predicted value talks about how well the student would be able to perform on the final assessment.")
    tab.subheader("Example")
    tab.write("For example when we run the code, and we get the recommendations after filtering out the data and we get the following result,")
    tab.write("Now let us assume the student\'s learner\'s adaptability score to be 6.5,")
    tab.subheader("Professor Dharun")
    tab.subheader("")
    tab.write(f"Friendliness Rating: {9}")
    tab.write(f"Quality of the material: {6}")
    tab.write(f"Communication Skills: {8}")
    tab.write(f"Proficiency: {10}")
    tab.write(f"Your ability to handle assignments given by the professor: ")
    tab.write(f"Your ability to score in the internal assessments with the professor: ")
    tab.write(f"Your ability to score in the final assessment with the professor: ")
