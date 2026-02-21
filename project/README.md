Classical Composer Suggestor
Video Demo:  <[URL](https://youtu.be/K7fx68c6nM8)>
Description:
Scrapes wikipedia page of classical composers using wikipedia library and parses with Beautiful Soup
Constructs a table using pandas of name, birth_year, death_year, and period of each composer
Fills name, birth_year, and death_year columns of this table using regex groupings
Categorizes birth_year and death_year of each row as Baroque, Classical, or Romantic to fill period column of dataframe
Prompts user for a period they would like a composer from (Baroque, Classical, or Romantic)
Based on prompt, provides 3 random composers from that period by selecting 3 values from column name that have the user's selected period in their period column
Re-prompts if provided an invalid user response
