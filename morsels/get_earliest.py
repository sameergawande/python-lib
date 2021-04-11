#!/usr/bin/env python3
def get_earliest(date1,date2):
	mm1,dd1,yyyy1=date1.split("/")
	mm2,dd2,yyyy2=date2.split("/")
	if (yyyy1 < yyyy2):
		return date1
	elif (yyyy1 < yyyy2):
		return date2
	elif (mm1 < mm2):
		return date1
	elif (mm1 > mm2):
		return date2
	elif (dd1 < dd2):
		return date1
	else:
		return date2
print (get_earliest("01/03/33","01/01/33"))
