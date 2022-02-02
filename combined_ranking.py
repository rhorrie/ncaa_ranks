#Finds the average ranking for each team

import pandas as pd

def find_combined_rankings(ncaa):
	ncaa['Combined'] = ncaa.mean(axis=1).round(2)
	
	return ncaa