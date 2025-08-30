from turtle import Turtle, Screen
import paddles
import ball
import time
import score

#Initalizing the Screen
screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

#Makeing Paddles and a ball
r_paddle=paddles.Paddles(goto=(350,0))
l_paddle=paddles.Paddles(goto=(-350,0))
the_ball=ball.Ball()
the_score=score.Score()
the_score.display_score()
speed=0.1

game_on=True



while game_on:
    screen.update()

    #Move the ball
    the_ball.goto(the_ball.xcor()+the_ball.x_move , the_ball.ycor()+the_ball.y_move)        

    # if the ball Hits r_paddle     
    if the_ball.xcor()>=325 and (the_ball.distance(r_paddle) <= 55) :
        speed*=0.8
        the_ball.x_move*=-1
    
    # if the ball Hits l_paddle     
    if (the_ball.xcor()<=-325) and (the_ball.distance(l_paddle)<= 55 ) :
        speed*=0.8
        the_ball.x_move*=-1 
    
    #if the ball didn't hit the r_paddle 
    if (the_ball.xcor()>=400):
        the_ball.set_ball( )
        speed=0.1
        the_score.add_left_score()
        the_score.display_score()
        the_ball.x_move*=-1

    #if the ball didn't hit the l_paddle
    elif (the_ball.xcor()<=-400):
        the_ball.set_ball( ) 
        speed=0.1
        the_score.add_right_score()
        the_score.display_score()
        the_ball.x_move*=-1





    #set Y's limit range
    if (the_ball.ycor()>280) or (the_ball.ycor()<-280):
        the_ball.y_move*=-1
        
        
    screen.update()
    
    #Move the Right paddle
    screen.listen()
    screen.onkey(r_paddle.goup,"Up")
    screen.onkey(r_paddle.godown,"Down")
    
    #Move the Left paddle
    screen.onkey(l_paddle.goup,"w")
    screen.onkey(l_paddle.godown,"s")
    
    #sleep the loop

    time.sleep(speed)

screen.exitonclick()