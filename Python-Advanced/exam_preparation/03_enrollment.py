def gather_credits(number_of_credits, *args):

    courses = []
    gathered_credits = 0
    
    for name, credits in args:
        if gathered_credits < number_of_credits and name not in courses:
            courses.append(name)
            gathered_credits += credits

            if gathered_credits >= number_of_credits:
                break
    if gathered_credits >= number_of_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted(courses))}"
    return f"You need to enroll in more courses! You have to gather {number_of_credits - gathered_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

print(gather_credits(
    0,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))

