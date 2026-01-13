from ninja import NinjaAPI

api = NinjaAPI(title="Merentalbe API", version="1.0.0")

@api.get("/hello")
def hello(request):
    return {"message": "Hello, Merental!"}