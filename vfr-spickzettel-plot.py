

# Karle3, 2025-01-02, v2.1
# https://github.com/Karle3/vfr-spickzettel



# https://matplotlib.org/

# https://matplotlib.org/stable/plot_types/basic/scatter_plot.html#sphx-glr-plot-types-basic-scatter-plot-py

# https://matplotlib.org/stable/tutorials/pyplot.html#introduction-to-pyplot

import numpy as np
import matplotlib.pyplot as plt


FEET2METER = 0.3048;

feet_min = 3000
feet_max = 8000+500;
feet_step = 500;

meter_min =  500;
meter_max = 2500;
meter_step = 250;

FEET_ALB_NORD = 4500;
FEET_ALB_SUED = 7500;

# plot, get figure and axes
fig, ax = plt.subplots()


# https://www.w3schools.com/python/python_while_loops.asp
feet = feet_min;
while feet <= feet_max:
	meter = feet * FEET2METER;
	if feet != FEET_ALB_NORD and feet != FEET_ALB_SUED :
		ax.plot(feet, meter, 'go')
	ax.annotate(f"_{meter:.0f} m", xy=(feet +50 , meter -10) )
	feet += feet_step;

plt.axis((feet_min,feet_max,  meter_min,meter_max))


# plt.title('[m] = f([ft])')
plt.title('Sektoren, EDDS, Luftraum D: [m] <==> [ft] ')
plt.xlabel('feet');
plt.ylabel('meter');

plt.xticks(np.arange(feet_min, feet_max, 1000))


plt.xticks(np.arange(feet_min,  feet_max,  feet_step))
plt.yticks(np.arange(meter_min, meter_max, meter_step))
plt.grid(visible=True, which='both')
# plt.minorticks_on(); --- kills ?ticks !!!


# Sektoren
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py
plt.plot(FEET_ALB_SUED, FEET_ALB_SUED * FEET2METER, 'r^', label="75kFT_2280m_Alb-Süd/Ost")
plt.plot(FEET_ALB_NORD, FEET_ALB_NORD * FEET2METER, 'b^', label="45kFT_1368_Alb-Nord")
# show labels in a legend
# plt.legend()


# Alb-S/O__
plt.annotate('_', xy=(FEET_ALB_SUED, 2280), xytext=(6500, 2280),
            arrowprops=dict(facecolor='red', shrink=0.05))

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


plt.text(8500, 600, 'Karle3: v2.1, 2025-01, www.edpj.de',
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
