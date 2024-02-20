
class User:
    def __init__(self,first_name, last_name,email,age):
        self.fname=first_name
        self.lname=last_name
        self.email=email
        self.age=age
        self.is_rewards_member=False
        self.gold_card_points=0
    
    def display_info(self):
        print(f"Users Full Name: {self.fname } {self.lname}")
        print(f"Users Email: {self.email}")
        print(f'Users Age: {self.age}')
        if self.is_rewards_member == True:
            print( f"{self.fname} {self.lname} is an enrolled Rewards Member with {self.gold_card_points} Gold Card Points ")
            return self
        else:
            print(f"{self.fname} {self.lname} is not a rewards member. Please enroll to start earning points! ")
            return self
        

    def enroll(self):
        if self.is_rewards_member==True:
            print("You are already a gold member")
        else:
            self.is_rewards_member=True
            self.gold_card_points+= 200
            self.display_info()
            return self
    
    def spend_gold_points(self, amount):
        if self.is_rewards_member==False:
            print("You are not an enrolled member. Please enroll to earn and spend gold reward points")
            return self
        else:
            if amount < self.gold_card_points and amount<0:
                print("You Dont have enough points or you enterd a negative number.")
                return self
            else:
                self.gold_card_points-=amount
                print( f"You now have {self.gold_card_points} points remaining")
                return self



Nina=User('Nina', 'Smith' ,' nina@yahoo', 64)
Matt= User("matt", "duffy", "fcb@gmail", 26)
Nina.enroll()
Nina.spend_gold_points(50)

Matt.enroll().spend_gold_points(80).spend_gold_points(100)


