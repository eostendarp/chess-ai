# Erich Ostendarp

# imports
library(dplyr)
library(ggplot2)

# read data
rvr <- read.csv('data/RvR.csv', sep='\t')
ava <- read.csv('data/AvA.csv', sep='\t')
rva <- read.csv('data/RvA.csv', sep='\t')
mva <- read.csv('data/MvA.csv', sep='\t')

# avh <- read.csv('data/AvH', sep='\t')
# avp <- read.csv('data/AvP', sep='\t')
# avc <- read.csv('data/AvC', sep='\t')
# hvh <- read.csv('data/HvH', sep='\t')
# pvp <- read.csv('data/PvP', sep='\t')
# cvc <- read.csv('data/CvC', sep='\t')

print('color win rate')

print('white random agent:')
sum(filter(rvr, agent_color=='white' & game_result==1)$game_result) / 100
print('black random agent:')
sum(filter(rvr, agent_color=='black' & game_result==1)$game_result) / 100

print('white alphabeta agent:')
sum(filter(mva, agent_color=='white' & game_result==1)$game_result) / 100
print('black alphabeta agent:')
sum(filter(mva, agent_color=='black' & game_result==1)$game_result) / 100


print('agent win rate')

print('white random agent:')
sum(filter(rva, agent_type=='random' & game_result==1)$game_result) / 100
print('black alphabeta agent:')
sum(filter(rva, agent_type=='alphabeta' & game_result==1)$game_result) / 100

print('white minimax agent:')
sum(filter(mva, agent_type=='minimax' & game_result==1)$game_result) / 100
print('black alphabeta agent:')
sum(filter(mva, agent_type=='alphabeta' & game_result==1)$game_result) / 100


# check data for anomalies
ggplot(rvr, aes(x=game_number, y=agent_decision_time, color=agent_color)) + geom_point()
ggplot(ava, aes(x=game_number, y=agent_decision_time, color=agent_color)) + geom_point()

ggplot(rva, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point()
ggplot(mva, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point()


# decision times

# color
ggplot(rvr, aes(x=agent_decision_time, fill=agent_color)) + geom_histogram() + facet_wrap(~agent_color)
ggplot(ava, aes(x=agent_decision_time, fill=agent_color)) + geom_histogram() + facet_wrap(~agent_color)

# agent
ggplot(rva, aes(x=agent_decision_time, fill=agent_type)) + geom_histogram() + facet_wrap(~agent_type)
ggplot(mva, aes(x=agent_decision_time, fill=agent_type)) + geom_histogram() + facet_wrap(~agent_type)


# Different distributions of moves for different agents
ggplot(rvr, aes(x=agent_num_moves)) + geom_histogram()
ggplot(ava, aes(x=agent_num_moves)) + geom_histogram()


# decision time vs. wins
ggplot(mva, aes(x=game_result, y=agent_decision_time, fill=agent_type)) + geom_histogram(stat='identity') + facet_wrap(~agent_type)


# num moves vs. wins
ggplot(rvr, aes(x=game_result, y=agent_num_moves)) + geom_histogram(stat='identity')
ggplot(ava, aes(x=game_result, y=agent_num_moves)) + geom_histogram(stat='identity')

ggplot(mva, aes(x=game_result, y=agent_num_moves, fill=agent_type)) + geom_histogram(stat='identity') + facet_wrap(~agent_type)


# num moves vs. decision time
ggplot(rvr, aes(x=agent_num_moves, y=agent_decision_time, color=agent_color)) + geom_point() + geom_smooth()
ggplot(ava, aes(x=agent_num_moves, y=agent_decision_time, color=agent_color)) + geom_point() + geom_smooth()

ggplot(rva, aes(x=agent_num_moves, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()
ggplot(mva, aes(x=agent_num_moves, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()


# Transposition Tables
avat <- read.csv('data/AvAT.csv', sep='\t')
ggplot(avat, aes(x=game_number, y=agent_decision_time, color=agent_color)) + geom_point() + geom_smooth()


# Different Depths
a1va2 <- read.csv('data/A1vA2.csv', sep='\t')
ggplot(a1va2, aes(x=game_number, y=agent_decision_time, color=agent_color)) + geom_point()

a1va3 <- read.csv('data/A1vA3.csv', sep='\t')
ggplot(a1va3, aes(x=game_number, y=agent_decision_time, color=agent_color)) + geom_point()

a2va3 <- read.csv('data/A2vA3.csv', sep='\t')
ggplot(a2va3, aes(x=game_number, y=agent_decision_time, color=agent_color)) + geom_point()
