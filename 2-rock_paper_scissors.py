
## get the highest score

def part1():

    scores = dict(
            X=1, # rock
            Y=2, # paper
            Z=3, # scissors
            A=1,
            B=2,
            C=3,
            win=6,
            loss=0,
            draw=3,
    )

    total_score = 0
    with open('2-input.txt') as file:  
        for line in file.readlines():    
            you, him = scores[line[2]], scores[line[0]]
            diff = you - him
            if diff == 0:
                total_score += scores['draw'] + you
            elif (diff == 1) or (diff == -2):
                total_score += scores['win'] + you
            else:
                total_score += scores['loss'] + you            
    return total_score
        

def part2():

    scores = dict(
            X='loss', # win
            Y='draw', # draw
            Z='win',  # loss
            A=1,
            B=2,
            C=3,
            win=6,
            loss=0,
            draw=3,
    )

    total_score = 0
    with open('2-input.txt') as file:  
        for line in file.readlines():    
            outcome = scores[line[2]]  # string for outcome
            him = scores[line[0]]      # int for scores

            if outcome == 'draw':
                total_score += scores[outcome] + him
            elif outcome == 'win':
                me = him + 1
                if him == 3: # he chose scissors
                    me = 1
                total_score += scores[outcome] + me
            else:
                me = him - 1
                if him == 1: # he chose rock
                    me = 3
                total_score += scores[outcome] + me

        return total_score


print(part2())
