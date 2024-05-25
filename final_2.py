import turtle

def draw_pifagoras_tree(branch_len, level):
    if level == 0:
        return
    turtle.forward(branch_len)
    turtle.left(45)
    draw_pifagoras_tree(0.7 * branch_len, level - 1)
    turtle.right(90)
    draw_pifagoras_tree(0.7 * branch_len, level - 1)
    turtle.left(45)
    turtle.backward(branch_len)

def main():
    turtle.speed(0)  # Set the speed of drawing (0 is the fastest)
    turtle.left(90)  # Adjust orientation
    
    # User input for recursion level
    level = int(input("Enter the recursion level (integer value): "))
    
    draw_pifagoras_tree(100, level)  # Call the recursive function with user-specified level
    turtle.hideturtle()  # Hide the turtle cursor
    turtle.done()  # Finish drawing

if __name__ == "__main__":
    main()
