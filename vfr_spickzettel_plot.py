
# =====================================================================
# Karle3, 2025-01-02,
# https://github.com/Karle3/vfr-spickzettel
# https://github.com/Karle3/vfr-spickzettel/releases/tag/V2_4
# =====================================================================

"""VFR Spickzettel (EDDS)."""

import numpy as np
import matplotlib.pyplot as plt

VERSION = "2.7" # boxes adjusted
DATE    = "2026-06-04"


VERSION = "2.6" # transponder
DATE    = "2026-06-04"

# VERSION = "2.5"
# DATE    = "2025-01-03"

# https://matplotlib.org/

# https://matplotlib.org/stable/plot_types/basic/scatter_plot.html#sphx-glr-plot-types-basic-scatter-plot-py

# https://matplotlib.org/stable/tutorials/pyplot.html#introduction-to-pyplot


# --- Global Constants:
FEET2METER = 0.3048

FEET_MIN = 3000
FEET_MAX = 8000+500
FEET_STEP = 500

METER_MIN =  500
METER_MAX = 2500
METER_STEP = 250

FEET_ALB_NORD = 4500
FEET_ALB_SUED = 7500

# plot, get figure and axes
fig, ax = plt.subplots()


# https://www.w3schools.com/python/python_while_loops.asp
""" Loop over abszizza (in feet unit) to calulate resulting value in meter units: """
# "ignore non-snake-case naming" :
#  https://pylint.readthedocs.io/en/stable/user_guide/messages/convention/invalid-name.html
FEET = FEET_MIN # pylint: disable=C0103
while FEET <= FEET_MAX:
    METER = FEET * FEET2METER # pylint: disable=C0103
    if FEET not in (FEET_ALB_NORD, FEET_ALB_SUED) :
        # instead feet != FEET_ALB_NORD and feet != FEET_ALB_SUED :
        #                     vv green circle
        #                     ||    vv marker size
        ax.plot(FEET, METER, 'go',  ms = 8)
    # --- Annote value pairs in diagram.
    ax.annotate(f"_{METER:.0f} m", xy=(FEET +80 , METER -5) )
    FEET += FEET_STEP

plt.axis((FEET_MIN,FEET_MAX,  METER_MIN,METER_MAX))

# Add tile and axis labels.
# plt.title('[m] = f([ft])')
plt.title('Sektoren, EDDS, Luftraum D: [m] <==> [ft] ')
plt.xlabel('feet')
plt.ylabel('meter')

# Add ticks to both axis.
plt.xticks(np.arange(FEET_MIN,  FEET_MAX,  FEET_STEP))
plt.yticks(np.arange(METER_MIN, METER_MAX, METER_STEP))
plt.grid(visible=True, which='both') # , linewidth = 1.0, color="y") # #808080")
# plt.minorticks_on(); --- kills ?ticks !!!


# Sektoren
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
# https://www.w3schools.com/python/matplotlib_markers.asp                          magenta -- v
plt.plot(FEET_ALB_SUED, FEET_ALB_SUED * FEET2METER, 'r<', markersize = 15, markeredgecolor = 'm')
   #, label="75kFT_2280m_Alb-Süd/Ost")
plt.plot(FEET_ALB_NORD, FEET_ALB_NORD * FEET2METER, 'b>', markersize = 12, markeredgecolor = 'm')
   #, label="45kFT_1368_Alb-Nord")
# show labels in a legend
# plt.legend()

## Alb-Nord:
# https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html#sphx-glr-gallery-text-labels-and-annotations-text-commands-py
plt.text(5400, 1260, 'Alb-Nord:  \n 4500 ft = 1372 m',
		fontsize=12,
        bbox={'facecolor': 'blue', 'alpha': 0.2, 'pad': 3})
#     style='italic',    bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 0})

## Alb-S/O__
Y_POS = FEET2METER  * FEET_ALB_SUED
# add red arrow
plt.annotate('---', xy=(FEET_ALB_SUED-100, Y_POS), xytext=(6400, Y_POS+10),
            arrowprops={"facecolor": 'red', "shrink": 0.05} )
# arrowprops=dict(facecolor='red', shrink=0.05))
# add box
plt.text(4000+30, 2065, 'Alb-Süd/Ost/West\nSchwarzwald/Hornberg:\n FL75 = 2286 m \n (@1013,25hPa)',
		fontsize=12,
        bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 2})

# Freq:
# ; 130.740(R9)
plt.text(4000+30, 580, '\
- BordBord: 122.540/555 ; 130.430 \n\
- Langen:   128.950 MHz (Einzelfreig.)\n\
- Segelfl:  134.505 MHz (ED-R132) \n\
- ATIS S:   126.125 MHz ',
		fontsize=12, fontweight='bold',  family='monospace', # 'sans-serif'
        bbox={'facecolor': 'lightgreen', 'alpha': 0.8, 'pad': 2})

# Transponder
# https://www.fliegermagazin.de/wissen/transponder-einschalten/
# https://www.fliegermagazin.de/wissen/welche-aircraft-squawk-codes-gibt-es/
# https://einklich.net/flugfunk/funk.pdf
plt.text(3200, 1530, '\
Transponder Squawk:\n\
- 7000: VFR\n\
- 7600: Funkausfall\n\
- 7700: Notfall',
		fontsize=9, fontweight='bold',  family='monospace', # 'sans-serif'
        bbox={'facecolor': 'lightgrey', 'alpha': 0.8, 'pad': 2})

# Version as side bar
VER_STR = f"Karle3: v{VERSION:s}, {DATE:s}, edpj.de, \
 \nhttps://github.com/Karle3/vfr-spickzettel"
plt.text(8500, 600, \
VER_STR,
 rotation=90,
 bbox={ 'facecolor': 'lightblue', 'pad': 5 }
)



# ---
# deploy figure

#
plt.show()
fig.savefig('vfr-spickzettel.png')
fig.savefig('vfr-spickzettel.svg')
fig.savefig('vfr-spickzettel.pdf')
