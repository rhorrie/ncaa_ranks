#Main function that also displays the homepage of ncaa-ranks. Plan to expand on this in future with ability to click on indiviudal teams (hopefully)


from flask import Flask, request, render_template, session, redirect
import requests
import pandas as pd
from kenpom_scrape import *
from torvik_scrape import *
from net_scrape import *
from combined_ranking import *
from ap_and_coaches_scrape import *

#Creating ncaa dataframe
ncaa = pd.DataFrame()

#Calling each scraping function to find different rankings
ncaa = kenpom_scrape(ncaa)
ncaa = torvik_scrape(ncaa)
ncaa = net_scrape(ncaa)
ncaa = ap_and_coaches_scrape(ncaa)

#Calling combine function to find the overall ranking of each team
ncaa = find_combined_rankings(ncaa)

#Creating webpage
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

	return render_template('test_template.html', column_names=ncaa.columns.values, row_data=list(ncaa.values.tolist()), zip=zip)

if __name__ == '__main__':
	app.run(debug=True)


