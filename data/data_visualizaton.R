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
A1vA3 <- read.csv('data/A1vA3.csv', sep='\t')
A2vA3 <- read.csv('data/A2vA3.csv', sep='\t')

# Transposition Tables
A2vA2T_1 <- read.csv('data/A2vA2T_1.csv', sep='\t')
A2vA2T_2 <- read.csv('data/A2vA2T_2.csv', sep='\t')
A2vA2T_3 <- read.csv('data/A2vA2T_3.csv', sep='\t')
A2vA2T_4 <- read.csv('data/A2vA2T_4.csv', sep='\t')
A2vA2T_5 <- read.csv('data/A2vA2T_5.csv', sep='\t')
A2vA2T_6 <- read.csv('data/A2vA2T_6.csv', sep='\t')
A2vA2T_7 <- read.csv('data/A2vA2T_7.csv', sep='\t')
A2vA2T <- rbind(A2vA2T_1, A2vA2T_2, A2vA2T_3, A2vA2T_4, A2vA2T_5, A2vA2T_6, A2vA2T_7)

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
RvA2 <- read.csv('data/RvA2.csv', sep='\t')
