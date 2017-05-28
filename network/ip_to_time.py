def extractip(ipaddress):
	valueip = ipaddress.split(".")
	minimalip = "".join(valueip[2:4])
	hour = str(int(minimalip) % 24)
	minutes = str(minimalip)[-2:] 
	x = int(minutes)
	lastoctet = ["51", "52", "53", "54", "55", "55",
				"56", "57", "58" "81", "82"]
	if minutes in lastoctet:
 		minutes = str(lastoctet.index(minutes) * 5)
 	else:
 		minutes = str(x % 60)

 	minutes = "{:0>2}".format(minutes)
	return hour+":"+minutes

print extractip("10.40.111.82")