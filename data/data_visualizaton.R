# Erich Ostendarp

# imports
library(dplyr)
library(ggplot2)


# Baseline
RvR <- read.csv('data/RvR.csv', sep='\t')
ggplot(RvR, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_color)) +
  ggtitle("Random Agent Vs. Random Agent") +
  labs(x="Game Number", y="Decision Time", color="Agent Type") +
  scale_color_manual(labels=c("Black Random Agent", "White Random Agent"), values=c("#F8766D", "#00BFC4"))


A2vA2 <- read.csv('data/A2vA2.csv', sep='\t')
ggplot(A2vA2, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_color)) +
  ggtitle("AlphaBeta Depth 2 Vs. AlphaBeta Depth 2") +
  labs(x="Game Number", y="Decision Time", color="Agent Type") +
  scale_color_manual(labels=c("Black AlphaBeta Depth 2", "White AlphaBeta Depth 2"), values=c("#F8766D", "#00BFC4"))


H2vH2 <- read.csv('data/H2vH2.csv', sep='\t')
ggplot(H2vH2, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_color)) +
  ggtitle("History Depth 2 Vs. History Depth 2") +
  labs(x="Game Number", y="Decision Time", color="Agent Type") +
  scale_color_manual(labels=c("Black History Depth 2", "White History Depth 2"), values=c("#F8766D", "#00BFC4"))


P2vP2 <- read.csv('data/P2vP2.csv', sep='\t')
ggplot(P2vP2, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_color)) +
  ggtitle("Principle-Variation Depth 2 Vs. Principle-Variation Depth 2") +
  labs(x="Game Number", y="Decision Time", color="Agent Type") +
  scale_color_manual(labels=c("Black Principle-Variation Depth 2", "White Principle-Variation Depth 2"), values=c("#F8766D", "#00BFC4"))


C2vC2 <- read.csv('data/C2vC2.csv', sep='\t')
ggplot(C2vC2, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_color)) +
  ggtitle("Combined Depth 2 Vs. Combined Depth 2") +
  labs(x="Game Number", y="Decision Time", color="Agent Type") +
  scale_color_manual(labels=c("Black Combined Depth 2", "White Combined Depth 2"), values=c("#F8766D", "#00BFC4"))



# Depth Performance
A1vA2 <- read.csv('data/A1vA2.csv', sep='\t')
ggplot(A1vA2, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_type)) +
  ggtitle("Decision Time and Game Number") +
  labs(x="Game Number", y="Decision Time (Seconds)", color="Agent Type") +
  scale_color_manual(labels=c("AlphaBeta Depth 1", "AlphaBeta Depth 2"), values=c("#F8766D", "#00BFC4"))

grouped_A1vA2 <- group_by(A1vA2, agent_type) %>%
  mutate(cum_wins=cumsum(game_result))

ggplot(grouped_A1vA2, aes(x=game_number, y=cum_wins)) +
  geom_bar(stat='identity', position='identity', aes(fill=agent_type), alpha=.6) +
  ggtitle("Win Density") +
  labs(x="Game Number", y="Cumulative Game Results (Wins - Losses)", fill="Agent Type") +
  scale_fill_manual(labels=c("AlphaBeta Depth 1", "AlphaBeta Depth 2"), values=c("#F8766D", "#00BFC4"))


A1vA3 <- read.csv('data/A1vA3.csv', sep='\t')
ggplot(A1vA3, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_type)) +
  ggtitle("Decision Time and Game Number") +
  labs(x="Game Number", y="Decision Time (Seconds)", color="Agent Type") +
  scale_color_manual(labels=c("AlphaBeta Depth 1", "AlphaBeta Depth 3"), values=c("#F8766D", "#00BFC4"))

grouped_A1vA3 <- group_by(A1vA3, agent_type) %>%
  mutate(cum_wins=cumsum(game_result))

ggplot(grouped_A1vA3, aes(x=game_number, y=cum_wins)) +
  geom_bar(stat='identity', position='identity', aes(fill=agent_type), alpha=.6) +
  ggtitle("Win Density") +
  labs(x="Game Number", y="Cumulative Game Results (Wins - Losses)", fill="Agent Type") +
  scale_fill_manual(labels=c("AlphaBeta Depth 1", "AlphaBeta Depth 3"), values=c("#F8766D", "#00BFC4"))


A2vA3 <- read.csv('data/A2vA3.csv', sep='\t')
ggplot(A2vA3, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_type)) +
  ggtitle("Decision Time and Game Number") +
  labs(x="Game Number", y="Decision Time (Seconds)", color="Agent Type") +
  scale_color_manual(labels=c("AlphaBeta Depth 2", "AlphaBeta Depth 3"), values=c("#F8766D", "#00BFC4"))

grouped_A2vA3 <- group_by(A2vA3, agent_type) %>%
  mutate(cum_wins=cumsum(game_result))

ggplot(grouped_A2vA3, aes(x=game_number, y=cum_wins)) +
  geom_bar(stat='identity', position='identity', aes(fill=agent_type), alpha=.6) +
  ggtitle("Win Density") +
  labs(x="Game Number", y="Cumulative Game Results (Wins - Losses)", fill="Agent Type") +
  scale_fill_manual(labels=c("AlphaBeta Depth 2", "AlphaBeta Depth 3"), values=c("#F8766D", "#00BFC4"))



# Transposition Tables
A2vA2T <- read.csv('data/A2vA2T.csv', sep='\t')
grouped_A2vA2T <- group_by(A2vA2T, game_number, agent_type) %>%
  summarise(mean_agent_decision_time=mean(agent_decision_time))

ggplot(grouped_A2vA2T, aes(x=game_number, y=mean_agent_decision_time)) +
  geom_point(aes(color=agent_type)) +
  geom_smooth(aes(color=agent_type)) +
  ggtitle("Average Decision Time and Game Number") +
  labs(x="Game Number", y="Average Decision Time (Seconds)", color="Agent Type") +
  scale_color_manual(labels=c("AlphaBeta Depth 2", "AlphaBeta Depth 2 w/\nTransposition Tables"), values=c("#F8766D", "#00BFC4"))



# Performance
M2vA2 <- read.csv('data/M2vA2.csv', sep='\t')
ggplot(M2vA2, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_type)) +
  geom_smooth(aes(color=agent_type)) +
  ggtitle("Decision Time and Game Number") +
  labs(x="Game Number", y="Decision Time (Seconds)", color="Agent Type") +
  scale_color_manual(labels=c("AlphaBeta Depth 2", "Minimax Depth 2"), values=c("#F8766D", "#00BFC4"))

grouped_M2vA2 <- group_by(M2vA2, agent_type) %>%
  mutate(cum_wins=cumsum(game_result))

ggplot(grouped_M2vA2, aes(x=game_number, y=cum_wins)) +
  geom_bar(stat='identity', position='identity', aes(fill=agent_type), alpha=.6) +
  ggtitle("Win Density") +
  labs(x="Game Number", y="Cumulative Game Results (Wins - Losses)", fill="Agent Type") +
  scale_fill_manual(labels=c("AlphaBeta Depth 2", "Minimax Depth 2"), values=c("#F8766D", "#00BFC4"))


RvA2 <- read.csv('data/RvA2.csv', sep='\t')
ggplot(RvA2, aes(x=game_number, y=agent_decision_time)) +
  geom_point(aes(color=agent_type)) +
  geom_smooth(aes(color=agent_type)) +
  ggtitle("Decision Time and Game Number") +
  labs(x="Game Number", y="Decision Time (Seconds)", color="Agent Type") +
  scale_color_manual(labels=c("AlphaBeta Depth 2", "Random"), values=c("#F8766D", "#00BFC4"))

grouped_RvA2 <- group_by(RvA2, agent_type) %>%
  mutate(cum_wins=cumsum(game_result))

ggplot(grouped_RvA2, aes(x=game_number, y=cum_wins)) +
  geom_bar(stat='identity', position='identity', aes(fill=agent_type), alpha=.6) +
  ggtitle("Win Density") +
  labs(x="Game Number", y="Cumulative Game Results (Wins - Losses)", fill="Agent Type") +
  scale_fill_manual(labels=c("AlphaBeta Depth 2", "Random"), values=c("#F8766D", "#00BFC4"))