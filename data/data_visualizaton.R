# Erich Ostendarp

# imports
library(dplyr)
library(ggplot2)

# read data
rvr <- read.csv('data/RvR.csv', sep='\t')
ava <- read.csv('data/AvA.csv', sep='\t')
rva <- read.csv('data/RvA.csv', sep='\t')
mva <- read.csv('data/MvA.csv', sep='\t')


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
g1 <- ggplot(rvr, aes(x=game_number, y=agent_decision_time, color=agent_color)) + geom_point()
g2 <- ggplot(ava, aes(x=game_number, y=agent_decision_time, color=agent_color)) + geom_point()

g3 <- ggplot(rva, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point()
g4 <- ggplot(mva, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point()


# decision times

# color
g5 <- ggplot(rvr, aes(x=agent_decision_time, fill=agent_color)) + geom_histogram() + facet_wrap(~agent_color)
g6 <- ggplot(ava, aes(x=agent_decision_time, fill=agent_color)) + geom_histogram() + facet_wrap(~agent_color)

# agent
g7 <- ggplot(rva, aes(x=agent_decision_time, fill=agent_type)) + geom_histogram() + facet_wrap(~agent_type)
g8 <- ggplot(mva, aes(x=agent_decision_time, fill=agent_type)) + geom_histogram() + facet_wrap(~agent_type)


# num moves

# color
g9 <- ggplot(rvr, aes(x=agent_num_moves)) + geom_histogram()
g10 <- ggplot(ava, aes(x=agent_num_moves)) + geom_histogram()

# agent
g11 <- ggplot(rva, aes(x=agent_num_moves)) + geom_histogram()
g12 <- ggplot(mva, aes(x=agent_num_moves)) + geom_histogram()


# decision time vs. wins
g13 <- ggplot(rvr, aes(x=game_result, y=agent_decision_time)) + geom_histogram(stat='identity')
g14 <- ggplot(ava, aes(x=game_result, y=agent_decision_time)) + geom_histogram(stat='identity')

g15 <- ggplot(mva, aes(x=game_result, y=agent_decision_time, fill=agent_type)) + geom_histogram(stat='identity') + facet_wrap(~agent_type)


# num moves vs. wins
g16 <- ggplot(rvr, aes(x=game_result, y=agent_num_moves)) + geom_histogram(stat='identity')
g17 <- ggplot(ava, aes(x=game_result, y=agent_num_moves)) + geom_histogram(stat='identity')

g18 <- ggplot(mva, aes(x=game_result, y=agent_num_moves, fill=agent_type)) + geom_histogram(stat='identity') + facet_wrap(~agent_type)


# num moves vs. decision time
g19 <- ggplot(rvr, aes(x=agent_num_moves, y=agent_decision_time, color=agent_color)) + geom_point() + geom_smooth()
g20 <- ggplot(ava, aes(x=agent_num_moves, y=agent_decision_time, color=agent_color)) + geom_point() + geom_smooth()

g21 <- ggplot(rva, aes(x=agent_num_moves, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()
g22 <- ggplot(mva, aes(x=agent_num_moves, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

g1
g2
g3
g4

g5
g6
g7
g8
g9
g10
g11
g12
g13
g14
g15
g16
g17
g18
g19
g20
g21
g22