from dataset import Dataset
import datetime

def formatDate(date):
    vals = date.split("/")
    formattedDate = datetime.datetime(int(vals[2]),int(vals[1]),int(vals[0]))  
    return formattedDate  

print("~~Halal Backtesting Engine~~")
startDate = input("Enter the start date in the format dd/mm/yy: \n")
endDate = input("Enter the end date in the format dd/mm/yy: \n")
ticker = input("Enter the ticker of the stock you want to test: \n")    
interval = input("Enter your desired interval in the format as a number and one of (m,h,d): \n")
#strategy = input("Enter your desired strategy name: ")


dataset = Dataset(formatDate(startDate),formatDate(endDate),ticker,interval)
dataset.fetchData()
print(dataset.data.head)
