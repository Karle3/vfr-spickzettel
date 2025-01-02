
# =====================================================================
# Karle3, 2025-01-02, v2.2
# https://github.com/Karle3/vfr-spickzettel
# =====================================================================

"""VFR Spickzettel (EDDS)."""


# https://matplotlib.org/

# https://matplotlib.org/stable/plot_types/basic/scatter_plot.html#sphx-glr-plot-types-basic-scatter-plot-py

# https://matplotlib.org/stable/tutorials/pyplot.html#introduction-to-pyplot

import numpy as np
import matplotlib.pyplot as plt

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
feet = FEET_MIN
while feet <= FEET_MAX:
    meter = feet * FEET2METER
    if feet not in (FEET_ALB_NORD, FEET_ALB_SUED) :
        # instead feet != FEET_ALB_NORD and feet != FEET_ALB_SUED :
        ax.plot(feet, meter, 'go')
    # --- Annote value pairs in diagram.
    ax.annotate(f"_{meter:.0f} m", xy=(feet +50 , meter -10) )
    feet += FEET_STEP

plt.axis((FEET_MIN,FEET_MAX,  METER_MIN,METER_MAX))


# plt.title('[m] = f([ft])')
plt.title('Sektoren, EDDS, Luftraum D: [m] <==> [ft] ')
plt.xlabel('feet')
plt.ylabel('meter')

plt.xticks(np.arange(FEET_MIN, FEET_MAX, 1000))


plt.xticks(np.arange(FEET_MIN,  FEET_MAX,  FEET_STEP))
plt.yticks(np.arange(METER_MIN, METER_MAX, METER_STEP))
plt.grid(visible=True, which='both')
# plt.minorticks_on(); --- kills ?ticks !!!


# Sektoren
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
plt.plot(FEET_ALB_SUED, FEET_ALB_SUED * FEET2METER, 'r^', label="75kFT_2280m_Alb-Süd/Ost")
plt.plot(FEET_ALB_NORD, FEET_ALB_NORD * FEET2METER, 'b^', label="45kFT_1368_Alb-Nord")
# show labels in a legend
# plt.legend()


# Alb-S/O__
Y_POS = FEET2METER  * FEET_ALB_SUED
plt.annotate('_', xy=(FEET_ALB_SUED, Y_POS), xytext=(6500, Y_POS),
            arrowprops={"facecolor": 'red', "shrink": 0.05} )
# arrowprops=dict(facecolor='red', shrink=0.05))

# https://matplotlib.org/stable/gallery/text_labels_and_annotations/text_commands.html#sphx-glr-gallery-text-labels-and-annotations-text-commands-py
plt.text(5400, 1250, 'Alb-Nord:  \n 4500 ft = 1372 m',
		fontsize=12,
        bbox={'facecolor': 'blue', 'alpha': 0.2, 'pad': 3})
#     style='italic',    bbox={'facecolor': 'blue', 'alpha': 0.5, 'pad': 0})

plt.text(3500, 2000, 'Alb-Süd/Ost/West\nSchwarzwald/Hornberg:\n FL75 = 2286 m \n (@1013,25hPa)',
		fontsize=15,
        bbox={'facecolor': 'red', 'alpha': 0.2, 'pad': 3})

# ; 130.740(R9)
plt.text(4000, 600, '\
- BordBord: 122.540/555 ; 130.430 \n\
- Langen:   128.950 MHz (Einzelfreig.) \n\
- Segelfl:  134.505 MHz (ED-R132) \n\
- ATIS S:   126.125 MHz ',
		fontsize=12, fontweight='bold',  family='monospace', # 'sans-serif'
        bbox={'facecolor': 'lightgreen', 'alpha': 0.8, 'pad': 2})


plt.text(8500, 600, \
	'Karle3: v2.2, 2025-01, www.edpj.de, \
	\nhttps://github.com/Karle3/vfr-spickzettel',
	rotation=90,
	bbox={ 'pad': 5 }
	)



# ---
# deploy figure

#
plt.show()
fig.savefig('vfr-spickzettel.png')
fig.savefig('vfr-spickzettel.svg')
fig.savefig('vfr-spickzettel.pdf')
