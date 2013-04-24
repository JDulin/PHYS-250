
w = 200E-6
D = 1
wave = 500E-9
L = 10E-2

def part_two():
   N = w*L/(wave*D) 
   alpha = 50,000*math.pi
   z = linspace(0,200,40)
   A = abs(math.sin(alpha*z))
   I = fft.fft(A)
   I = np.square(abs(I))
   I = fft.fftshift(I)
   # plt.plot(I)
   # plt.show()

   # Here we construct an array with zero padding to mimic a longer, opaque, diffraction grating.
   z_padded = np.concatenate((z, zero))
   A2 = abs(math.sin(alpha*z_padded))
   I2 = fft.fft(A2)
   I2 = np.square(abs(I2))
   I2 = fft.fftshift(I2)
   # We can normalize the vector by dividing it by the maximum value.



   # Part 3
   x = linspace(-L/2, L/2, 40)
   plt.imshow([I2,], extent=(x[0], x[-1], 0, 1), cmap=cm.gray) # Extent defines the min, max of the x,y axes
   plt.yticks([])
   plt.xlabel("Screen length position (in cm)")
   plt.ylabel("Screen width")
   plt.title("Light pattern from diffraction grating")

   # Repeat for logarithm scale for better viewing.
   I

if __name__ == "__main__":
    import numpy as np
    import scipy.fftpack as fft
    import matplotlib.pyplot as plt
    import math
    lab

