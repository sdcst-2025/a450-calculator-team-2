import time
import math




def title():



    print("Welcome to our new and improved calculator!")
    time.sleep(1)
    print("This calculator does many things such as:")
    time.sleep(1)
    print("1. Missing triangle side (A or B)")
    time.sleep(0.5)
    print("2. Calculate the missing hypotenuse (C).")
    time.sleep(0.5)
    print("3. Area of a Circle")
    time.sleep(0.5)
    print("4. Area of a rectangle")
    time.sleep(0.5)
    print("5. Area of a triangle")
    time.sleep(0.5)
    print("6. Volume of a cylinder")
    time.sleep(0.5)
    print("7. Circumference of a circle")
    time.sleep(0.5)
    print("8. GST + PST")
    time.sleep(0.5)
    print("9.Addition")
    time.sleep(0.5)
    print("10.Subtraction")
    time.sleep(0.5)
    print("11.Multiplication")
    time.sleep(0.5)
    print("12.Division")
    time.sleep(0.5)
    print("13.Credits")
    time.sleep(0.5)
    print("14.Quit")
def missing_side():
    try:
        A = float(input("Please enter the hypotenuse length:"))
        B = float(input("Please provide the remaining side length you have:"))
        if B >= A:
            print("Side length cannot be longer then hypotenuse")
        C = (A**2 - B**2) ** 0.5
        print(f"The missing value for the missing side is {C}")
    except ValueError:
        print("Please enter a valid number:")


def missing_hypotenuse():
    try:
        a = float(input("Please enter side 1:"))
        b = float(input("Please enter side 2:"))
        C = round((a**2 + b**2) ** 0.5, 2)


        print(f"The hypotenuse is {C}")
    except ValueError:
        print("Please enter a valid number:")




def a_circle():
    try:
        r = float(input("Enter value for the radius:"))
        a = round(math.pi * (r**2), 2)
        print(f"{a}")
    except ValueError:
        print("Please enter a valid number:")
   
def a_rectangle():
    try:
        L = float(input("Please enter the length:"))
        W = float(input("Please enter the width:"))
        A = round(W * L, 2)
        print(f"The area is {A}!")
    except ValueError:
        print("Please enter a valid number:")






def a_triangle():
    try:
        b = float(input("Enter value for the base:"))
        h = float(input("Enter value for the height:"))
        a = round((h * b) / 2, 2)
        print(f"The answer is {a}!")
    except ValueError:
        print("Please enter a valid number:")





def v_cylinder():
    try:
        R = float(input("Please enter the value for the radius:"))
        H = float(input("Please enter the value for the height:"))
        V = round(math.pi * (R**2) * H, 2)
        print(f"The volume for the cylinder is {V}")
    except ValueError:
        print("Please enter a valid number:")



def circumference_circle():
    try:
        R = float(input("please enter the value of the radius:"))
        C = round(2 * math.pi * R, 2)
        print(f"The value of the circumference is {C}")
    except ValueError:
        print("Please enter a valid number:")





def gst_pst():
    try:
        C = float(input("Please enter the value: "))
       
        gst = C * 0.05
        pst = C * 0.07
        total = round(C + gst + pst, 2)


        print(f"GST = {gst}, PST = {pst}, total = {total}")
    except ValueError:
        print("Please enter a valid number:")



def addition():
    try:
        A = float(input("Enter first number:"))
        B = float(input("Enter a second number:"))
        C = A + B
        print(f"The sum is {C}")
    except ValueError:
        print("Please enter a valid number:")
   
def subtraction():
    try:
        A = float(input("Please enter the first value:"))
        B = float(input("Please enter the second value:"))
        C = A - B
        print(f"The difference is {C}")
    except ValueError:
        print("Please enter a valid number.")




   
def multiplication():
    try:
        A = float(input("Please enter the first value:"))
        B = float(input("Please enter the second value:"))
        C = round(A * B, 2)
        print(f"The product is {C}")


    except ValueError:
        print("Please enter a valid number.")





def division():
    try:
        A = float(input("Please enter the first value:"))
        B = float(input("Please enter the second value:"))
        C = round(A / B, 2)
        print(f"The quotient is {C}")
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("cannot divide by zero.")


   



def credits():
    print("Devs: Greyson, Takala")
    print("Tilte (Greyson)")
    print("Flowchart (Takala)")
    print("Definitions 1 - 7 (Greyson)")
    print("Definitions 8-14 (Takala)")
    print("Touch up (Greyson, Takala)")





def main():
    title()
    Running = True
    while Running:
        Choice = input("Enter the corresponding number to the formula you would like to choose:")
        try:
            if Choice == '1':
                missing_side()
            elif Choice == '2':
                missing_hypotenuse()
            elif Choice == '3':
                a_circle()
            elif Choice == '4':
                a_rectangle()
            elif Choice == '5':
                a_triangle()
            elif Choice == '6':
                v_cylinder()
            elif Choice == '7':
                circumference_circle()
            elif Choice == '8':
                gst_pst()
            elif Choice == '9':
                addition()
            elif Choice == '10':
                subtraction()
            elif Choice == '11':
                multiplication()
            elif Choice == '12':
                division()
            elif Choice == '13':
                credits()
            elif Choice == '14':
                print("Bye")
                Running = False
            else:
                print("Please pick a valid number.")
        except ValueError:
            print("Invalid Input! Pick a number.")


if __name__ == "__main__":
            main()


