# A simple restaurant system that displays meals from 3 menus to the user and gives them the option to choose any menu and a meal from it.



class restaurant: # Defines the restaurant class

# This initializes the restaurant class with breakfast, lunch, and dinner menus
    def __init__(self):
        self.breakfast=["Oats","Tom brown","Tea","Salad","Coffee"]
        self.lunch=["Curry rice","Banku","Pasta","Paella"]
        self.dinner=["Soup","Waakye","Fried eggs","Sushi"]

# This method displays the available menu items in the restaurant
    def show_menu(self):
        print("Breakfast:")
        for i,item in enumerate(self.breakfast, 1):
            print(f"{i}. {item}")
        
        print("\nLunch:")
        for i,item in enumerate(self.lunch, 1):
            print(f"{i}. {item}")

        print("\nDinner:")
        for i,item in enumerate(self.dinner, 1):
            print(f"{i}. {item}")

# This method allows users to select a meal from the menus
    def select_menu(self):
        
        menu_choice=input("\nPick a menu,'B' for breakfast, 'L' for lunch, 'D' for dinner: ")

        # Checks the user's input and selects the corresponding menu, and prints the selected meal from the menu
        if menu_choice.upper() =='B':
            meal_choice=int(input("Input meal number: "))
            print(f"user selected {self.breakfast[meal_choice - 1]}")
        elif menu_choice.upper() =='L':
            meal_choice=int(input("Input meal number: "))
            print(f"user selected {self.lunch[meal_choice - 1]}")  
        elif menu_choice.upper() =='D':
            meal_choice=int(input("Input meal number: "))
            print(f"user selected {self.dinner[meal_choice - 1]}") 
        else:
            print("Invalid choice.")


# This creates an instance of the restaurant class and assigns it to the variable 'menu'
menu=restaurant() 
menu.show_menu()
menu.select_menu()