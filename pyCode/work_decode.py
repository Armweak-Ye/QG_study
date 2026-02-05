code = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;Mission:2025-RESCUE-X "
no_space_code=code.replace(' ','')
word = no_space_code.split(';')

name = word[0]
coords = word[1]
items = word[2]
mission = word[3]

no_head_items = items.replace('Items:','')
no_head_items = no_head_items.replace(',',' ')
single_items = no_head_items.split()
unique_items = list(set(single_items))

no_head_name = name.replace('Agent:','')
no_head_coords = coords.replace('Coords:','')
tuple_coords = tuple(no_head_coords)
no_head_mission = mission.replace('Mission:','')

decode = {'name':no_head_name,'coords':no_head_coords,
          'items':unique_items,'mission':no_head_mission}
print(decode)