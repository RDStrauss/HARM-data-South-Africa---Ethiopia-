
from __future__ import division
import matplotlib, datetime
import matplotlib.pyplot as plt
import numpy as np
# Set-up standard style
from matplotlib import rcParams
plt.rcParams['agg.path.chunksize'] = 10000
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = 'Computer Modern Roman'
plt.rcParams['font.sans-serif'] = 'Computer Modern Roman'
plt.rcParams['font.monospace'] = 'Computer Modern Roman'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams["axes.labelweight"] = "bold"#"medium"
plt.rcParams['axes.labelsize'] =23
plt.rcParams["axes.linewidth"] = 1.5
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['axes.edgecolor'] = 'black'  
plt.rcParams['axes.facecolor'] = 'white'  
#plt.rcParams['axes.facecolor'] = 'black'
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['font.size'] =23
plt.rcParams['legend.fontsize'] =23
plt.rcParams['legend.fancybox'] = True
plt.rcParams["lines.linewidth"] = 1.5
plt.rcParams['lines.antialiased'] = True
matplotlib.rc('text',usetex=True)
plt.rcParams['text.color'] = 'black'
plt.rcParams['text.hinting'] = 'auto'
rcParams['mathtext.default'] = 'regular'
plt.rcParams['mathtext.fontset'] = 'cm'

plt.rcParams['mathtext.default'] = 'regular'
plt.rcParams['mathtext.default'] = 'rm' # sf
rcParams['pdf.compression'] = 0
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.color'] = 'gray'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = '1.2'
plt.rcParams['grid.alpha'] = 0.2
# visible ticks
plt.rcParams['xtick.labelsize'] =20
plt.rcParams['ytick.labelsize'] =20
plt.rcParams["xtick.major.width"] = 1.5
plt.rcParams["ytick.major.width"] = 1.5
plt.rcParams["xtick.minor.width"] = 1.5
plt.rcParams["ytick.minor.width"] = 1.5
rcParams["xtick.minor.visible"] = True
rcParams["ytick.minor.visible"] = True
rcParams["xtick.top"] = False
rcParams["ytick.right"] = True
rcParams["xtick.major.size"] = 12
rcParams["xtick.major.pad"] = 10
rcParams["ytick.major.size"] = 12
rcParams["ytick.major.pad"] = 10
rcParams["xtick.minor.size"] = 6
rcParams["ytick.minor.size"] = 6
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'
 

# Save figures as PDFs
from matplotlib.backends.backend_pdf import PdfPages
pdfsave_Spectra = PdfPages( "Medium_Haul_Flight.pdf")

 
#=========================================================##=========================================================#
#=========================================================##=========================================================#
#=========================================================##=========================================================#


Fig_=plt.figure(figsize=(14,8))
ax = Fig_.add_subplot(111)  
Colors = ['red','blue']

import glob
f = sorted(glob.glob('*HARMCounter.txt')) # absolute path to search all text files inside a specific folder
for Fl,CLRz in zip(f,Colors):
    Flight_date = str(Fl.split('/')[-1].split('_')[0])
    Flight_route = str(Fl.split('/')[-1].split('_')[1])
    departure_Airp = str(Flight_route.split('-')[0])
    destination_Airp = str(Flight_route.split('-')[-1])
    
    with open(Fl,"r") as fl:
        lineZ=fl.readlines()[3:-2]
        fl.close()
    Time,CountR, = [],[] 
    for i in lineZ:
        CountR.append( float(i.split()[2]) )
        Time.append(i.split()[0]+' '+i.split()[1])
  
    # Calculated Elapsed time.....
    startDate = datetime.datetime.strptime(Time[0], '%Y-%m-%d %H:%M:%S' ) 
    startDateEvol = [datetime.datetime.strptime(d,'%Y-%m-%d %H:%M:%S') for d in  Time]
    Time_elasped = [ float((TimeP -startDate).total_seconds()/60.)  for TimeP in  startDateEvol ] # Elapsed time in hours /3600...

    # Plotting two data sets with the error bars
    kwargs = dict(ecolor=CLRz, color='k', capsize=2.5,elinewidth=0.8, linestyle='none', markersize=12)
    ax.errorbar(Time_elasped, CountR, yerr=np.sqrt(np.array(CountR)), fmt='.', mfc=CLRz, **kwargs,label = str(departure_Airp) + r'$\rightarrow$' + str(destination_Airp)+' ['+Flight_date+']')

    #plt.plot(Time_elasped, CountR ,color=CLRz,label = str(departure_Airp) + r'$\rightarrow$' + str(destination_Airp)+' ['+Flight_date+']')

ax.set_ylabel(r"Counts per Min.")
ax.set_xlabel(r"Elapsed Time [Min.]")
ax.legend( shadow =False,frameon =False,ncol =1,loc =2, labelspacing =0.1,handlelength =1,handletextpad =0.5,columnspacing =0.7,markerscale =1.5,fontsize=20)

pdfsave_Spectra.savefig(Fig_,dpi =250)
pdfsave_Spectra.close()


plt.show()



   
