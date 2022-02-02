from flask import Flask, request, render_template, session, redirect
import requests
import pandas as pd
from kenpom_scrape import *
from torvik_scrape import *
from net_scrape import *
from combined_ranking import *
from ap_and_coaches_scrape import *

ncaa = pd.DataFrame()

ncaa = kenpom_scrape(ncaa)
ncaa = torvik_scrape(ncaa)
ncaa = net_scrape(ncaa)
ncaa = ap_and_coaches_scrape(ncaa)
ncaa = find_combined_rankings(ncaa)

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

	return render_template('test_template.html', column_names=ncaa.columns.values, row_data=list(ncaa.values.tolist()), zip=zip)

if __name__ == '__main__':
	app.run(debug=True)




#NET ranks dont use same team names, so unable to merge dataframes. Need to find a way around this