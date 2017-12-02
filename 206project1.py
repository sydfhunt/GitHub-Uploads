import os
import operator
import csv
from datetime import datetime, date
import filecmp

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.

	#Your code here:
	dictreader = csv.DictReader(open(file))
	dict_list = []
	for line in dictreader:
		dict_list.append(line)
	return (dict_list)


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	sort = sorted(data, key=operator.itemgetter(col))
	firstLast = sort[0]['First'] + " " + sort[0]['Last']
	return(firstLast)


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	d = {}
	for x in data:
		# print(x['Class'])
		if "Senior" == x["Class"]:
			d["Senior"] = d.get("Senior",0) + 1
			# print(dict1)
		if "Junior" == x["Class"]:
 			d["Junior"] = d.get("Junior",0) + 1
		if "Sophomore" == x["Class"]:
			d["Sophomore"] = d.get('Sophomore',0) + 1
		if "Freshman" == x["Class"]:
			d["Freshman"] = d.get('Freshman',0) + 1
	#--------------------------------------------------------------------
	x = sorted(d.items(), key=operator.itemgetter(1), reverse = True)
	return(x)




# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	list_wkdays = []
	split_wkdays = []
	dict_days = {}
	for b in a:
		dob = b.get('DOB')
		split_days = dob.split('/')
		split_wkdays.append(split_days)
	for z in split_wkdays:
		list_wkdays.append(z[1])
	for wkday in list_wkdays:
		dict_days[wkday] = dict_days.get(wkday, 0) + 1
	final_dict = sorted(dict_days.items(), key = lambda x:x[1], reverse = True)
	return int(final_dict[0][0])



# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	list_bday = []
	list_age = []
	today_date = date.today()
	for t in a:
		dob_ = t.get('DOB')
		bday1 = datetime.strptime(dob_, "%m/%d/%Y")
		list_bday.append(bday1)
	for y in list_bday:
		age = today_date.year - y.year - ((today_date.month, today_date.day) < (y.month, y.day))
		list_age.append(age)
	added_age = sum(list_age)
	age_count = len(list_age)
	avg_age = round(added_age / age_count)
	return avg_age


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	csv = open(fileName, 'w')
	sortlist = sorted(a, key = lambda k: k[col])
	for element in sortlist:
		temp = []
		for value in element.values():
			temp.append(value)
		row = ",".join(temp[:3])
		csv.write(row + "\n")

#I believe my code is correct here but am getting errors

	csv.close()
	return None



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
