import matplotlib.pyplot as plt

t = 0.0
dt = 1.0/200.0
v = -55.0
v_trash = 30.0  #mV
u = 0.0
a = 0.1
b = 0.25
c = -65.0
d = 2.0
vs = []
spike_times = []
while t < 70.0:
    vs.append(v)
    dv = (0.04 * v ** 2)+(5.0*v)+140.0-u
    du = a*((b*v)-u)
    if t>20.0 and t<45.0:
        dv+=50.0
    v += dv*dt
    u += du*dt
    if v >= v_trash:
        spike_times.append(t)
        v = c
        u = u+d
    t += dt

fig = plt.figure(figsize=(15,10), dpi=180)
plt.plot(vs)
plt.show()