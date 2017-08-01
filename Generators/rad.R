zg = c(64.9,90.0,139.0,164.0,163.9,167.0,122.9,160.0,191.9,197.0,228.2,113.7,103.3,95.4,121.5,124.7,149.4,117.3,142.2,167.3,194.0)

summa = sum(g)

lat = length(g)

avg = summa/lat

print(avg) 

V = avg 

PI = 3.14

radius_from_vol = function(vol){
  r = ((3*vol)/(4*PI))^(1/3)
}

Vsph = 4062.3184800000004

height_from_radius = function(h){
  r = 3
  height = h/(PI*(r^2))
  print(height)
}

r = radius_from_vol(V)
print(r)

height_from_radius(Vsph)

radii = c(5.1,2.35,2.35,3.65,2.45,2.35,3.05,3.65,3.6,3.9,3.65,4.6,4.25,4.25,2.95,2.2,2.25,4.65,4.45,2.35)
tot = sum(radii)
avg = tot/20
print(avg)






















