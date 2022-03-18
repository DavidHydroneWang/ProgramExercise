(* ::Package:: *)

(* ::Section:: *)
(*ProgramPratice*)


Y2 = m11^2 cb^2 + m22^2 sb^2 - m12^2 s2b cosE


Z3 = 1/4*(lam1 + lam2 - 2 lam3 - 2 lam4 - 2 lam5 cos2E)*s2b^2 + lam3 -(lam6 -lam7)s2b c2b cosE 


Z4 = 1/4*(lam1 + lam2 - 2 lam3 - 2 lam4 - 2 lam5 cos2E)*s2b^2 + lam4 -(lam6 -lam7)s2b c2b cosE 


Z5 = E^(- 2 I arccosE) (1/4*(lam1 + lam2 - 2 lam3 - 2 lam4 - 2 lam5 cos2E)*s2b^2 + lam5 cos2E -(lam6 -lam7)s2b c2b cosE  + I( lam5 c2b sin2E -(lam6 -lam7)s2b  sinE ))


cosE = 0;
cos2E = -1;
sinE = 1;
sin2E = 0;
arccosE = Pi/2;
lam6 =0;
lam7 = 0;


Y2


Z3


Z4 -Z5//Simplify


Z5


mhp^2/.{ mhp^2 -> Y2 + 1/2 Z3 v^2}


ma^2 /.{ma^2 ->Y2 + 1/2 (Z3 +Z4 -Z5) v^2}


mhp^2-ma^2/.{mhp^2 -> Y2 + 1/2 Z3 v^2,ma^2 ->Y2 + 1/2 (Z3 +Z4 -Z5) v^2}//Simplify


Quit[];


Mh = 125;
MH = 150;
Mh2 = Mh^2;
MH2 = MH^2;
cba=0;
sba=1;
tan2B = Tan[Pi/4];
Z4 = Z5 = -2;
Z7 = 0;
v =100;


Z6 = (Mh2-MH2)*sba*cba/v^2


lam5 = Z5 + 1/2*(Z6 - Z7)tan2B


MA2= MH2*sba^2+Mh2*cba^2 -Z5*v^2


MHP2 = MA2 - 1/2(Z4-Z5)v^2


Quit[];
