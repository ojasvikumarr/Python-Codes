datetime = input("Enter the date in the format MM/DD/YYYY : ")

month , day , year = datetime.split("/")

year = year[2:]

print(f"{day}-{month}-{year}")