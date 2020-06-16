import math
print("****This is Voting System****")

candidates = []
cwithVotes = {}
totalContenstent = 0
voterIds = {}
totalVoters = 0


def take_all_voters():
    global totalVoters
    global voterIds
    n = int(input("enter total voter ids: "))
    totalVoters = n
    print("enter the voterIds: ")
    while n:
        vid = input()
        voterIds[vid] = 1
        n -= 1


def takeNames():
    """ this take input as name of candidates"""
    global totalContenstent
    global candidates
    global cwithVotes
    n = int(input("enter how many Contestents: "))
    totalContenstent = n
    print("enter "+str(n)+" Names: ")
    while n:
        name = input()
        candidates.append(name)
        cwithVotes[name] = 0
        n -= 1


def takeVote():
    global voterIds
    global cwithVotes
    global candidates
    ith = int(input())
    vid = input("enter your id: ")
    x = voterIds.get(vid, -1)
    if x == -1:
        print("invalid id")
    elif x == 0:
        print("you have voted already")
    else:
        voterIds[vid] = 0
        cwithVotes[candidates[ith]] += 1
        print("voting successful")


def poll():
    global totalContenstent
    global candidates
    print(totalContenstent)
    for i in range(totalContenstent):
        print("---\t\t\tenter "+str(i)+" for "+candidates[i]+" ----")

    status = 1

    while status == 1:
        takeVote()
        print("enter 0 for exit any other key for continue: ")
        status = int(input())


def staticsOfPolling():
    global voterIds
    global totalVoters
    global cwithVotes
    totalPolled = 0
    for i, j in voterIds.items():
        if j == 0:
            totalPolled += 1

    print(
        f"total polled = {totalPolled} and total Votes = {totalVoters} and polling percentage : {totalPolled/totalVoters * 100}")
    winnerId = -1
    maxVotes = 0
    for x, y in cwithVotes.items():
        print(x+" got "+str(y)+"votes ")
        if y > maxVotes:
            winnerId = x
            maxVotes = y
    print(
        f"winner is {winnerId} with {maxVotes} and {maxVotes/totalPolled * 100} percentage votes ")


if __name__ == '__main__':
    print("voters data: ")
    take_all_voters()
    print("Candidates Data: ")
    takeNames()
    print("polling starts..")
    poll()
    staticsOfPolling()
