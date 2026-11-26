"""
Práctica: Sistema Respiratorio (Asma)

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Prado, Cerano, Contreras
Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Librerias
import control as ctrl
import numpy as np
import matplotlib.pyplot as plt


# Datos Generales de la Simulacion
x0,t0,tend,dt,w,h = 0,0,15,1E-3,12,7
N = round((tend-t0)/dt) + 1
t = np.linspace(t0,tend,N)


# Funcion de transferencia
def sistema(R1,R2,R3,C,L):
    num = [R3]
    den = [R1*C*L, L + R1*C*(R2+R3), R1+R2+R3]
    sys = ctrl.tf(num,den)
    L_polos = np.roots(den)
    return sys,L_polos


# Funcion de transferencia: Control
R1,R2,R3,C,L = 200,100,1000,1E-3,1E-5
syscontrol,L1 = sistema(R1,R2,R3,C,L)
print(f'Funcion de transferencia del control: {syscontrol}')
print(f"Polos del sistema: L1 = {L1[0]:.3e}, L2 = {L1[1]:.3e}\n")


# Funcion de transferencia: Caso
R1,R2,R3,C,L = 200,800,1000,1E-3,1E-5
syscaso,L2 = sistema(R1,R2,R3,C,L)
print(f'Funcion de transferencia del caso: {syscaso}')
print(f"Polos del sistema: L1 = {L2[0]:.3e}, L2 = {L2[1]:.3e}\n")


# Componentes del controlador
kP,kI,kD = 234.6505,46336.0566,0.038703
Cr = 1E-6
Re = 1/(Cr*kI)
Rr = kP*Re
Ce = kD/Rr

numPID = [Re*Rr*Ce*Cr,Re*Ce+Rr*Cr,1]
denPID = [Re*Cr,0]
PID = ctrl.tf(numPID,denPID)


# Sistema de control en lazo cerrado
sysPID = ctrl.feedback(ctrl.series(PID,syscaso),1,sign = -1)
print(f"Función de transferencia en lazo cerrado: {sysPID}\n")


# Respuesta: Pulso unitario
F = np.zeros(N)
F[(t>=1) & (t<2)] = 1
_,Fsx = ctrl.forced_response(syscontrol,t,F,x0)
_,Fsy = ctrl.forced_response(syscaso,t,F,x0)
_,PID_resp = ctrl.forced_response(sysPID,t,Fsx,x0)

#Colores
clr1 = np.array([66,133,244])/255
clr2 = np.array([234,67,53])/255
clr3 = np.array([251,188,5])/255
clr4 = np.array([100,150,200])/255

# Respuestas
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman','DejaVu Serif']

fg1 = plt.figure(1,figsize=(w,h))

plt.plot(t,F,'-',linewidth=1.5,color=clr1,label='Ve(t)')
plt.plot(t,Fsx,'-',linewidth=1.5,color=clr2,label='Fs(t): Control')
plt.plot(t,Fsy,'--',linewidth=1.5,color=clr3,label='Fs(t): Caso')
plt.plot(t,PID_resp,'--',linewidth=1.5,color=clr4,label='PID(t): Tratamiento')

plt.grid(False)
plt.xlim(0,10)
plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.1)
plt.yticks(np.round(np.arange(0,1.11,0.1),1))

plt.xlabel('t [s]')
plt.ylabel('Fs(t) [V]')

plt.legend(bbox_to_anchor=(0.5,1.08),loc='center',ncol=4,frameon=False)

fg1.savefig('impulso_unitario_python.pdf',bbox_inches='tight')
plt.show()