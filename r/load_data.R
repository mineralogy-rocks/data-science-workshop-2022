library(tidyverse)
library(ggplot2)


plots_path = 'plots'
setwd('~/git-repositories/data-science-workshop-2022/r')


initial_data <- readxl::read_excel(path='../data/mafic_dykes.xlsx')

initial_data %>% 
  group_by(`Rock Type`) %>%
  summarise(min_SiO2=min(SiO2), max_SiO2=max(SiO2)) %>%
  max(max_SiO2)
