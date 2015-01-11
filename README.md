# usda_plants
Interface to the USDA PLANTS database.

scrape_nox.py -- scrapes the composite noxious weeds list at : http://plants.usda.gov/java/noxComposite
 This will generate a csv file as output.  Ideally it should be downloadable via a direct query, as the page has
 an advanced search download feature.  However the logic is limited and doesn't expose the url for query.  This is a 
 quick beautifulsoup script to parse it out from their internal composite query.
