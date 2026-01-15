Pdc = 10e3;
Vll = 400;
f = 50;
wref = 2 * pi * f;
Vdcref = 700;
Vbat = 800;
Rbat = (Vdcref / Pdc) * (Vbat - Vdcref);
Rbat
ka = Vdcref / 2;
Vq = 1.5 * sqrt(2) + Vll / sqrt(3);
Ll = 5e-3;
Rl = 0.002;
Cl = 2000e-6;
Pl = 10e3;
fsw = 5e3*3; 
tau_fl = 1 / (2 * pi * 100);

% Current controller
fbwi = fsw / 10;
kpi = 2 * pi * fbwi * Ll / ka;
kpi
kii = 2 * pi * fbwi * Rl / ka;
kii
tau_il = Rl / ka / kii;
fbwi

% Voltage controller
kiw = Vq / Vdcref;
kiw
tau1l = tau_fl + tau_il;
f_vc=1/tau1l;
f_vc
PM_l = pi * 60 / 180;
a_l = tan(PM_l) + sqrt(tan(PM_l)^2 + 1);
a_l
kpw = 2 * Cl / (kiw * a_l * tau1l);
kpw