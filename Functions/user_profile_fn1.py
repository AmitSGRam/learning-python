def build_profile(first, last, **user_info):
    user_info['f_name'] = first
    user_info['l_name'] = last
    return user_info

user_profile = build_profile("amit", "sgr",
                            age=25, languages="python, go lang",
                            height=174)
                            
print(user_profile)