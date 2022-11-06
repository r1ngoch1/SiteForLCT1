from .models import  DataBase1,Tnved_Type
def zalupa(request):

    database = DataBase1.objects.all()

    print(database)