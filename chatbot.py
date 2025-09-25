# # simple chatbot in python

# def chatbot():
#     print("chatbot: Namaste! Main aapka chatbot hoon. (type 'exit' to quit)")

#     while True:
#         user = input("You: ").lower()

#         if user == "exit":
#             print("chatbot: Bye! Milte hain fir😊")
#             break

#         elif "hello" in user or "hi" in user:
#             print("chatbot: Hello dost! kaise ho?")

#         elif "kaise ho" in user:
#             print("chatbot: Main theek hoon, aap kaise ho?")

#         elif "naam" in user:
#             print("chatbot: mera naam python chaitbot hain.💖💖😀")

#         elif "python" in user:
#             print("python ek bahut powerful aur easy programming language hai.")

#         elif "bharat ke pradhaan mantri kaun hain" in user:
#             print("bharat ke pradhanmantri shri narendra modi hai.💖")

#         elif "Main aapka sabse achhat dost hoon" in user:
#             print("thanks👍")

#         elif "india is a independence nation" in user:
#             print("yes , right👍")

#         elif " aap mera sabse achha dost hai bhai." in user:
#             print("really , aap bhi mera sabse achha dost hai")

#         elif "dost two plus two kitna hota hai" in user:
#             print("two plus two four hota hai.🤣")

#         elif "khana khane ke kitne minutes ke baad pani pina chahiye." in user:
#             print("chatbot: dost khana khnae ke 45 minutes ke baad pani pina chahiye")

#         elif "bharat kab aazad hua tha" in user:
#             print("chatbot : apna bharat 26 jan 1950 ko aazad hua tha")

#         else:
#             print("chatbot: Mujhe ye samjh nahi aaya😂😎")
# chatbot()
        



# simple chatbot

def chatbot():
    print("chatbot: i am simple chatbot :")

while True:
    user_inp = input("you :")

    if user_inp == "hi"  or user_inp ==  "hello ":
        print("charbot: hello how can help you:")

    elif "your name" in user_inp:
        print("chatbot: i am simple chatbot:")

    elif "how can help me" in user_inp:
        print("chatbot: as your wish:")

    else:
        print("chatbot: invalid cmd:")

chatbot()