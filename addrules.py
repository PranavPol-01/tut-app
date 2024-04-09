import sqlite3

def create_table():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Badminton(
        sport_name TEXT NOT NULL,                  
        sport_info TEXT NOT NULL,
        page2 TEXT NOT NULL,
        page3 TEXT,
        page4 TEXT,
        page5 TEXT,
        media1 BLOB,
        media2 BLOB,
        media3 BLOB,
        media4 BLOB,
        media5 BLOB
    )""")
    conn.commit()
    conn.close()
    print("Database created successfully!")
create_table()
def add_sport(sport_name):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Badminton
                    VALUES("Badminton", "Badminton is one of the most popular sports in the world, with a passionate fan following around the globe.\n\nIt is also one of the biggest draws at multi-sport spectacles like the Olympics.\n\nA regular fixture since the Barcelona 1992 Olympics, badminton now has five disciplines at the Games after mixed doubles was introduced at Atlanta 1996.\n\nChina has since emerged as the sport's dominant force with a total of 20 golds, 12 silvers and 15 bronze medals at the Olympics. Indonesia are second with eight golds, six silvers and seven bronze medals.\n\nWhile badminton is most popular in Asia, it also attracts great interest in Europe with players from Denmark among those regularly challenging for top honours.\n\nWant to learn more about badminton? Here’s a look at the rules and equipment you need to play.", "As outlined by the Badminton World Federation (BWF), here is a simplified rundown of the rules of badminton.

Badminton can be played either as singles or doubles. In singles, there are two players competing against each other. In doubles, two pairs of players form teams and compete against each other, resulting in a game of four players.Badminton scoring system
All singles and doubles matches are the best-of-three games. The first side to 21 points wins a game.\nA shuttlecock is hit over the net and into the opponent's court with a racquet.\n\nA point is scored on every serve and awarded to whichever side wins the rally. The winning side gets the next serve.\n\nIf the score is 20-20, a side must win by two clear points to win the game. If it reaches 29-29, the first to get their 30th point wins.", "Change of ends in badminton\n\n\nIn badminton, players are required to change ends under specific conditions. They should change ends at the conclusion of the first game. If a third game is required, they should also change ends at the end of the second game. In the third game, the change of ends occurs when one side reaches a score of 11 points.\n\n\n Winning a point in badminton\n\n\nA point is won if the birdie (shuttlecock) hits the ground in the opponent’s half of the court, including the lines. A point can therefore be conceded if a shot goes outside the court boundaries, if the birdie hits the net or passes through/under it, or if a player strikes the birdie twice with their racket.

Players must wait for the birdie to cross the net before playing a shot, and while you can follow through over it, touching the net with your body or racket results in a point being conceded.", "How to serve in badminton
The birdie must be hit below waist height, with players serving diagonally into their opponent’s service box. Both players must remain stationary until the serve is made.

As per badminton singles rules, the server starts from the right service court, and will serve from that side every time they have an even amount of points. A player serves from the left every time they have an odd amount of points.

Each player will retain serve for as long as they keep winning points.

In badminton doubles, the server will start on the right-hand side and keep serving, while alternating sides with their team-mate, so long as they keep winning points.

If the receiving side takes the point, they assume serve. Going forward, the player who did not initially serve for each team will only assume the service once their side has won a point as the receiving side.", "What is a badminton court’s dimensions?
In singles, a badminton court is 13.41m (44ft) long and 5.18m (17ft) wide. The width extends to 6.1m (20ft) in doubles.

The net is 1.55m (5ft 1in) high at the ends and 1.52m high (5ft) where it dips in the middle.

A serve must pass the short service line, which is 1.98m (6.5ft) from the net.

Beyond the short service line, there is a line which runs down the middle to split the left and right service courts. There is also a doubles service line 0.76m (2.5ft) in from the baseline.

That means each service court (four in total) is 3.96m (13ft) long and 2.59m (8.5ft) wide.", NULL , "assets\\shots.png", NULL, "assets\\badminton-drive-serve-like-a-boss-badmintonserve.mp4", "assets\\dimensions.png")""")

    conn.commit()   
    conn.close()
    print("Sport added successfully!")

add_sport('Badminton')

def create_table_football():
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Football(
        sport_name TEXT NOT NULL,                  
        sport_info TEXT NOT NULL,
        page2 TEXT NOT NULL,
        page3 TEXT,
        page4 TEXT,
        page5 TEXT,
        media1 BLOB,
        media2 BLOB,
        media3 BLOB,
        media4 BLOB,
        media5 BLOB
    )""")
    conn.commit()
    conn.close()
    print("Database created successfully!")
create_table_football()

def add_sport(sport_name):
    conn = sqlite3.connect('rules.db')
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Football
                    VALUES("Football", "Football is a team sport played with a spherical ball between two teams of 11 players. It is played by approximately 250 million players in over 200 countries and dependencies, making it the world's most popular sport. The game is played on a rectangular field called a pitch with a goal at each end. The object of the game is to outscore the opposition by moving the ball beyond the goal line into the opposing goal. The team with the higher number of goals wins the game. The Laws of the Game were originally codified in England by The Football Association in 1863. Association football is governed internationally by the International Federation of Association Football (FIFA: Fédération Internationale de Football Association), which organises World Cups", "The aim of football is to score more goals then your opponent in a 90 minute playing time frame. The match is split up into two halves of 45 minutes. After the first 45 minutes players will take a 15 minute rest period called half time. The second 45 minutes will resume and any time deemed fit to be added on by the referee (injury time) will be accordingly.\nEach team consists of 11 players. These are made up of one goalkeeper and ten outfield players.\nEssentially the equipment that is needed for a soccer match is pitch and a football. Additionally players can be found wearing studded football boots, shin pads and matching strips. The goalkeepers will additionally wear padded gloves as they are the only players allowed to handle the ball. Each team will have a designated captain.","The game starts with a kick-off in the centre circle. The team that wins the coin toss will choose which end to attack in the first half and will kick off. The opposing team must be outside of the centre circle and the team kicking off must be in their own half. The ball must be played forward and cannot be played back. The game is officiated by a referee and two linesman. The referee has full control of the match and his decisions are final. The linesman will assist the referee in certain decisions such as whether the ball has gone out of play, offside decisions and fouls. The game is split up into two halves of 45 minutes. After the first half is completed there is a 15 minute rest period. Any time deemed fit to be added on by the referee (injury time) will be added on at the end of each half for stoppages in play. The game will finish after 90 minutes including injury time unless the referee indicates otherwise. If the game is a draw after 90 minutes then the game will go into extra time and penalties if necessary.\nThe offside rule is a rule in football which states that if a player is in an offside position when the ball is played to him or touched by a team mate, he may not become actively involved in the play. A player is in an offside position if he is nearer to his opponents goal line than both the ball and the second last opponent when his team mate plays the ball to him. The offside rule is in place to stop players from simply standing by the oppositions goal waiting for the ball to be played to them. The rule is in place to encourage attacking play and to stop players from simply goal hanging. The offside rule is one of the hardest rules to get right in football and is often the cause of controversy.\nThe penalty rule is a rule in football which states that if a player commits a foul in the 18 yard box a penalty will be awarded. The player who has been fouled will take the penalty from 12 yards out and will have a free shot at goal with only the goalkeeper to beat. The penalty rule is in place to stop players from committing fouls in the 18 yard box and to stop players from simply hacking down an opponent when he is through on goal. The penalty rule is one of the most important rules in football and is often the cause of controversy.","To score the ball must go into your opponent’s goal. The whole ball needs to be over the line for it to be a legitimate goal. A goal can be scored with any part of the body apart from the hand or arm up to the shoulder. The goal itself consists of a frame measuring 8 feet high and 8 yards wide.\n The whole ball must cross the goal line for it to constitute as a goal.
For fouls committed a player could receive either a yellow or red card depending on the severity of the foul; this comes down to the referee’s discretion. The yellow is a warning and a red card is a dismissal of that player. Two yellow cards will equal one red. Once a player is sent off then they cannot be replaced.","The dimensions of a football pitch vary depending on the age group but for a full size pitch the dimensions are 105m x 68m. The penalty area is 16.5m x 40.3m. The penalty spot is 11m from the goal line. The goal area is 5.5m x 18.3m. The goal is 7.32m x 2.44m. The centre circle has a radius of 9.15m. The corner area is a quarter circle with a radius of 1m. The pitch is split into two halves and the halfway line is in the middle of the pitch. The pitch is split into two halves and the halfway line is in the middle of the pitch. The pitch is split into two halves and the halfway line is in the middle of the pitch.", "assets\\fbmedia1.png" , "assets\\fbpage2.png", NULL, "assets\\3-control-skills-to-practice-first-football-soccer-shorts.mp4", "assets\\fbmrdia5.png")""")
    conn.commit()
    conn.close()
    print("Sport added successfully!")

add_sport('Football')

