post = input("Enyter your Post \n")
if "harry" in post:
    print("Post is about Harry")
elif "hary" in post:
    print("Post is about Harry")
elif "HAARY" in post:
    print("Post is about Harry")
elif "HARRY" in post:
    print("Post is about Harry")
elif "HaRRY" in post:
    print("Post is about Harry")
else:
    print("Post is not about harry")