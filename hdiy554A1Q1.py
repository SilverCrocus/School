"""
Name: Hivin Diyagama
Username: hdiy554
ID: 365061211

Surface area and volume calculator of a dodecahedron
"""




import math


banner_line = "##################################"
print(banner_line)
print("       Regular Dodecahedron")
print("Surface Area and Volume Calculator")
print(banner_line)
print()
prompt = "Edge Length: "
edge_length = float(input(prompt))
surface_area1 = (math.sqrt(5) * 10 + 25)  #steps broken down to calculate surface area
surface_area1 = (3 * math.sqrt(surface_area1))
surface_area1 = round(edge_length**2 * surface_area1, 3)
volume1 = 15 + 7 * math.sqrt(5)  #steps broken down to calculate volume.
volume1 = volume1 / 4
volume1 = round(volume1 * math.pow(edge_length,3), 3)


print("Surface Area:", surface_area1)
print("Volume:", volume1)


