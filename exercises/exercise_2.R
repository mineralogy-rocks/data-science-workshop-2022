library(readr)
library(tidyr)
library(knitr)
library(dplyr)

initial_data <-readxl::read_xls('./data/raw_data/Chrysoberyl analysis database.xls')

initial_data_t <- t(initial_data)
colnames(initial_data_t) <- initial_data_t[1,]
initial_data_t <- as_tibble(cbind(Sample = names(initial_data)[-1], initial_data_t[-1,]))

initial_data_t <- 
  initial_data_t %>%
  mutate_at(vars(-Sample, -Origin, -Reference), as.numeric) %>%
  mutate_at(vars(-Sample, -Origin, -Reference), .funs=function(x){ replace(x, x<=0, NA) })

# Write your code below this line.

