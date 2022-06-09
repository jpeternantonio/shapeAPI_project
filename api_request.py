import requests
import os 
import time

service_uri = 'http://localhost:8001/api/'


def check_server():
    uri = 'http://localhost:8001/admin/'
    try:
        requests.get(uri)
    except:
        print('Server is not running. Will exit the program.')
        time.sleep(1)
        exit()


def main_menu():
    print("+---------------------------------------+")
    print("|  Shapes RestFul API  |")
    print("+---------------------------------------+")
    global main_choice
    uri = service_uri + 'shapes/'
    res = requests.get(uri, auth=(username, password))
    global json_res_shapes
    json_res_shapes = res.json()
    global available_shapes
    available_shapes = []
    if len(json_res_shapes) == 0:
        print('No shapes found.')
        print('Please add a shape.')
        try:
            start_choice = int(input(""" What would you like to do?
            1. Add a shape
            2. Exit
            """))
        except ValueError:
            print('Invalid choice. Please try again.')
            time.sleep(1)
            main_menu()
        
        if start_choice == 1:
            add_shape()
        elif start_choice == 2:
            print('Thank you for using the Shapes RestFul API.')
            time.sleep(1)
            exit()
        elif start_choice != 1 or start_choice != 2:
            print('Invalid choice. Please try again.')
            time.sleep(1)
            main_menu()
           
    try:
        main_choice = int(input(""" What would you like to do?
        1. Add Shape
        2. Get Shape
        3. Delete Shape
        4. Update Shape
        5. Get Perimeter
        6. Get Area
        7. Exit
        Your Answer:  """))
    except ValueError:
        print('Invalid choice. Please try again.')
        time.sleep(1)
        main_menu()

    
    if main_choice == 1:
        add_shape()
    elif main_choice == 2:
        get_shape()
    elif main_choice == 3:
        delete_shape()
    elif main_choice == 4:
        update_shape()
    elif main_choice == 5:
        get_perimeter()
    elif main_choice == 6:
        get_area()
    elif main_choice == 7:
        print('Thank you for using the Shapes RestFul API.')
        time.sleep(1)
        exit()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        exit()

def register_user():
    uri = service_uri + 'users/add/'
    global username, password
    username = input('Enter your username: ').lower()
    if username == "":
        print("Username cannot be blank.")
        exit()
    email = input('Enter your email: ').lower()
    if email == "":
        print("Email cannot be blank.")
        exit()
    password = input('Enter your password: ')
    if password == "":
        print("Password cannot be blank.")
        exit()
    data = {'username': username, 'email': email, 'password': password}
    res = requests.post(uri, json=data)
    print('Welcome, ' + username)
    time.sleep(1)
    main_menu()


def add_shape():
    if len(json_res_shapes) == 4:
        print('You have reached the maximum number of shapes.')
        time.sleep(1)
        main_menu()
    if len(json_res_shapes) > 0:
        get_shape()
        to_add_shape()
    elif len(json_res_shapes) == 0:
        to_add_shape()
   
 


def to_add_shape():
    uri = service_uri + 'shapes/add/'
   
    try:
         shape_choice = int(input(""" What shape would you like to add?
            1. Triangle
            2. Square
            3. Rectangle
            4. Diamond
            Type the number.
            Your Answer:  """))
    except ValueError:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        add_shape()

    available_choices = [1, 2 ,3, 4]
    if shape_choice not in available_choices:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        add_shape()


    if shape_choice == 1 and 'triangle' not in available_shapes:
        try:
            triangle_side = int(input('Enter the side length: '))
        except ValueError:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            add_shape()
            
        if triangle_side <= 0:
            print('Invalid side length. Please try again.')
            time.sleep(1)
            add_shape()
        try:
            triangle_height = int(input('Enter the height length: '))
        except ValueError:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            add_shape()
        if triangle_height <= 0:
            print('Invalid height length. Please try again.')
            time.sleep(1)
            add_shape()
        try:
            triangle_base = int(input('Enter the base length: '))
        except ValueError:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            add_shape()
        if triangle_base <= 0:
            print('Invalid base length. Please try again.')
            time.sleep(1)
            add_shape()
        data = {'name': 'triangle', 'side': triangle_side, 'height': triangle_height, 'base': triangle_base}
        res = requests.post(uri, json=data,  auth=(username, password))
        if res.status_code == 200:
            print('Shape Triangle added.')
            time.sleep(1)
            main_menu()
    elif shape_choice == 1 and 'triangle' in available_shapes:
        print('Triangle Shape already exists.')
        time.sleep(1)
        main_menu()
    
    if shape_choice == 2 and 'square' not in available_shapes:
        try:
            square_side = int(input('Enter the side length: '))
        except ValueError:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            add_shape()
        if square_side <= 0:
            print('Invalid side length. Please try again.')
            time.sleep(1)
            add_shape()
        data = {'name': 'square', 'side': square_side, 'height': 0, 'base': 0}
        res = requests.post(uri, json=data,  auth=(username, password))
        if res.status_code == 200:
            print('Shape Square added.')
            time.sleep(1)
            main_menu()
    elif shape_choice == 2 and 'square' in available_shapes:
        print('Square Shape already exists.')
        time.sleep(1)
        main_menu()

    if shape_choice == 3 and 'rectangle' not in available_shapes:
        try:
            rectangle_side = int(input('Enter the side length: '))
        except ValueError:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            add_shape()
        if rectangle_side <= 0:
            print('Invalid side length. Please try again.')
            time.sleep(1)
            add_shape()
        try:
            rectangle_base = int(input('Enter the base length: '))
        except ValueError:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            add_shape()
        if rectangle_base <= 0:
            print('Invalid base length. Please try again.')
            time.sleep(1)
            add_shape()
        data = {'name': 'rectangle', 'side': rectangle_side, 'base': rectangle_base, 'height': 0}
        res = requests.post(uri, json=data,  auth=(username, password))
        if res.status_code == 200:
            print('Shape Rectangle added.')
            time.sleep(1)
            main_menu()
    elif shape_choice == 3 and 'rectangle' in available_shapes:
        print('Rectangle Shape already exists.')
        time.sleep(1)
        main_menu()

    if shape_choice == 4 and 'diamond' not in available_shapes:
        try:
            diamond_side = int(input('Enter the side length: '))
        except ValueError:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            add_shape()
        if diamond_side <= 0:
            print('Invalid side length. Please try again.')
            time.sleep(1)
            add_shape()
        try:
            diamond_height = int(input('Enter the height length: '))
        except ValueError:
            print("Invalid choice. Please try again.")
            time.sleep(1)
            add_shape()
        if diamond_height <= 0:
            print('Invalid height length. Please try again.')
            time.sleep(1)
            add_shape()
        data = {'name': 'diamond', 'side': diamond_side, 'height': diamond_height, 'base': 0}
        res = requests.post(uri, json=data,  auth=(username, password))
        if res.status_code == 200:
            print('Shape Diamond added.')
            time.sleep(1)
            main_menu()
    elif shape_choice == 4 and 'diamond' in available_shapes:
        print('Diamond Shape already exists.')
        time.sleep(1)
        main_menu()


 
    # res = requests.post(uri, json=data,  auth=(username, password))

def get_shape():
    print('Here are the available shapes:')
    for shape in json_res_shapes:
        available_shapes.append(shape['name'])
        print(f"Name:{shape['name']}, Side:{shape['side']}, Height:{shape['height']}, Base:{shape['base']}")

    time.sleep(2)
    if main_choice == 2:
        main_menu()

    # main_menu()

def delete_shape():
    get_shape()
    uri = service_uri + 'shapes/add/'
    # print(available_shapes)
    shape_choice_name = str(input(""" What shape would you like to delete?
    Type the name.
    Your Answer:  """)).lower()
    if shape_choice_name not in available_shapes:
        print('you typed: ', shape_choice_name)
        print("Invalid choice. Please try again.")
        time.sleep(1)
        delete_shape()
    
    if shape_choice_name in available_shapes:
        data = {'name': shape_choice_name}
        res = requests.delete(uri, json=data,  auth=(username, password))
        if res.status_code == 200:
            print('Shape deleted.')
            time.sleep(1)
            main_menu()
    


def update_shape():
    get_shape()
    uri = service_uri + 'shapes/add/'
    shape_choice_name = str(input(""" What shape would you like to update?
    Type the name.
    Your Answer:  """)).lower()
    if shape_choice_name not in available_shapes:
        print('you typed: ', shape_choice_name)
        print("Invalid choice. Please try again.")
        time.sleep(1)
        update_shape()
    
    if shape_choice_name in available_shapes:
        if shape_choice_name == 'triangle':
            try:
                triangle_side = int(input('Enter the side length: '))
            except ValueError:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                update_shape()
            if triangle_side <= 0:
                print('Invalid side length. Please try again.')
                time.sleep(1)
                update_shape()
            try:
                triangle_height = int(input('Enter the height length: '))
            except ValueError:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                update_shape()
            if triangle_height <= 0:
                print('Invalid height length. Please try again.')
                time.sleep(1)
                update_shape()
            try:
                triangle_base = int(input('Enter the base length: '))
            except ValueError:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                update_shape()
            if triangle_base <= 0:
                print('Invalid base length. Please try again.')
                time.sleep(1)
                update_shape()
            data = {'name': 'triangle', 'side': triangle_side, 'height': triangle_height, 'base': triangle_base}
            res = requests.put(uri, json=data,  auth=(username, password))
            if res.status_code == 200:
                print('Triangle Shape updated.')
                time.sleep(1)
                main_menu()
        elif shape_choice_name == 'square':
            try:
                square_side = int(input('Enter the side length: '))
            except ValueError:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                update_shape()
            if square_side <= 0:
                print('Invalid side length. Please try again.')
                time.sleep(1)
                update_shape()
            data = {'name': 'square', 'side': square_side, 'height': 0, 'base': 0}
            res = requests.put(uri, json=data,  auth=(username, password))
            if res.status_code == 200:
                print('Square Shape updated.')
                main_menu()
        elif shape_choice_name == 'rectangle':
            try:
                rectangle_side = int(input('Enter the side length: '))
            except ValueError:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                update_shape()
            if rectangle_side <= 0:
                print('Invalid side length. Please try again.')
                time.sleep(1)
                update_shape()
            try:
                rectangle_base = int(input('Enter the base length: '))
            except ValueError:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                update_shape()
            if rectangle_base <= 0:
                print('Invalid base length. Please try again.')
                time.sleep(1)
                update_shape()
            data = {'name': 'rectangle', 'side': rectangle_side, 'base': rectangle_base, 'height': 0}
            res = requests.put(uri, json=data,  auth=(username, password))
            if res.status_code == 200:
                print('Rectangle Shape updated.')
                time.sleep(1)
                main_menu()
        elif shape_choice_name == 'diamond':
            try:
                diamond_side = int(input('Enter the side length: '))
            except ValueError:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                update_shape()
            if diamond_side <= 0:
                print('Invalid side length. Please try again.')
                update_shape()
            try:
                diamond_height = int(input('Enter the height length: '))
            except ValueError:
                print("Invalid choice. Please try again.")
                time.sleep(1)
                update_shape()
            if diamond_height <= 0:
                print('Invalid height length. Please try again.')
                update_shape()
            data = {'name': 'diamond', 'side': diamond_side, 'height': diamond_height, 'base': 0}
            res = requests.put(uri, json=data,  auth=(username, password))
            if res.status_code == 200:
                print('Diamond Shape updated.')
                time.sleep(1)
                main_menu()

def get_perimeter():
    get_shape()
    shape_choice_name = str(input(""" What shape would you like to get the perimeter?
    Type the name.
    Your Answer:  """)).lower()
    if shape_choice_name not in available_shapes:
        print('you typed: ', shape_choice_name)
        print("Invalid choice. Please try again.")
        time.sleep(1)
        get_perimeter()
    
    if shape_choice_name in available_shapes:
        if shape_choice_name == 'triangle':
            for shape in json_res_shapes:
                if shape['name'] == 'triangle':
                    triangle_side = shape['side']
                    triangle_base = shape['base']
                    perimeter = triangle_side + triangle_base
                    print(f'The perimeter of the triangle is {perimeter}')
                    time.sleep(1)
                    main_menu()
        elif shape_choice_name == 'square':
            for shape in json_res_shapes:
                if shape['name'] == 'square':
                    square_side = shape['side']
                    perimeter = square_side * 4
                    print(f'The perimeter of the square is {perimeter}')
                    time.sleep(1)
                    main_menu()
        elif shape_choice_name == 'rectangle':
            for shape in json_res_shapes:
                if shape['name'] == 'rectangle':
                    rectangle_side = shape['side']
                    rectangle_base = shape['base']
                    perimeter = (rectangle_side * 2) + (rectangle_base * 2)
                    print(f'The perimeter of the rectangle is {perimeter}')
                    time.sleep(1)
                    main_menu()
        elif shape_choice_name == 'diamond':
            for shape in json_res_shapes:
                if shape['name'] == 'diamond':
                    diamond_side = shape['side']
                    perimeter = diamond_side * 4
                    print(f'The perimeter of the diamond is {perimeter}')
                    time.sleep(1)
                    main_menu()


def get_area():
    get_shape()
    shape_choice_name = str(input(""" What shape would you like to get the area?
    Type the name.
    Your Answer:  """)).lower()
    if shape_choice_name not in available_shapes:
        print('you typed: ', shape_choice_name)
        print("Invalid choice. Please try again.")
        time.sleep(1)
        get_area()
    
    if shape_choice_name in available_shapes:
        if shape_choice_name == 'triangle':
            for shape in json_res_shapes:
                if shape['name'] == 'triangle':
                    triangle_base = shape['base']
                    triangle_height = shape['height']
                    area = (triangle_base * triangle_height) / 2
                    print(f'The area of the triangle is {area}')
                    time.sleep(1)
                    main_menu()
                   
        elif shape_choice_name == 'square':
            for shape in json_res_shapes:
                if shape['name'] == 'square':
                    square_side = shape['side']
                    area = square_side * square_side
                    print(f'The area of the square is {area}')
                    time.sleep(1)
                    main_menu()
        elif shape_choice_name == 'rectangle':
            for shape in json_res_shapes:
                if shape['name'] == 'rectangle':
                    rectangle_side = shape['side']
                    rectangle_base = shape['base']
                    area = rectangle_side * rectangle_base
                    print(f'The area of the rectangle is {area}')
                    time.sleep(1)
                    main_menu()
            for shape in json_res_shapes:
                if shape['name'] == 'diamond':
                    diamond_side = shape['side']
                    diamond_height = shape['height']
                    area = (diamond_side * diamond_height) / 2
                    print(f'The area of the diamond is {area}')
                    time.sleep(1)
                    main_menu()




def login():
    global username, password
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    user_id_request = requests.get(f'{service_uri}users/', auth=(username, password))
    if user_id_request.status_code == 401:
        print('Invalid user. Please check your username or password.')
        time.sleep(1)
        welcome()
        
    elif user_id_request.status_code == 200:
        print('Welcome, ' + username)
        time.sleep(1)
    main_menu()


def welcome():
    print("+---------------------------------------+")
    print("|  Welcome to Shapes RestFul API  |")
    print("+---------------------------------------+")

    try:
        initial_choice = int(input(""" What would you like to do?
        1. Login
        2. Register
        3. Exit
        Type the number.
        Your Answer:  """))
    except ValueError:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        welcome()


    if initial_choice == 1:
        login()
    elif initial_choice == 2:
        register_user()
    elif initial_choice == 3:
        print('Thank you for using the Shapes RestFul API.')
        exit()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        welcome()


check_server()
welcome()
