from typing import Union, Optional, List, Dict, Tuple, Any
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import contextplt as cplt

class CountryList:
    typical1 = [
        "Japan", "United States", 
        "United Kingdom", "France", "Germany", 
        "China", "Brazil", "Nigeria", "Congo"
    ]
    typical1_world = ["World"] + typical1

    europe = [
        "United Kingdom", "Belgium", "Denmark",
        #"Finland", 
        "France", "Germany", 
        #"Estonia", "Greece", "Greenland", "Iceland",
        "Italy", 
        #"Latvia", "Luxembourg", "Malta",
        "Poland", "Portugal", "Spain", "Sweden", 
        "Switzerland", 
    ]

    north_america = [
        "United States", "Canada", "Cuba"
    ]

    south_america = [
        "Brazil", "Argentina", "Colombia",
        "Peru", "Chile", "Ecuador",
    ]



def case_death_vis(df: pd.DataFrame,
                   countries: list,
                   cols: Optional[list] = None,
                   figsize=(9,6),
                   suptitle="",
                  ):
    if cols is None:
        cols = ["new_cases_smoothed", "new_deaths_smoothed",
                "new_cases_smoothed_per_million", "new_deaths_per_million"
               ]
    mosaic = [[1,2],
              [3,4]
             ]
    with cplt.Multiple(mosaic=mosaic, 
                       figsize=figsize,
                       suptitle=suptitle,
                       ) as mul:
        for i, col in enumerate(cols):
            with mul.Single(index=i+1,xrotation=90, title=col) as p:
                for cnt in countries:
                    dfM = df[ df.location == cnt]
                    p.ax.plot(dfM.date, dfM[col], label=cnt)
                #if i + 1 == 2:
                p.ax.legend(frameon=False) 
                            #bbox_to_anchor=(1,1), fontsize=6)

