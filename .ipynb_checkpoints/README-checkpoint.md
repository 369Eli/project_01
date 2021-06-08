# project_01

Summer Olympic Real Estate Investment Portfolio
Identify undervalued rental properties that would have a high resale value after the 2028 summer olympics 

Summer Olympics Locations : https://la.curbed.com/maps/olympics-map-los-angeles-2028-games-locations

Property Assesor Home Values:  https://data.lacounty.gov/Parcel-/Assessor-Parcel-Data-2020/42ne-gwcj/data

Question: How do we find the data requested by the client?
## How do we do that?: Goals, tasks, methods of study
    A: Client wants to find real estate investment opportunities near sporting venues hosting the 2028 Olymipics. Long Beach, Inglewood, and Calabasas are near by popular cities. We analyze zip codes in the surrounding area to find markets with the highest number of homes for sale to artifically create a buyers market or the market with the greatest inventory to choose from. The three cities were chosen because they represent neighborhoods with different degrees of developement. Inglewood is developing, Long beach is pretty settled, and Calabasas is finalized.    
       
       Opening ceremonies are planned to be held at the rising Los Angeles Rams stadium in Inglewood, with a simultaneous event at the Los Angeles Memorial Coliseum, tickets for the kickoff of the games are expected to come with an average price tag of $1,783. Closing ceremonies at the Coliseum will be somewhat less, with an average ticket price of $1,226. Therefore target properties criteria:
       2 mile radius from venue
       Inglewood city = 90304 
       Long Beach city = 90712 
       3 bedrooms 
      2 bathroom
      
Question 1:  Import Libraries 
    We imported pandas and numpy.
   
Questions 2: Filter Raw Data Frame into a 2 Dimensional array create a csv file
    Line 56
        
Question 3:  Filter csv data frame into logical answers defining real estate qualitites like Property type, # bath, # of Bed, price per sq ft. please see line 42-57.

Questions 4: How many available properties match our core criteria filter. Line 39.

Question 5: Identify values to possibly create a Series to manipulate or delete. Line 40.

Question 6: Identify City with the largest volume of homes for sale by type. Line 44.

Create Visuals - Line 47 - 23.

Question 7: Excersise in conditionals. Could we create a replicatable formula with set property qualities to apply in different markets?





