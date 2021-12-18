from logging import *
import logging
import getpass

username = getpass.getuser()

basicConfig(
	filename='day_finder.log',
	level=DEBUG,
	style="{",
	datefmt="%d/%m/%Y  %I:%M:%S %p",
	format="{asctime} {message}"
)


logger = logging.getLogger()

logger.setLevel(logging.INFO)
error( f" {username}  {logging.getLevelName(logging.root.level)}:  ---  File  Runned  by  user:{username}")



def main():

    day = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}
    print("\n\n\t\t--------------------------------------")
    print("\t\t|\t    Find Y0uR D@Y   \t      |")
    print("\t\t--------------------------------------\n\n")
    valid = True
    date = input("  ----★ Date: ")
    month = input("\n  ----★ Month: ")
    year = input("\n  ----★ Year: ")

    logger.setLevel(logging.ERROR)

    if not date.isdigit() or not month.isdigit() or not year.isdigit():
        print("\n  ERROR: \tDate, Month and Year should be a integer :(\n")

        error(
            f" {username}  {logging.getLevelName(logging.root.level)}:  ---  Typeerror Date or Month or Year is not a digit -- Date:{date} Month:{month} Year:{year}")
        retry()
    else:
        date = int(date)
        month = int(month)
        year = int(year)

    if len(str(date)) > 2 or len(str(month)) > 2 or len(str(year)) != 4:
        print("  Error! :(")
        print("\tPlease check your DD/MM/YY")
        print("\t\tYear should be greater than 1500 and date & month should be valid :(")
        if len(str(date)) > 2:
            error(f" {username}  {logging.getLevelName(logging.root.level)}:  ---  Date's length greater than 2 -- Date:{date} Month:{month} Year:{year}")
        if len(str(month)) > 2:
            error(f" {username}  {logging.getLevelName(logging.root.level)}:  ---  Month's length greater than 2 -- Date:{date} Month:{month} Year:{year}")
        if len(str(year)) != 4:
            error(f" {username}  {logging.getLevelName(logging.root.level)}:  ---  Year's length is not equal to 4 -- Date:{date} Month:{month} Year:{year}")
        retry()

    if (date <= 31) == False or (month <= 12) == False or (year >= 1500)  == False:
        print("  Error! :(")
        print("\tPlease check your DD/MM/YY")
        print("\t\tYear should be greater than 1500 and date & month should be valid :(")
        error(f" {username}  {logging.getLevelName(logging.root.level)}:  ---  INVALID Arguments input -- Date:{date} Month:{month} Year:{year}")
        retry()


    def dt(st):
        return st

    def mnt(st):
        if st == 1:
            return 1
        elif st == 2:
                return 4
        elif st == 3:
                return 4
        elif st == 4:
                return 0
        elif st == 5:
                return 2
        elif st == 6:
                return 5
        elif st == 7:
                return 0
        elif st == 8:
                return 3
        elif st == 9:
                return 6
        elif st == 10:
                return 1
        elif st == 11:
                return 4
        elif st == 12:
                return 6

    def yr(st):
        if str(st).startswith("15"):
            return 0
        if str(st).startswith("16"):
            return 6
        if str(st).startswith("17"):
            return 4
        if str(st).startswith("18"):
            return 2
        if str(st).startswith("19"):
            return 0
        if str(st).startswith("20"):
            return 6
    main_year = yr(year)

    temp = str(year)
    main_year_last2 = int(temp[-2:])

    main_month = mnt(month)

    main_date = dt(date)

    leap_year = int(main_year_last2/4)

    sum_ = main_date + main_month + main_year + main_year_last2 + leap_year

    result = sum_ % 7

    res_day = day[result]

    logger.setLevel(logging.INFO)
    info(f" {username}  {logging.getLevelName(logging.root.level)}:  ---  DATE:{date}  MONTH:{month}  YEAR:{year}  LEAP_YEAR:{leap_year}  --  SUM:{sum_}  RESULT_int:{result}   DAY:{res_day}")


    print("\t --------------------------------------------")
    print(f"\t\t\tThe Day was/will be {res_day}")
    print("\t --------------------------------------------")




def retry():
    print("\n\t\tPRESS 1 to continue or 0 to exit :')\n")
    inp = input("\t-->>")

    if inp == '1':
        main()
    else:
    	logger.setLevel(logging.INFO)
    	error( f" {username}  {logging.getLevelName(logging.root.level)}:  ---  user:{username}  EXITTED")
    	exit(0)

main()
