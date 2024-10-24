class Star_cinema : 
    

    __hall_list = [] # create a class attribute 



    @classmethod
    def entry_hall(cls,hall_obj):
        cls.__hall_list.append(hall_obj) 

    @classmethod 
    def view_hall(cls):
        for hall in cls.__hall_list:
            print(f"Hall Number : {hall.get_hallNo()} , Row : {hall.get_rowNo()} , Col: {hall.getColNo()}")


class Hall(Star_cinema):
        
    def __init__(self , rows , cols , hall_no ) -> None:
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        self.__show_list = []
        self.__seats = {}
        self.entry_hall(self)
        
        

    # 3 number question requirement
    def entry_show(self,id,movie_name , time):
        self.id = id 
        self.movie_name = movie_name 
        self.time = time
        info = (self.id, self.movie_name, self.time)
        self.__show_list.append(info)
        self.__seats[id] = []

        for i in range(self.__rows):
            row = []
            for j in range(self.__cols):
                row.append(0)
            self.__seats[id].append(row)

    # 4 number question Requirement
    def book_seat(self , id ):
        
        if id not in self.__seats :
            print(f"Invalid Show Id \n\n")
            return

        NumberOfTicket = int(input('Numher Of Ticket?: '))


        availableTicket = 0 

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0: 
                    availableTicket+=1 
        
        if availableTicket < NumberOfTicket :
            print(f"There are not that many tickets for this show {id}.")
            return

        print(f"\nAvailable Seat for the show {id}")

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0:
                    print(f"Seat ({i} , {j}) --> Free")
                else:
                    print(f"Seat ({i} , {j}) --> Booked")
            

        print(f"\n\nUpdated Seats Layout : \n")
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(self.__seats[id][i][j] ,end=" ")
            print("\n")

       
        for i in range(NumberOfTicket):
            while True: 
                SeatRow = int(input('Enter Seat Row: '))
                SeatCol = int(input("Enter Seat Column: "))

                if(SeatRow >= 0 and SeatRow < self.__rows) and (SeatCol >= 0 and SeatCol < self.__cols):
                    if self.__seats[id][SeatRow][SeatCol] == 0 :
                        self.__seats[id][SeatRow][SeatCol] = 1 
                        print(f"Seat {SeatRow} , {SeatCol} is Booked Successfully .")
                        break
                    else: 
                        print(f"This Seat {SeatRow}, {SeatCol} Already Booked . Please select Another Ones.\n")
                else:
                    print(f"Invalid Seat selection . Please select Valid Seat Row And Col\n")
                    

    #5 number question requirement
    def view_show_list(self):
        if len(self.__show_list) == 0: 
            print(f"There is no show currently running.")
            return

        for value in self.__show_list: # Print each show in the show list
            print(value)
        print("\n")

    #6 number question requirement
    def view_available_seats(self , id ):
        if id not in self.__seats: # it's complexity o(1)
            print(f"Invalid Show Id\n")
            return



        print(f'Available Seat for show  {id}')

        # rowSize = len(self.__seats[id]) # find the row size 
        # colSize = len(self.__seats[id][0])#find the col size

        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__seats[id][i][j] == 0 :
                    print(f"seat ({i} , {j}) --> Free")
                else:
                    print(f"seat ({i} , {j}) --> Booked")
        
        print("\n")
        print(f"Updated Seats Layout : ")
        for i in range(self.__rows):
            for j in range(self.__cols):
                print(self.__seats[id][i][j], end= " ")
            print()


    
    #getter Method Use for access Private attribute
    def get_hallNo(self):
            return self.__hall_no
    
    def get_rowNo(self):
        return self.__rows

    def getColNo(self):
        return self.__cols
    
    def __repr__(self) -> str:
        return f"HallNumber : {self.__hall_no} Rows : {self.__rows} Cols : {self.__cols}"


HallDictionary = {}

while True:
    print(f"Who are You ? ")
    print(f"1.Are You HallOwner/HallManager")
    print(f"2.Are You User")
    print(f"Exit")
    option = int(input("Select Option : "))
    if option == 1 :
        while True: 
            print(f"1.Are You want a create a new Hall in your Star cinema")
            print(f"2.Are You want to entry show")
            print(f"3.Show All the Halls in Star Cinema")
            print(f"4.Do You want to Back")
            # print(f"1. Yes...")
            # print(f"2. No...")
            chose = int(input("Chose Your Option: "))

            if chose ==1 :

                rowss = int(input("How many rows do you want?"))
                colss = int(input("How many column do you want?"))
                hallNumber = int(input("Enter Hall Number "))

                if hallNumber in HallDictionary:
                    print(f"This hallNumber Hall already exist .Enter different HallNumber : ")
                    continue

                HallDictionary[hallNumber] = Hall(rowss,colss,hallNumber)

                

            elif chose == 2 : 
                
                if not HallDictionary:
                    print(f"No Halls Available. Please create One First")
                    continue

                print(f"Existed Hall List : ")
                for key,value in HallDictionary.items():
                    print(f"HallNumber: {key} - {value}")
                print("\n")

                HallNumber = int(input("Enter Hall_Number : "))
                if HallNumber not in HallDictionary:
                    print(f"HallNumber is not exist ")
                    continue
                
                id = int(input("Enter Movie Id : "))
                MovieName = input("Enter Movie Name: ")
                Time = input("Enter show Time : ")
                HallDictionary[HallNumber].entry_show(id,MovieName,Time)
            
            elif chose == 3 : 
                if not HallDictionary:
                    print(f"No Halls Available . please Create One First.")
                    continue
                Star_cinema.view_hall()

            else:
                break
    elif option == 2:
        
        
        if not HallDictionary:
            print(f"No Halls Available. Please Create One First.")
            break

        print(f"Existed Hall List : ")
        for key,value in HallDictionary.items():
            print(f"HallNumber: {key} - {value}")
        print("\n")

        print("Which hall's information do you want to know? Enter The HallNumber : ")
        hallNumber 
        while True:
            hallNumber = int(input("Hall Numbers: "))
            if hallNumber not in HallDictionary:
                print(f"Enter Valid Hall Number . this is not valid ")
            else:
                break
   
        while True:

            print('\t1. VIEW ALL THE SHOW TODAY')
            print('\t2. VIEW AVAILABLE SEATS')
            print('\t3. BOOK TICKET')
            print('\t4. EXIT')
            option = int(input('ENTER OPTION: '))

            if option == 1 :
                # print(f"Existed Hall List : ")
                # for key,value in HallDictionary.items:
                #     print(f"HallNumber: {key} - {value}")
                # print("\n")

                # print(f"Which Hall All The Show  Are You Want To See")
                # hallNumber = int(input("Hall Numbers: "))
                # if hallNumber not in HallDictionary:
                #     print(f"Enter Valid Hall Number . this is not valid ")
                #     continue

                print("********************************************************\n\n")

                HallDictionary[hallNumber].view_show_list()

                print("********************************************************\n\n")


            elif option == 2:

                # print(f"Existed Hall List : ")
                # for key,value in HallDictionary.items:
                #     print(f"HallNumber: {key} - {value}")
                # print("\n")

                # print(f"Which hall's available tickets do you want to view?")

                # print(f"Which Hall All The Show  Are You Want To See")
                # hallNumber = int(input("Hall Numbers: "))
                # if hallNumber not in HallDictionary:
                #     print(f"Enter Valid Hall Number . this is not valid ")
                #     continue

                

                id = int(input("Enter Show Id : "))
                HallDictionary[hallNumber].view_available_seats(id)

            elif option == 3:
                id = int(input('Enter Show Id : '))
                HallDictionary[hallNumber].book_seat(id)
            else:
                break
    else:
        break
        






