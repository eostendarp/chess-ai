# Erich Ostendarp

# imports
library(dplyr)
library(ggplot2)


A1vA2 <- read.csv('data/A1vA2.csv', sep='\t')  # Depth
A1vA3 <- read.csv('data/A1vA3.csv', sep='\t')  # Depth
A2vA2 <- read.csv('data/A2vA2.csv', sep='\t')  # Baseline

A2vA2T_1 <- read.csv('data/A2vA2T_1.csv', sep='\t')  # Transposition Tables
A2vA2T_2 <- read.csv('data/A2vA2T_2.csv', sep='\t')  # Transposition Tables
A2vA2T_3 <- read.csv('data/A2vA2T_3.csv', sep='\t')  # Transposition Tables
A2vA2T_4 <- read.csv('data/A2vA2T_4.csv', sep='\t')  # Transposition Tables
A2vA2T_5 <- read.csv('data/A2vA2T_5.csv', sep='\t')  # Transposition Tables
A2vA2T_6 <- read.csv('data/A2vA2T_6.csv', sep='\t')  # Transposition Tables
A2vA2T_7 <- read.csv('data/A2vA2T_7.csv', sep='\t')  # Transposition Tables
A2vA2T <- rbind(A2vA2T_1, A2vA2T_2, A2vA2T_3, A2vA2T_4, A2vA2T_5, A2vA2T_6, A2vA2T_7)  # Transposition Tables

A2vA3 <- read.csv('data/A2vA3.csv', sep='\t')  # Depth
C2vC2 <- read.csv('data/C2vC2.csv', sep='\t')  # Baseline

