urls = ["Belt Size Calculator","Wheel Offset Calculator","Flight Radiation Calculator","Gas Calculator","MPG Calculator","RPM Calculator","Speed Calculator","Speedometer Gear Calculator","Tesla Charging Cost Calculator","Ticket Optimizer","Tire Size Calculator","Traffic Density Calculator","Boat Speed Calculator","Commute Calculator","Tree Height Calculator","Log Reduction Calculator","Protein Molecular Weight Calculator"]
# print(len(urls))

with open("urls.py", 'w') as u:
  for i in urls:
    urlPath = i.lower().replace(' ','-') + "/"
    viewfunction = i.lower().replace(' ','')
    u.write(f'path("{urlPath}",{viewfunction}),\n'.strip('"'))

with open("views.py", 'w') as v:
  for i in urls:
    viewfunction = i.lower().replace(' ','')
    print(viewfunction)
    v.write(f'def {viewfunction}(request):\n'.strip('"') + f'  return render(request,"{viewfunction}.html")\n\n'.strip('"'))
    open("templates/"+viewfunction+".html", "w")




    
