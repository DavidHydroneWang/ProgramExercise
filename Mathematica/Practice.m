(* ::Package:: *)

(* ::Title:: *)
(*ProgramPratice*)


(* ::Section:: *)
(*Polynomials and Rational Functions*)


Manipulate[Factor[x^n \[Minus] 1], {n, 2, 10, 1, Appearance -> "Labeled"}]


Log[Exp[x]]


Exp[2 Pi I]


SetPrecision[Log[%21],10]


a = f [g[x, 1], h[y, z, 2]]


TreeForm[a]


a = 2*x^2*y*z


a/.x^n_*y^m_.->f[n,m]


a = 2*x*y*z


a/.x^n_.*y^m_.->f[n,m]


a = {2*x*y*z, 2 * x^2 * y * z, 2 * x ^ 2 * y ^ 3 * z, 2 * x ^ 2 * z/y, 2 * x ^ 2 * z,
2 *z}


s = {x^l_. * f[n_,m_] -> f[n+l,m],y^l_. * f[n_,m_] -> f[n,m+l] }


a*f[0,0]//.s


a = {x + y + z + 2, 2 * x + y + z + 2, 2 * x + 3 * y + z + 2, 2 * x \[Minus] y + z + 2,
x + z + 2, z + 2}


s = {x*l_. + f[n_,m_] -> f[n+l,m],y*l_. + f[n_,m_] -> f[n,m+l] }


a+f[0,0]//.s
































Quit[];
