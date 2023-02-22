def validation(TotalScore):
    if TotalScore <= 20:
        # print(
        #     f"{TotalScore}Below Average, This is an opportune time to work with your provider to help you adopt habits that will significantly improve your health")
        return "Below Average, This is an opportune time to work with your provider to help you adopt habits that will significantly improve your health."
    elif 21 <= TotalScore <= 30:
        # print(
        #     "Average,You have some great health habits,throughthere is sample opportunity to improve your health and decreases your disease risk")
        return "Average,You have some great health habits,throughthere is sample opportunity to improve your health and decreases your disease risk."
    elif 31 <= TotalScore <= 40:
        # print(
        #     "Very Good, You have many healthy habits, though there are a few areas that you should assess your habits in to see if you can improve them.")
        return "Very Good, You have many healthy habits, though there are a few areas that you should assess your habits in to see if you can improve them."
    elif 41 <= TotalScore <= 50:
        print("Excellent, Consider minor tweaks to a an overall very healthy lifestyle overall.")
        return "Excellent, Consider minor tweaks to a an overall very healthy lifestyle overall."


# print(validation(22))

def category_validation(Score):
    if Score < 7:
        # print(
        #     "significant room for improvement.Discuss this area specifically with your provider to see how you can improve your health.")
        return "significant room for improvement.Discuss this area specifically with your provider to see how you can improve your health."

    elif 7 <= Score <= 9:
        # print(
        #     "Although you are doing well, a few tweaks to address the  domain items could significantly improve your health.")
        return "Although you are doing well, a few tweaks to address the  domain items could significantly improve your health."
    elif Score <= 10:
        # print(
        #     "Perfect score!Talk To your provider about other things you can do beyond this assessment to improve your health.")
        return "Perfect score!Talk To your provider about other things you can do beyond this assessment to improve your health."


category_validation(8)


def answer_validation_depression(Answer):
    if Answer == 'Yes':
        return f'{Answer} then, You might be having Initial Signs and Symptoms for Depression; We suggest to consult with Psychiatrist'
    elif Answer == 'No':
        return f'{Answer} then, You are not having any Initial Signs and Symptoms for Depression; but you can always consult with Psychatrist  for better clarity'


def answer_validation_diabetes(Answer):
    if Answer == 'Yes':
        return f'{Answer} then, You might be having Initial Signs and Symptoms for Diabetes; We suggest to consult with Endocrinologist'
    elif Answer == 'No':
        return f'{Answer} then, You are not having any Initial Signs and Symptoms for Diabetes; but you can always consult with Endocrinologist for better clarity'
