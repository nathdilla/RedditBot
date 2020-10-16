def filter_string(string):
    omitted = ["asshole", "fuck", "shit", "penis", "cock", "anus", "vagina", "dick", "fucking", "horny", "sex",
               "retard", "gay",
               "faggot", "cum", "fuckin", "bastard", "porn", "porno", "cocksucker", "motherfucker", "motherfuckin",
               "tits",
               "ass", "nigger", "nigga", "coochie", "chink", "tit", "blowjob", "handjob", "rimjob", "anal", "taint",
               "trib", "tribbing", "jackass", "dumbass"]
    output = string

    for nono_word in omitted:
        replace = "****"
        if nono_word == "asshole":
            replace = "jerk"
        output = output.replace(nono_word, replace)
    return output

print(filter_string("Jack was a real asshole because he did not go to the party. fuckin idiot. Piss cum and jack off into"
                    "my penis, I love tits so much. Everyone is an asshole for not being a nigger. you a real nigga"))