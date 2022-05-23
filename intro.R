

initial_data <- read.table('./data/raw_data/mafic_dykes.csv', header=TRUE, sep=',')

df1 <- data.frame(specimen = 1:3, location = c('Peterman', 'Barchan', 'Galindez'),
                  rock_type = 'basalt')
df2 <- data.frame(specimen = 1:3, location = 'Forge Isl',
                   rock_type = 'andesite')

rbind(df1, df2)

rock_types = unique(initial_data$Rock.Type)

print('safsa')
print('something else\nas')



?print
