#mensuration calculator
print("choose the shape to be operated")
print("*"*40)
print("press 1 to operate on 3 dimensional shapes")
print("press 2 to operate on 2 dimensional shapes")
print("*"*40)
shape=int(input("enter the choosen shape:\t"))
print("*"*50)
if(shape==1):
    print("now choose the shape to operate on")
    print("press 1 for sphere")
    print("press 2 for hemisphere")
    print("press 3 for cube")
    print("press 4 for cuboid")
    print("press 5 for prism")
    print("press 6 for equilateral triangular pyramid(all sides should be equal in length )")
    print("press 7 for cylinder")
    print("press 8 for cone")
    print("*" * 50)
    choice=int(input("enter the choice:\t"))
    print("*" * 50)
    if(choice==1):
        print("please tell how you want it to be operated")
        print("enter 1 if you want to find surface area of sphere")
        print("enter 2 if you want to find the volume of the sphere ")
        operation=int(input("enter the desired operation:\t"))
        if(operation==1):
            print("enter the value of radius to find the surface area of sphere")
            r=float(input("enter the value:\t"))
            print("surface area of the sphere is:",4*3.14*r*r)
        elif(operation==2):
            r=float(input("enter the value of radius to find the volume of the sphere"))
            print("volume of the desired sphere is:\t",1.33*3.14*r*r*r)
            print("*" * 50)
        else:
            print("entered operation is invalid")
            print("*" * 50)
    elif(choice==2):
        print("*" * 50)
        print("please tell how you want it to be operated")
        print("enter 1 if you want to find total surface area of hemisphere")
        print("enter 2 if you want to find curve surface area of hemisphere")
        print("enter 3 if you want to find volume area of hemisphere")
        operation=int(input("enter the desired operation:\t"))
        if(operation==1):
            r=float(input("enter the value of radius to find the total surface area of hemisphere:\t"))
            print("total surface area of the desired hemisphere is:\t",3*3.14*r*r)
        elif(operation==2):
            r=float(input("enter the value of radius to find the curve surface area of hemisphere"))
            print("curve surface area of the desired hemisphere is:\t",2*3.14*r*r)
        elif(operation==3):
            r=float(input("enter the value of radius to find the volume of the hemisphere"))
            print("volume of the desired hemisphere is:\t ",0.67*3.14*r*r*r)
            print("*" * 50)
        else:
            print("entered operation is invalid")
            print("*" * 50)
    elif(choice==3):
        print("*" * 50)
        print("please tell how you want it to be operated")
        print("enter 1 to find the total surface area of the cube")
        print("enter 2 to find the lateral surface area of the cube")
        print("enter 3 to find the volume of the cube")
        print("*" * 50)
        operation=int(input("enter the desired operation:\t"))
        print("*" * 50)
        if(operation==1):
            side=float(input("enter the side of the cube to find the total surface area"))
            print("total surface area of the desired cube is:\t",6*side*side)
        elif(operation==2):
            side=float(input("enter the side of the cube:\t"))
            print("lateral surface area of the desired cube is:\t",4*side*side)
        elif(operation==3):
            side=float(input("enter the side of the cube"))
            print("volume of the desired cube is:\t",side*side*side)
            print("*" * 50)
        else:
            print("entered operation is invalid")
            print("*" * 50)
    elif(choice==4):
        print("*" * 50)
        print("please tell how you want it to be operated")
        print("enter 1 to find the total surface area of the cuboid")
        print("enter 2 to find the lateral surface area of the cuboid")
        print("enter 3 to find volume of the cuboid")
        print("*" * 50)
        operation=int(input("enter the desired operation"))
        print("*" * 50)
        if(operation==1):
            length=float(input("enter the lenght of the cuboid"))
            breadth=float(input("enter the breadth of the cuboid"))
            height=float(input("enter the height of the cuboid"))
            print("total surface area of the desired cuboid is:\t",2*(length*breadth+length*height+breadth*height))
        elif(operation==2):
            length=float(input("enter the length of the cuboid"))
            breadth=float(input("enter the breadth of the cuboid"))
            height=float(input("enter the height of the cuboid"))
            print("lateral surface areas of the desired cuboid is:\t",2*height(length+breadth))
        elif(operation==3):
            length = float(input("enter the length of the cuboid"))
            breadth = float(input("enter the breadth of the cuboid"))
            height = float(input("enter the height of the cuboid"))
            print("volume of the desired cuboid is:\t",length*breadth*height)
        else:
            print("entered operation in invalid")
    elif(choice==5):
        print("please tell how you want it to be operated")
        print("enter 1 to find the total surface area of the prism")
        print("enter 2 to find the lateral surface area of the prism")
        print("enter 3 to find volume of the prism")
        operation = int(input("enter the desired operation:\t"))
        if(operation==1):
            length=float(input("enter the length of the longest side of the prism:\t"))
            side=float(input("enter the side of the triangular portion:\t"))
            s=3*side/2
            area=(s*(s-side)**3)*0.5
            print("total surface area of the desired prism is:\t",3*side*length+2*area)
        elif(operation==2):
            length = float(input("enter the length of the longest side of the prism:\t"))
            side = float(input("enter the side of the triangular portion:\t"))
            print("lateral surface area of the desired prism is:\t",3*side*length)
        elif(operation==3):
            length = float(input("enter the length of the longest side of the prism"))
            side = float(input("enter the side of the triangular portion"))
            s=3*side/2
            area=(s*(s-side)**3)*0.5
            print("volume of the desired prism is:\t",area*length)
        else:
            print("entered operation is invalid")
    elif(choice==6):
        print("please tell how you want it to be operated")
        print("enter 1 to find the total surface area of the pyramid")
        print("enter 2 to find the lateral surface area of the pyramid")
        print("enter 3 to find volume of the pyramid")
        operation = int(input("enter the desired operation"))
        if(operation==1):
            side = float(input("enter the value of the side of the equilateral triangular pyramid:\t"))
            s = 3 * side / 2
            area = (s * (s - side) ** 3) * 0.5
            print("total surface area of the desired pyramid is:\t",4*area)
        elif(operation==2):
            side = float(input("enter the value of the side of the equilateral triangular pyramid:\t"))
            s = 3 * side / 2
            area = (s * (s - side) ** 3) * 0.5
            print("lateral surface area of the desired pyramid is:\t",3*area)
        elif(operation==3):
            side = float(input("enter the value of the side of the equilateral triangular pyramid:\t"))
            height=float(input("enter the height of the equilateral triangular pyramid:\t"))
            s = 3 * side / 2
            area = (s * (s - side) ** 3) * 0.5
            print("volume of the equilateral triangular pyramid is:\t",1/3*(area*height))
        else:
            print("entered operation is invalid ")
    elif(choice==7):
        print("please tell how you want it to be operated")
        print("enter 1 to find the total surface area of the cylinder")
        print("enter 2 to find the lateral surface area of the cylinder")
        print("enter 3 to find volume of the cylinder")
        print("enter 4 to find the area of the circular part of the cylinder")
        operation = int(input("enter the desired operation"))
        if(operation==1):
            length=float(input("enter the length of the cylinder:\t"))
            radius=float(input("enter the radius of the cylinder:\t"))
            boundary=2*3.14*radius
            area=3.14*(radius**2)
            print("total surface area of the desired cylinder is:\t",boundary*length+2*area)
        elif(operation==2):
            length = float(input("enter the length of the cylinder:\t"))
            radius = float(input("enter the radius of the cylinder:\t"))
            boundary = 2 * 3.14 * radius
            print("lateral surface area of the desired cylinder is:\t", boundary*length)
        elif(operation==3):
            length = float(input("enter the length of the cylinder:\t"))
            radius = float(input("enter the radius of the cylinder:\t"))
            boundary = 2 * 3.14 * radius
            area = 3.14 * (radius ** 2)
            print("volume of the desired cylinder is:\t",area*length)
        elif(operation==4):
            radius = float(input("enter the radius of the cylinder:\t"))
            print("area of the two circular portions of the cylinder is:\t", 2*3.14*radius*radius)
        else:
            print("entered operation is invalid ")
    elif(choice==8):
        print("please tell how you want it to be operated")
        print("enter 1 if you want to total find surface area of cone")
        print("enter 2 if you want to find the volume of the cone ")
        print("enter 3 to find the curve surface area of the cone ")
        operation=int(input("enter the desired operation:\t"))
        if(operation==1):
            l=float(input("enter the slant height of the cone:\t"))
            pi=3.14
            radius=float(input("enter the value of radius of the base of the cone:\t"))
            print("total surface area of the desired cone is:\t", pi*radius*(radius*l))
        elif(operation==2):
            l = float(input("enter the slant height of the cone:\t"))
            pi = 3.14
            radius = float(input("enter the value of radius of the base of the cone:\t"))
            h=(l**2-radius**2)
            print("volume of the desired cone is:\t", 1/3*pi*radius*radius*h)
        elif (operation == 3):
            l = float(input("enter the slant height of the cone:\t"))
            pi = 3.14
            radius = float(input("enter the value of radius of the base of the cone:\t"))
            print("curved surface area of the desired cone is:\t", pi*radius*l)
        else:
            print("entered operation is invalid ")
    else:
        print("entered choice is invalid ")
elif(shape==2):

    print("now choose the shape to operate on")
    print("press 1 for square")
    print("press 2 for rectangle")
    print("press 3 for triangle")
    print("press 4 for circle")
    print("press 5 for parallelogram")
    print("press 6 for trapezium")
    print("press 7 for rhombus")
    print("press 8 for semicircle")
    choice = int(input("enter the choice:\t"))
    if(choice==1):
        print("please tell how you want it to be operated")
        print("press 1 to find the area of the square\t")
        print("press 2 to find the perimeter of the square\t")
        print("press 3 to find the diagonal of the square\t")
        operation=int(input("enter the desired operation\t"))
        if(operation==1):
            side=float(input("enter the value of the side of the square to find the area:\t"))
            print("area of the desired square is:\t",side**2)
        elif(operation==2):
            side=float(input("enter the value of side to find the perimeter of the square:\t"))
            print("perimeter of the desired square is:\t",4*side)
        elif(operation==3):
            side=float(input("enter the value of side to find the diagonal of the square:\t"))
            print("diagonal of the desired square is:\t",side*((2)**0.5))
        else:
            print("entered operation is invalid")
    elif(choice==2):
        print("please tell how you want it to be operated")
        print("press 1 to find the area of the rectangle:\t")
        print("press 2 to find the perimeter of the rectangle:\t")
        print("press 3 to find the diagonal of the rectangle:\t")
        operation = int(input("enter the desired operation:\t"))
        if(operation==1):
            l=float(input("enter the value of length to find the area of the rectangle:\t"))
            b=float(input("enter the value of breadth to find the area of the rectangle:\t"))
            print("area of the desired rectangle is:\t",l*b)
        elif(operation==2):
            l = float(input("enter the value of length to find the perimeter of the rectangle:\t"))
            b = float(input("enter the value of breadth to find the perimeter of the rectangle:\t"))
            print("perimeter of the desired rectangle is:\t",2*(l+b))
        elif(operation==3):
            l = float(input("enter the value of length to find the diagonal of the rectangle:\t"))
            b = float(input("enter the value of breadth to find the diagonal of the rectangle:\t"))
            print("diagonal of the desired rectangle is:\t",((l**2)+(b**2))**0.5)
        else:
            print("entered operation is invalid")
    elif(choice==3):
        print("please tell how you want it to be operated")
        print("press 1 to find the area of the triangle ")
        print("press 2 to find the perimeter of the triangle ")
        operation = int(input("enter the desired operation:\t"))
        if(operation==1):
            ab=float(input("enter the first side of the triangle to find the area:\t"))
            bc=float(input("enter the second side of the triangle to find the area:\t"))
            ca=float(input("enter the third side of the triangle to find the area:\t"))
            s=(ab+bc+ca)/2
            print("area of the desired triangle is:\t",(s*(s-ab)*(s-bc)*(s-ca))**0.5)
        elif(operation==2):
            ab = float(input("enter the first side of the triangle to find the perimeter:\t"))
            bc = float(input("enter the second side of the triangle to find the perimeter:\t"))
            ca = float(input("enter the third side of the triangle to find the perimeter:\t"))
            print("perimeter of the desired triangle is:\t",(ab+bc+ca))
        else:
            print("entered operation is invalid")
    elif(choice==4):
        print("please tell how you want it to be operated")
        print("press 1 to find the area of the circle:\t")
        print("press 2 to find the perimeter/circumference of the circle:\t")

        operation = int(input("enter the desired operation:\t"))
        if(operation==1):
            pi=3.14
            r=float(input("enter the value of radius to find the area of the desired circle:\t"))
            print("area of the desired circle is:\t",pi*r*r)
        elif(operation==2):
            pi = 3.14
            r = float(input("enter the value of radius to find the perimeter/circumference of the desired circle:\t"))
            print("perimeter/circumference of the desired circle is:\t",2*pi*r)
        else:
            print("entered operation is invalid")
    elif(choice==5):
        print("please tell how you want it to be operated")
        print("press 1 to find the area of the parallelogram:\t")
        print("press 2 to find the perimeter of the parallelogram:\t")

        operation = int(input("enter the desired operation:\t"))
        if(operation==1):
            b=float(input("enter the value of base of the parallelogram to find the area:\t"))
            h=float(input("enter the value of height of the parallelogram to find the area:\t "))
            print("area of the desired parallelogram is:\t",b*h)
        elif(operation==2):
            l=float(input("enter the length of the longest parallel side:\t"))
            b=float(input("enter the length of the shorter parallel side:\t"))
            print("perimeter of the desired parallelogram is:\t",2*(l+b))
        else:
            print("entered operation is invalid")
    elif(choice==6):
        print("please tell how you want it to be operated")
        print("press 1 to find the area of the trapezium:\t")
        print("press 2 to find the perimeter of the trapezium:\t")
        operation = int(input("enter the desired operation:\t"))
        if(operation==1):
            a=float(input("enter the length of first parallel side:\t"))
            b=float(input("enter the length of second parallel side:\t"))
            h=float(input("enter the height of the trapezium:\t"))
            print("area of the desired trapezium is:\t",0.5*(a+b)*h)
        elif(operation==2):
            a=float(input("enter the length of the first side:\t"))
            b=float(input("enter the length of the second side:\t"))
            c=float(input("enter the length of the third side:\t"))
            d=float(input("enter the length of the fourth side:\t"))
            print("perimeter of the desired trapezium is:\t",a+b+c+d)
        else:
            print("entered operation is invalid")
    elif(choice==7):
        print("please tell how you want it to be operated")
        print("press 1 to find the area of the rhombus:\t")
        print("press 2 to find the diagonal of the rhombus:\t")
        print("press 3 to find the side of the rhombus:\t")
        print("press 4 to find the perimeter of the rhombus:\t")

        operation = int(input("enter the desired operation:\t"))
        #formula to find side from given diaognal
        #side=0.5*root under( diaogonal1**2+diagonal2**2)
        #area=0.5*diagonal1*diagonal2
        if(operation==1):
            da=float(input("enter the value of d1 to find the area of the rhombus:\t"))
            db=float(input("enter the value of d2 to find the area of the rhombus:\t"))
            print("area of the desired rhombus is:\t",0.5*da*db)
        elif(operation==2):
            da=float(input("enter the value of given diagonal:\t"))
            a=float(input("enter the side of the rhombus:\t"))
            print("value of the desired diagonal is:\t",0.5*(4*(a**2)-da**2))


        elif(operation==3):
            da=float(input("enter the length of the first diagonal:\t"))
            db=float(input("enter the length of the second diagonal:\t"))
            print("sides of the desired rhombus are:\t",0.5*((da*da+db*db)**0.5))
        elif(operation==4):
            side=float(input("enter the side of the rhombus to find the perimeter:\t"))
            print("perimeter of the desired rhombus is:\t",4*side)
        else:
            print("entered operation is invalid")
    elif(choice==8):
        print("enter 1 to find the area of the semicircle")
        print("enter 2 to find the perimeter of the semicircle")
        print("enter 3 to find the perimeter of the curve of the semicircle")
        print("enter 4 to find the area of the semicircle")
        operation = int(input("enter the desired operation:\t"))
        pi=3.14
        if(operation==1):
            r=float(input("enter the value of the radius:\t"))
            print("area of the desired semicircle is:\t",pi*r*r)
        elif(operation==2):
            r = float(input("enter the value of the radius:\t"))
            print("perimeter of the desired semicircle is:\t",(pi*r)+(2*r))
        elif(operation==3):
            r = float(input("enter the value of the radius:\t"))
            print("perimeter of the curve of the semicircle is:\t",pi*r)
        elif(operation==4):
            r = float(input("enter the value of the radius:\t"))
            print("area of the semicircle is:\t",0.5*pi*r**2)
        else:
            print("entered operation is invalid")
    else:
        print("entered choice is invalid")
else:
    print("entered shape is undefined")












































































