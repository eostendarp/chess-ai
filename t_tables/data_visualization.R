# Erich

library(dplyr)
library(ggplot2)

## Random

# AVL
random_avl_1 <- read.csv('t_tables/data/random_avl_1.csv')
random_avl <- rbind(random_avl_1)

ggplot(random_avl, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Hash
random_hash_1 <- read.csv('t_tables/data/random_hash_1.csv')
random_hash <- rbind(random_hash_1)

ggplot(random_hash, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# RB
random_rb_1 <- read.csv('t_tables/data/random_rb_1.csv')
random_rb <- rbind(random_rb_1)

ggplot(random_rb, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Splay
random_splay_1 <- read.csv('t_tables/data/random_splay_1.csv')
random_splay <- rbind(random_splay_1)

ggplot(random_splay, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Trie
random_trie_1 <- read.csv('t_tables/data/random_trie_1.csv')
random_trie <- rbind(random_trie_1)

ggplot(random_trie, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

## Minimax

# AVL
minimax_avl_1 <- read.csv('t_tables/data/minimax_avl_1.csv')
minimax_avl <- rbind(minimax_avl_1)

ggplot(minimax_avl, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Hash
minimax_hash_1 <- read.csv('t_tables/data/minimax_hash_1.csv')
minimax_hash <- rbind(minimax_hash_1)

ggplot(minimax_hash, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# RB
minimax_rb_1 <- read.csv('t_tables/data/minimax_rb_1.csv')
minimax_rb <- rbind(minimax_rb_1)

ggplot(minimax_rb, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Splay
minimax_splay_1 <- read.csv('t_tables/data/minimax_splay_1.csv')
minimax_splay <- rbind(minimax_splay_1)

ggplot(minimax_splay, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Trie
minimax_trie_1 <- read.csv('t_tables/data/minimax_trie_1.csv')
minimax_trie <- rbind(minimax_trie_1)

ggplot(minimax_trie, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()


## AlphaBeta

# AVL
alpha_beta_avl_1 <- read.csv('t_tables/data/alpha_beta_avl_1.csv')
alpha_beta_avl <- rbind(alpha_beta_avl_1)

ggplot(alpha_beta_avl, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Hash
alpha_beta_hash_1 <- read.csv('t_tables/data/alpha_beta_hash_1.csv')
alpha_beta_hash <- rbind(alpha_beta_hash_1)

ggplot(alpha_beta_hash, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# RB
alpha_beta_rb_1 <- read.csv('t_tables/data/alpha_beta_rb_1.csv')
alpha_beta_rb <- rbind(alpha_beta_rb_1)

ggplot(alpha_beta_rb, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Splay
alpha_beta_splay_1 <- read.csv('t_tables/data/alpha_beta_splay_1.csv')
alpha_beta_splay <- rbind(alpha_beta_splay_1)

ggplot(alpha_beta_splay, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Trie
alpha_beta_trie_1 <- read.csv('t_tables/data/alpha_beta_trie_1.csv')
alpha_beta_trie <- rbind(alpha_beta_trie_1)

ggplot(alpha_beta_trie, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()
