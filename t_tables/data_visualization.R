# Erich

library(dplyr)
library(ggplot2)


## Random
# AVL
random_avl_1 <- read.csv('t_tables/data/random_avl_1.csv')
random_avl_2 <- read.csv('t_tables/data/random_avl_2.csv')
random_avl_3 <- read.csv('t_tables/data/random_avl_3.csv')
random_avl_4 <- read.csv('t_tables/data/random_avl_4.csv')
random_avl_5 <- read.csv('t_tables/data/random_avl_5.csv')
random_avl <- rbind(random_avl_1, random_avl_2, random_avl_3, random_avl_4, random_avl_5)
ggplot(random_avl, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Hash
random_hash_1 <- read.csv('t_tables/data/random_hash_1.csv')
random_hash_2 <- read.csv('t_tables/data/random_hash_2.csv')
random_hash_3 <- read.csv('t_tables/data/random_hash_3.csv')
random_hash_4 <- read.csv('t_tables/data/random_hash_4.csv')
random_hash_5 <- read.csv('t_tables/data/random_hash_5.csv')
random_hash <- rbind(random_hash_1, random_hash_2, random_hash_3, random_hash_4, random_hash_5)
ggplot(random_hash, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# RB
random_rb_1 <- read.csv('t_tables/data/random_rb_1.csv')
random_rb_2 <- read.csv('t_tables/data/random_rb_2.csv')
random_rb_3 <- read.csv('t_tables/data/random_rb_3.csv')
random_rb_4 <- read.csv('t_tables/data/random_rb_4.csv')
random_rb_5 <- read.csv('t_tables/data/random_rb_5.csv')
random_rb <- rbind(random_rb_1, random_rb_2, random_rb_3, random_rb_4, random_rb_5)
ggplot(random_rb, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Splay
random_splay_1 <- read.csv('t_tables/data/random_splay_1.csv')
random_splay_2 <- read.csv('t_tables/data/random_splay_2.csv')
random_splay_3 <- read.csv('t_tables/data/random_splay_3.csv')
random_splay_4 <- read.csv('t_tables/data/random_splay_4.csv')
random_splay_5 <- read.csv('t_tables/data/random_splay_5.csv')
random_splay <- rbind(random_splay_1, random_splay_2, random_splay_3, random_splay_4, random_splay_5)
ggplot(random_splay, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Trie
random_trie_1 <- read.csv('t_tables/data/random_trie_1.csv')
random_trie_2 <- read.csv('t_tables/data/random_trie_2.csv')
random_trie_3 <- read.csv('t_tables/data/random_trie_3.csv')
random_trie_4 <- read.csv('t_tables/data/random_trie_4.csv')
random_trie_5 <- read.csv('t_tables/data/random_trie_5.csv')
random_trie <- rbind(random_trie_1, random_trie_2, random_trie_3, random_trie_4, random_trie_5)
ggplot(random_trie, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# all
random <- rbind(random_avl, random_hash, random_rb, random_splay, random_trie)
ggplot(random, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()


## Minimax
# AVL
minimax_avl_1 <- read.csv('t_tables/data/minimax_avl_1.csv')
minimax_avl_2 <- read.csv('t_tables/data/minimax_avl_2.csv')
minimax_avl_3 <- read.csv('t_tables/data/minimax_avl_3.csv')
minimax_avl_4 <- read.csv('t_tables/data/minimax_avl_4.csv')
minimax_avl_5 <- read.csv('t_tables/data/minimax_avl_5.csv')
minimax_avl <- rbind(minimax_avl_1, minimax_avl_2, minimax_avl_3, minimax_avl_4, minimax_avl_5)
ggplot(minimax_avl, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Hash
minimax_hash_1 <- read.csv('t_tables/data/minimax_hash_1.csv')
minimax_hash_2 <- read.csv('t_tables/data/minimax_hash_2.csv')
minimax_hash_3 <- read.csv('t_tables/data/minimax_hash_3.csv')
minimax_hash_4 <- read.csv('t_tables/data/minimax_hash_4.csv')
minimax_hash_5 <- read.csv('t_tables/data/minimax_hash_5.csv')
minimax_hash <- rbind(minimax_hash_1, minimax_hash_2, minimax_hash_3, minimax_hash_4, minimax_hash_5)
ggplot(minimax_hash, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# RB
minimax_rb_1 <- read.csv('t_tables/data/minimax_rb_1.csv')
minimax_rb_2 <- read.csv('t_tables/data/minimax_rb_2.csv')
minimax_rb_3 <- read.csv('t_tables/data/minimax_rb_3.csv')
minimax_rb_4 <- read.csv('t_tables/data/minimax_rb_4.csv')
minimax_rb_5 <- read.csv('t_tables/data/minimax_rb_5.csv')
minimax_rb <- rbind(minimax_rb_1, minimax_rb_2, minimax_rb_3, minimax_rb_4, minimax_rb_5)
ggplot(minimax_rb, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Splay
minimax_splay_1 <- read.csv('t_tables/data/minimax_splay_1.csv')
minimax_splay_2 <- read.csv('t_tables/data/minimax_splay_2.csv')
minimax_splay_3 <- read.csv('t_tables/data/minimax_splay_3.csv')
minimax_splay_4 <- read.csv('t_tables/data/minimax_splay_4.csv')
minimax_splay_5 <- read.csv('t_tables/data/minimax_splay_5.csv')
minimax_splay <- rbind(minimax_splay_1, minimax_splay_2, minimax_splay_3, minimax_splay_4, minimax_splay_5)
ggplot(minimax_splay, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Trie
minimax_trie_1 <- read.csv('t_tables/data/minimax_trie_1.csv')
minimax_trie_2 <- read.csv('t_tables/data/minimax_trie_2.csv')
minimax_trie_3 <- read.csv('t_tables/data/minimax_trie_3.csv')
minimax_trie_4 <- read.csv('t_tables/data/minimax_trie_4.csv')
minimax_trie_5 <- read.csv('t_tables/data/minimax_trie_5.csv')
minimax_trie <- rbind(minimax_trie_1, minimax_trie_2, minimax_trie_3, minimax_trie_4, minimax_trie_5)
ggplot(minimax_trie, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# all
minimax <- rbind(minimax_avl, minimax_hash, minimax_rb, minimax_splay, minimax_trie)
ggplot(minimax, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()


## AlphaBeta
# AVL
alpha_beta_avl_1 <- read.csv('t_tables/data/alpha_beta_avl_1.csv')
alpha_beta_avl_2 <- read.csv('t_tables/data/alpha_beta_avl_2.csv')
alpha_beta_avl_3 <- read.csv('t_tables/data/alpha_beta_avl_3.csv')
alpha_beta_avl_4 <- read.csv('t_tables/data/alpha_beta_avl_4.csv')
alpha_beta_avl_5 <- read.csv('t_tables/data/alpha_beta_avl_5.csv')
alpha_beta_avl <- rbind(alpha_beta_avl_1, alpha_beta_avl_2, alpha_beta_avl_3, alpha_beta_avl_4, alpha_beta_avl_5)
ggplot(alpha_beta_avl, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Hash
alpha_beta_hash_1 <- read.csv('t_tables/data/alpha_beta_hash_1.csv')
alpha_beta_hash_2 <- read.csv('t_tables/data/alpha_beta_hash_2.csv')
alpha_beta_hash_3 <- read.csv('t_tables/data/alpha_beta_hash_3.csv')
alpha_beta_hash_4 <- read.csv('t_tables/data/alpha_beta_hash_4.csv')
alpha_beta_hash_5 <- read.csv('t_tables/data/alpha_beta_hash_5.csv')
alpha_beta_hash <- rbind(alpha_beta_hash_1, alpha_beta_hash_2, alpha_beta_hash_3, alpha_beta_hash_4, alpha_beta_hash_5)
ggplot(alpha_beta_hash, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# RB
alpha_beta_rb_1 <- read.csv('t_tables/data/alpha_beta_rb_1.csv')
alpha_beta_rb_2 <- read.csv('t_tables/data/alpha_beta_rb_2.csv')
alpha_beta_rb_3 <- read.csv('t_tables/data/alpha_beta_rb_3.csv')
alpha_beta_rb_4 <- read.csv('t_tables/data/alpha_beta_rb_4.csv')
alpha_beta_rb_5 <- read.csv('t_tables/data/alpha_beta_rb_5.csv')
alpha_beta_rb <- rbind(alpha_beta_rb_1, alpha_beta_rb_2, alpha_beta_rb_3, alpha_beta_rb_4, alpha_beta_rb_5)
ggplot(alpha_beta_rb, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Splay
alpha_beta_splay_1 <- read.csv('t_tables/data/alpha_beta_splay_1.csv')
alpha_beta_splay_2 <- read.csv('t_tables/data/alpha_beta_splay_2.csv')
alpha_beta_splay_3 <- read.csv('t_tables/data/alpha_beta_splay_3.csv')
alpha_beta_splay_4 <- read.csv('t_tables/data/alpha_beta_splay_4.csv')
alpha_beta_splay_5 <- read.csv('t_tables/data/alpha_beta_splay_5.csv')
alpha_beta_splay <- rbind(alpha_beta_splay_1, alpha_beta_splay_2, alpha_beta_splay_3, alpha_beta_splay_4, alpha_beta_splay_5)
ggplot(alpha_beta_splay, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# Trie
alpha_beta_trie_1 <- read.csv('t_tables/data/alpha_beta_trie_1.csv')
alpha_beta_trie_2 <- read.csv('t_tables/data/alpha_beta_trie_2.csv')
alpha_beta_trie_3 <- read.csv('t_tables/data/alpha_beta_trie_3.csv')
alpha_beta_trie_4 <- read.csv('t_tables/data/alpha_beta_trie_4.csv')
alpha_beta_trie_5 <- read.csv('t_tables/data/alpha_beta_trie_5.csv')
alpha_beta_trie <- rbind(alpha_beta_trie_1, alpha_beta_trie_2, alpha_beta_trie_3, alpha_beta_trie_4, alpha_beta_trie_5)
ggplot(alpha_beta_trie, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()

# all
alpha_beta <- rbind(alpha_beta_avl, alpha_beta_hash, alpha_beta_rb, alpha_beta_splay, alpha_beta_trie)
ggplot(alpha_beta, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()


## Everything
everything <- rbind(random, minimax, alpha_beta)
ggplot(everything, aes(x=game_number, y=agent_decision_time, color=agent_type)) + geom_point() + geom_smooth()
