library(tidyverse)
library(ggplot2)


plots_path = 'plots'
setwd('~/git-repositories/data-science-workshop-2022/R')


initial_data <- readxl::read_excel(path='../data/Chrysoberyl analysis database.xls', 
                                   sheet='CHRYZO', 
                                   skip=1)
