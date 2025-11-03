import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

def double_slit_diffraction_intensity (slit_width, wavelength, screen_distance, distance_between_slits,  X) :
  """
    Takes in slit_width, wavelength, screen distance, distance between the two strings and a numpy array X(an array of distances from the center).
    Outputs an array of normalized intensities corresponding to X.
  """
  return (((np.sin((np.pi*slit_width*X)/(wavelength*screen_distance)))/((np.pi*slit_width*X)/(wavelength*screen_distance)))**2)*((np.cos((np.pi*distance_between_slits*X)/(wavelength*screen_distance)))**2)


X = np.arange(-0.005,0.005,0.00001)
slit_width = 100*(10**-6)
wavelength = 500*(10**-9)
screen_distance = 50*(10**-2)
distance_between_slits= 1*10**-3

Y = double_slit_diffraction_intensity(slit_width, wavelength, screen_distance, distance_between_slits, X)
plot, = plt.plot(X,Y)
plt.xlabel("Distance from center")
plt.ylabel("Intensity")

axis=(plt.axes([0.75, 0.75, 0.14, 0.05]))
axis2 = (plt.axes([0.75,0.65, 0.14, 0.05]))
axis3 = (plt.axes([0.75,0.55, 0.14, 0.05]))
axis4 = (plt.axes([0.75,0.45, 0.14, 0.05]))

wavelength_slider = Slider(axis,'Wavelength(nm)',100, 1000,valinit=wavelength*10**9)
slit_width_slider = Slider(axis2, "Slit Width(micrometers)", 10, 1000, valinit=slit_width*10**6)
screen_distance_slider = Slider(axis3, "Screen Distance(cm)", 10, 100, valinit= screen_distance*10**2)
distance_between_slits_slider = Slider(axis4, "Distance b/w slits(mm)", 0.1, 10, valinit=distance_between_slits*10**3) 

"""
  Dynamic callback function to update slider values and plot again
"""
def update(val) :
  wavelength = wavelength_slider.val*(10**-9)
  slit_width = slit_width_slider.val*(10**-6)
  screen_distance = screen_distance_slider.val*(10**-2)
  distance_between_slits = distance_between_slits_slider.val*(10**-3)
  Y = double_slit_diffraction_intensity(slit_width, wavelength, screen_distance, distance_between_slits, X)
  plot.set_ydata(Y)

wavelength_slider.on_changed(update)
slit_width_slider.on_changed(update)
screen_distance_slider.on_changed(update)
distance_between_slits_slider.on_changed(update)

plt.show()
