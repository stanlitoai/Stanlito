#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as pt
x = np.arrange(1,12,0.001)
y = np.x
pt.plot(x,y)
pt.xlabel(independent variable)
pt.ylabel(dependent variable)
pt.title(sample graph)
pt.grid()
pt.show


# In[5]:


import numpy as np
import matplotlib.pyplot as pt
x=np.arrange(1,12,0.001)
y=np.sin(x)
pt.plot(x,y)
pt.xlabel(independent variable)
pt.ylabel(dependent variable)
pt.title(sample graph)
pt.grid()
pt.show


# In[1]:


import matplotlib.pyplot as plot
import math
import numpy as npy
length=0.05
signalGen=48000.0
F1=1000.0

y=[math.sin(2.0* math.pi *F1 * i / signalGen)for i in range(int(length *signalGen))]
x=[1000.0 * i / signalGen for i in range(len(y))]
spectrum=npy.fft.rfft(y)
spectrumMod=20.0 * npy.log10(npy.abs(spectrum))
spectrumPha=180.0 / npy * pi * npy.angle(spectrum)
frequencyBins=[i / len(spectrum) * signalGen / 2.0 for i in range (len(spectrum))]

#waveform plot

plot.plot(x, y, label='sine wave')
plot.plot([0, 2 * (1.0 / F1) * 1000.0])
plot.xlabel('Time[ms]')
plot.ylabel(Amplitude[m])
plot.grid(1)
plot.legend()
plot.show()


# In[ ]:


import matplotlib.pyplot as plot
import math
import numpy as npy
length=0.05
signalGen=48000.0
F1=1000.0

y=[math.sin(2.0* math.pi *F1 * i / signalGen)for i in range(int(length *signalGen))]
x=[1000.0 * i / signalGen for i in range(len(y))]
spectrum=npy.fft.rfft(y)
spectrumMod=20.0 * npy.log10(npy.abs(spectrum))
spectrumPha=180.0 / npy * pi * npy.angle(spectrum)
frequencyBins=[i / len(spectrum) * signalGen / 2.0 for i in range (len(spectrum))]

#waveform plot

plot.plot(x, y, label='sine wave')
plot.plot([0, 2 * (1.0 / F1) * 1000.0])
plot.xlabel('Time[ms]')
plot.ylabel('Amplitude[m]')
plot.grid(1)
plot.legend()
plot.show()


# In[ ]:





# In[ ]:




