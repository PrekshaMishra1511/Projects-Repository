Vg= 800;
Ra= 0.052;
La= 0.001;
fsw= 2000;
wref= 625*2*pi/60; %
ke= 3.65;
p= 250*745.7;
J= 5;
wref

wbwi=2*pi*(fsw/5); %
Kii= wbwi*Ra/Vg;   
Kpi= Kii*La/Ra;
wbwi
Kii
Kpi

Tl= p/wref;
imax=Tl/ke;
Tfil= 1/20;
a= (1+sqrt(3))/2; % PM=54 deg
Kiw= J/(ke*Tfil*Tfil*a*a*a);
Kpw= J/(ke*Tfil*a);
wbww=Kiw*a/Kpw;
wbww
Kiw
Kpw

W= 625;
T= Tl;