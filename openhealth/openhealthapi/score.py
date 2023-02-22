def Score(questionid, answer):
    if questionid.Question == 'Felt your life had a sense of purpose':
        if answer == 'Yes':
            return 2
        elif answer == 'No':
            return 0
    elif questionid.Question == 'Engaged in two or more spiritual or religious practices (e.g., meditation, prayer, church services, etc.)':
        if answer == 'No':
            return 0
        elif answer == 'Yes':
            return 2
    elif questionid.Question == 'Interacted with one or more club(s) or organization(s) (e.g., athletic, community, school group, etc.)':
        if answer == 'Yes':
            s = 2
            return s
        else:
            s = 0
            return s
    elif questionid.Question == 'Spent at least two hours in nature (approximately 20 minutes daily)':
        if answer == 'Yes':
            s = 2
            return s
        else:
            s = 0
            return s

    elif questionid.Question == 'Visited or spoke to a close friend or family member on three or more separate occasions':
        if answer == 'Yes':
            s = 2
            return s
        else:
            s = 0
            return s


    elif questionid.Question == 'Total amount of cardiorespiratory exercise during the week (e.g., brisk walk, jog, etc.) (in minutes)':
        if answer == 'less than 30':
            s = 0
            return s
        elif answer == '300+':
            return 5
        elif int(answer) >= 30:
            if int(answer) == 60:
                s = 2
                return s
            elif int(answer) == 90:
                s = 3
                return s
            elif int(answer) == 120:
                s = 4
                return s
            elif int(answer) >= 150:
                s = 5
                return s
            else:
                s = 1
                return s
    elif questionid.Question == 'Total number of resistance training workouts performed (e.g., pushups, squats, pullups, etc.)':
        if answer == 'less than 1':
            s = 0
            return s
        elif answer == '10+' or int(answer) >= 2:
            s = 2
            return s
        elif int(answer) == 1:
            s = 1
            return s
    elif questionid.Question == 'Average number of hours spent sitting each day':
        if answer == 'less than 1':
            s = 3
            return s
        elif answer == '10+':
            return 0
        elif int(answer) > 0:
            if int(answer) > 7:
                s = 0
                return s
            elif int(answer) > 5:
                s = 1
                return s
            else:
                s = 3
                return s

    elif questionid.Question == 'Average number of daily servings of vegetables':
        if answer == 'less than 1':
            s = 0
            return s
        elif answer == '10+':
            return 2
        elif int(answer) >= 1:
            if int(answer) >= 3:
                s = 2
                return s
            else:
                s = 1
                return s
    elif questionid.Question == 'Average number of daily servings of fruit':
        print(type(answer))
        if answer == 'less than 1':
            s=0
            return s
        elif answer == '10+':
            s=2
            return s
        elif int(answer) == 1:
            s = 1
            return s
        elif int(answer) >= 2:
            s=2
            return s
    elif questionid.Question == 'Used olive oil as your primary oil or used no oil when cooking':
        if answer == 'Yes':
            return 1
        elif answer == 'No':
            return 0
    elif questionid.Question == 'Total number of sit-down or take-out restaurant meals':
        if answer == 'less than 1':
            return 1
        elif answer == '10+':
            return 0
        if int(answer) == 1 or int(answer) == 2 or int(answer) == 3:
            return 1
        elif int(answer) >= 4:
            return 0
    elif questionid.Question == 'Total number of sweetened drinks consumed (e.g., juice, sweetened coffee or tea, soda, sports drinks)':
        if answer == 'less than 1':
            return 2
        elif answer == '10+':
            return 0
        elif int(answer) == 1:
            return 2
        elif int(answer) >= 2:
            return 0
    elif questionid.Question == 'Average number of packaged snacks per day (e.g., chips, crackers, cookies, candy, protein bars, etc.)':
        if answer == 'less than 1' or int(answer) == 1:
            return 2
        elif answer == '10+' or int(answer) >= 2:
            return 0
    elif questionid.Question == 'Average number of hours slept per night':
        if answer == 'less than 1' or int(answer) > 1:
            if int(answer) == 7:
                return 3
            elif answer == '10+' or int(answer) >= 8:
                return 5
            else:
                s = 0
                return s

    elif questionid.Question == 'Woke up feeling refreshed and rested on most days':
        if answer == 'Yes':
            s = 2
            return s
        elif answer == 'No':
            s = 0
            return s
    elif questionid.Question == 'Felt that you were able to manage and deal with stressors effectively most days':
        if answer == 'Yes':
            s = 2
            return s
        elif answer == 'No':
            s = 0
            return s
    elif questionid.Question == 'Felt you had enough time to take care of yourself most days':
        if answer == 'Yes':
            s = 1
            return s
        elif answer == 'No':
            s = 0
            return s
    elif questionid.Question == 'Smoked, vaped, or used tobacco/e-cigarettes':
        if answer == 'Yes':
            s = 0
            return s
        elif answer == 'No':
            s = 6
            return s
    elif questionid.Question == 'Highest number of alcoholic drinks consumed on any single day':
        if answer == 'less than 1' or int(answer) == 1 or int(answer) == 2 or int(answer) == 3:
            return 2
        elif answer == '10+' or int(answer) >= 3:
            return 0
    elif questionid.Question == 'Average number of alcoholic drinks consumed on days alcohol was consumed (select less than one if you did not drink any alcohol)':
        if answer == 'less than 1' or int(answer) == 1:
            return 2
        elif answer == '10+' or int(answer) >= 2:
            return 0

    elif questionid.Question == 'Down feeling':
        if answer == 'Yes':
            return 0
        elif answer == 'No':
            return 0

    elif questionid.Question =='Loss of interest in daily activities':
        if answer == 'Yes':
            return 0
        elif answer == 'No':
            return 0

    elif questionid.Question == 'Sleep changes(oversleeping is less common)':
        if answer == 'Yes':
            return 0
        elif answer == 'No':
            return 0
    elif questionid.Question =='Appetite or weight changes':
        if answer == 'Yes':
            return 0
        elif answer == 'No':
            return 0
    elif questionid.Question == 'increased thirst':
        if answer == 'Yes':
            return 0
        elif answer == 'No':
            return 0

    elif questionid.Question == 'increased hunger':
        if answer == 'Yes':
            return 0
        elif answer == 'No':
            return 0

    elif questionid.Question == 'fatigue':
        if answer == 'Yes':
            return 0
        elif answer == 'No':
            return 0
    elif questionid.Question == 'increased urination':
        if answer == 'Yes':
            return
        elif answer == 'No':
            return 0
    elif questionid.Question == 'unintended weight loss':
        if answer == 'Yes':
            return 0
        elif answer == 'No':
            return 0

