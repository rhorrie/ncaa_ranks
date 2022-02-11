from flask import Flask, request, render_template, session, redirect
import requests
import pandas as pd
from big10_stats_scrape import *

	
def get_big10_stats():
	
	big10 = pd.DataFrame(columns=['Team', 'G', 'MP', 'FG', 'FGA', 'FG%', '2P', '2PA', '2P%', '3P', '3PA', '3P%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS'])

	teams = ['purdue', 'wisconsin', 'illinois', 'rutgers', 'michigan', 'indiana', 'iowa', 'northwestern', 'maryland', 'minnesota', 'nebraska', 'michigan-state', 'ohio-state', 'penn-state']

	for team in teams:
		big10 = big10_stats_scrape(team, big10)

	return big10