# from fastapi import FastAPI
# from fastapi.templating import Jinja2Templates
# #from model import User
# from fastapi import Request
#
# app = FastAPI()
#

#1.1
# @app.get("/")
# async def root():
#     return {"message": "Добро пожаловать в моё приложение FastAPI!"}

#1.2
#templates = Jinja2Templates(directory="templates")
# @app.get("/")
# async def index(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})

#1.3
# @app.get("/calculate")
# async def calculate(num1: int, num2: int):
#     return {"result": num1 + num2}

#1.4
#user_1 = User(id=1, name="Sasha Belov")
# @app.get("/users")
# async def get_users():
#     return {"id": user_1.id, "name": user_1.name}

#1.5
# @app.post("/user")
# async def create_user(user: User):
#     #Артур генадьевич, я узнал почему не работало, там была какая-то проблема с реквестом, он по умолчанию ставил тип none
#     #а оказывается, что FastApi умеет сразу парсить json в pydantic model, так что можно просто
#     передавать pydantic model в фунцкию
#     is_adult = False
#     if user.age >= 18:
#         is_adult = True
#     return {"name": user.name, "age": user.age, "is_adult": is_adult}

#2.1
# from fastapi import FastAPI
# from model import Feedback
#
#
# app = FastAPI()
# feedback_list = []
#
#
# @app.post("/feedback")
# async def feedback(feedback: Feedback):
#     feedback_list.append(feedback.feedback)
#     return {"message": "Feedback received. Thank you, Rustam."}

# #2.2
# from fastapi import FastAPI
# from model import Feeedback
#
#
# app = FastAPI()
# feedbacks = []
#
#
# @app.post("/feedback")
# async def feedback(feeedback: Feeedback):
#     feedbacks.append(feeedback.feedback)
#     print(feedbacks)
#     return {"message": f"Спасибо, {feeedback.name}! Ваш отзывсохранён."}